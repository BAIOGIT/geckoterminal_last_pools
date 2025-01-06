from datetime import datetime
import sqlite3
import time

def get_wallet_transactions(wallet_address: str):
    """
    Fetch the transaction history for a given wallet address from the wallet_transaction_hashes table,
    including transaction hashes, trade types (buy/sell), and timestamps.
    
    :param wallet_address: Wallet address to retrieve transactions.
    :return: List of dictionaries containing transaction data (tx_hash, trade_type, timestamp).
    """
    connection = sqlite3.connect('db/geckoterminal.db')
    cursor = connection.cursor()

    # Fetch transaction hashes and trade types for the given wallet
    cursor.execute("""
        SELECT tx_hash, trade_type, timestamp
        FROM wallet_transaction_hashes
        WHERE wallet_address = ?
    """, (wallet_address,))
    transactions = cursor.fetchall()

    connection.close()

    return [
        {
            "tx_hash": tx_hash[0],
            "trade_type": tx_hash[1],
            "timestamp": tx_hash[2]
        }
        for tx_hash in transactions
    ]


def get_wallet_profit(wallet_address: str):
    """
    Fetch the total profit for a given wallet address from the highly_profitable_wallets table.
    
    :param wallet_address: Wallet address to retrieve profits.
    :return: Profit of the wallet.
    """
    connection = sqlite3.connect('db/geckoterminal.db')
    cursor = connection.cursor()

    cursor.execute("""
        SELECT percentage_profit
        FROM highly_profitable_wallets
        WHERE wallet_address = ?
    """, (wallet_address,))
    result = cursor.fetchone()
    connection.close()

    return result[0] if result else 0


def analyze_wallet_transactions(wallet_address: str):
    """
    Analyze wallet transactions and classify as insider, bot, or normal.
    Incorporates transaction frequency, type ratio, transaction intervals, and profit.
    
    :param wallet_address: Wallet address to analyze.
    :return: Classification string: 'Insider', 'Bot', or 'Normal'.
    """
    transactions = get_wallet_transactions(wallet_address)

    if len(transactions) < 2:
        return "Normal"  # Not enough data for analysis

    # Sort transactions by timestamp for time-based analysis
    transactions.sort(key=lambda x: x['timestamp'])

    # Count buy and sell transactions
    buy_count = sum(1 for tx in transactions if tx['trade_type'] == 'buy')
    sell_count = sum(1 for tx in transactions if tx['trade_type'] == 'sell')
    
    # Calculate the transaction intervals (in seconds)
    transaction_times = [datetime.strptime(tx['timestamp'], '%Y-%m-%d %H:%M:%S') for tx in transactions]
    intervals = [(transaction_times[i] - transaction_times[i - 1]).total_seconds() for i in range(1, len(transaction_times))]

    # Metrics
    total_transactions = len(transactions)
    buy_sell_ratio = buy_count / total_transactions
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    # print(f"Average Transaction Interval: {avg_interval:.2f} seconds")

    # Get the total profit for the wallet
    total_profit = get_wallet_profit(wallet_address)

    # Classify based on frequency, trade behavior, and profitability
    if avg_interval < 60 * 0.5:  # If transactions are frequent (less than a minute apart)
        classification = "Bot"
    # elif buy_sell_ratio > 0.5 and total_profit > 200:  # More buys than sells and significant profits
    #     classification = "Insider"
    # elif sell_count > buy_count:  # More sells than buys (Could be a Bot)
    #     classification = "Bot"
    elif total_profit > 2000 and total_transactions < 20:  # If the wallet has made significant profits
        classification = "Insider"
    else:
        classification = "Normal"  # Regular trading behavior

    return classification


def detect_and_classify_wallets():
    """
    Detect and classify wallets as insiders or bots based on their trade behavior.
    Saves the insiders to the database.
    """
    connection = sqlite3.connect('db/geckoterminal.db')
    cursor = connection.cursor()

    # Fetch all wallets that we want to classify
    cursor.execute("SELECT wallet_address FROM highly_profitable_wallets")
    wallets = cursor.fetchall()
    connection.close()

    # Analyze each wallet
    for wallet_address in wallets:
        wallet_address = wallet_address[0]
        classification = analyze_wallet_transactions(wallet_address)

        if classification == "Normal" or classification == "Bot":
            continue  # Skip normal or bot classifications

        # Save the classification to the database only if it's not already classified as 'Insider'
        connection = sqlite3.connect('db/geckoterminal.db')
        cursor = connection.cursor()

        # Check if the wallet already exists in the classifications table
        cursor.execute("""
            SELECT COUNT(*) FROM wallet_classifications WHERE wallet_address = ?
        """, (wallet_address,))
        result = cursor.fetchone()

        if result[0] == 0:  # If the wallet does not exist, insert it
            print(f"Found new {classification} wallet: {wallet_address}")

            cursor.execute("""
                INSERT INTO wallet_classifications (wallet_address, classification)
                VALUES (?, ?)
            """, (wallet_address, classification))
        else:  # If it exists, update it
            cursor.execute("""
                UPDATE wallet_classifications
                SET classification = ?
                WHERE wallet_address = ?
            """, (classification, wallet_address))

        connection.commit()
        connection.close()


# Sample usage in the main module
detect_and_classify_wallets()

if __name__ == "__main__":
    while True:
        detect_and_classify_wallets()
        time.sleep(30)