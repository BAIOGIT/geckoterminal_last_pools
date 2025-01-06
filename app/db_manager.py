import sqlite3
from typing import List, Dict

DB_FILE = "db/geckoterminal.db"

def init_database():
    """
    Initialize the database, creating tables if they do not exist.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Table for highly profitable wallets (include coin column)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS highly_profitable_wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT NOT NULL,
            coin TEXT NOT NULL,  -- Added column to store coin information
            buy_cost_usd REAL NOT NULL,
            sell_value_usd REAL NOT NULL,
            net_profit REAL NOT NULL,
            percentage_profit REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table for coins bought by wallets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallet_coin_purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT NOT NULL,
            coin TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table for storing transaction hashes for profitable wallets' trades
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallet_transaction_hashes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT NOT NULL,
            tx_hash TEXT NOT NULL,
            trade_type TEXT NOT NULL,  -- 'buy' or 'sell'
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Table for storing transaction hashes for profitable wallets' trades
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallet_classifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT NOT NULL,
            classification TEXT NOT NULL,  -- 'Insider', 'Bot', or 'Normal'
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_profitable_wallets(wallets: List[Dict]):
    """
    Save a list of profitable wallets to the database.

    :param wallets: List of dictionaries containing wallet data.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for wallet in wallets:
        cursor.execute("""
            INSERT INTO highly_profitable_wallets (
                wallet_address, coin, buy_cost_usd, sell_value_usd, net_profit, percentage_profit
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            wallet["wallet"],
            wallet["coin"],  # Save the coin
            wallet["buy_cost_usd"],
            wallet["sell_value_usd"],
            wallet["net_profit"],
            wallet["percentage_profit"]
        ))

    connection.commit()
    connection.close()


def save_wallet_coin_purchases(purchases: List[Dict]):
    """
    Save a list of coin purchases made by wallets.

    :param purchases: List of dictionaries containing coin purchase data.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for purchase in purchases:
        cursor.execute("""
            INSERT INTO wallet_coin_purchases (
                wallet_address, coin
            ) VALUES (?, ?)
        """, (
            purchase["wallet_address"],
            purchase["coin"]
        ))

    connection.commit()
    connection.close()

def save_wallet_tx_hashes(wallet_address: str, tx_hashes: List[str], trade_type: str):
    """
    Save transaction hashes for a specific wallet.

    :param wallet_address: The wallet address to associate the tx_hashes with.
    :param tx_hashes: List of transaction hashes to store.
    :param trade_type: The type of trade, either 'buy' or 'sell'.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for tx_hash in tx_hashes:
        cursor.execute("""
            INSERT INTO wallet_transaction_hashes (
                wallet_address, tx_hash, trade_type
            ) VALUES (?, ?, ?)
        """, (
            wallet_address,
            tx_hash,
            trade_type
        ))

    connection.commit()
    connection.close()

def get_profitable_wallets(min_percentage: float = 200.0) -> List[Dict]:
    """
    Retrieve all wallets with a profit percentage above the specified threshold.

    :param min_percentage: Minimum profit percentage to filter wallets.
    :return: List of dictionaries containing wallet data.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT wallet_address, buy_cost_usd, sell_value_usd, net_profit, percentage_profit, timestamp
        FROM highly_profitable_wallets
        WHERE percentage_profit > ?
    """, (min_percentage,))

    rows = cursor.fetchall()

    # Now fetch the tx_hash for each wallet
    profitable_wallets = []
    for row in rows:
        wallet_address = row[0]
        cursor.execute("""
            SELECT tx_hash, trade_type
            FROM wallet_transaction_hashes
            WHERE wallet_address = ?
        """, (wallet_address,))

        tx_hashes = cursor.fetchall()
        buy_tx_hashes = [tx_hash[0] for tx_hash in tx_hashes if tx_hash[1] == "buy"]
        sell_tx_hashes = [tx_hash[0] for tx_hash in tx_hashes if tx_hash[1] == "sell"]

        profitable_wallets.append({
            "wallet_address": row[0],
            "buy_cost_usd": row[1],
            "sell_value_usd": row[2],
            "net_profit": row[3],
            "percentage_profit": row[4],
            "timestamp": row[5],
            "buy_tx_hashes": buy_tx_hashes,
            "sell_tx_hashes": sell_tx_hashes
        })

    connection.close()

    return profitable_wallets

def get_wallet_coin_purchases(wallet_address: str) -> List[Dict]:
    """
    Retrieve all coin purchases for a given wallet.

    :param wallet_address: Wallet address to filter purchases.
    :return: List of dictionaries containing coin purchase data.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT coin, timestamp
        FROM wallet_coin_purchases
        WHERE wallet_address = ?
    """, (wallet_address,))

    rows = cursor.fetchall()
    connection.close()

    return [
        {
            "coin": row[0],
            "timestamp": row[1]
        }
        for row in rows
    ]

def delete_old_data(days: int):
    """
    Delete data older than a specified number of days.

    :param days: Number of days to retain data.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Delete old profitable wallet data
    cursor.execute("""
        DELETE FROM highly_profitable_wallets
        WHERE timestamp < DATETIME('now', ?)
    """, (f"-{days} days",))

    # Delete old coin purchases
    cursor.execute("""
        DELETE FROM wallet_coin_purchases
        WHERE timestamp < DATETIME('now', ?)
    """, (f"-{days} days",))

    connection.commit()
    connection.close()