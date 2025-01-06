
from collections import defaultdict

def analyze_highly_profitable_trades(trades_data):
    wallet_trades = defaultdict(lambda: {"buy": [], "sell": []})

    # Organize trades by wallet
    for trade in trades_data.get("data", []):
        trade_details = trade["attributes"]
        wallet = trade_details["tx_from_address"]
        kind = trade_details["kind"]
        tx_hash = trade_details["tx_hash"]  # Extract transaction hash
        
        # Add trade to the wallet's buy or sell list
        wallet_trades[wallet][kind].append({
            "from_token_amount": float(trade_details["from_token_amount"]),
            "to_token_amount": float(trade_details["to_token_amount"]),
            "price_from_in_usd": float(trade_details["price_from_in_usd"]),
            "price_to_in_usd": float(trade_details["price_to_in_usd"]),
            "block_timestamp": trade_details["block_timestamp"],
            "tx_hash": tx_hash,  # Store the transaction hash
            "coin": trade_details["to_token_address"],  # Ensure coin is available
            "amount": float(trade_details.get("amount", 0)),  # Ensure amount is available
            "cost_usd": float(trade_details.get("cost_usd", 0))  # Ensure cost_usd is available
        })

    # Find wallets with over 200% profit
    very_profitable_wallets = []
    for wallet, trades in wallet_trades.items():
        total_buys = sum(trade["to_token_amount"] for trade in trades["buy"])
        total_buy_cost = sum(trade["from_token_amount"] * trade["price_from_in_usd"] for trade in trades["buy"])

        total_sells = sum(trade["from_token_amount"] for trade in trades["sell"])
        total_sell_value = sum(trade["to_token_amount"] * trade["price_to_in_usd"] for trade in trades["sell"])

        # Calculate net profit in USD and percentage profit
        if total_sells > 0 and total_buys > 0:
            net_profit = total_sell_value - total_buy_cost
            if net_profit > 0:  # Only track profitable wallets
                percentage_profit = (net_profit / total_buy_cost) * 100
                if percentage_profit > 200:
                    # Add transaction hashes for both buy and sell trades
                    buy_tx_hashes = [trade["tx_hash"] for trade in trades["buy"]]
                    sell_tx_hashes = [trade["tx_hash"] for trade in trades["sell"]]
                    
                    # Get the coin associated with the wallet (we assume the first 'buy' trade's coin is the one to track)
                    coin = trades["buy"][0]["coin"] if trades["buy"] else "Unknown Coin"

                    very_profitable_wallets.append({
                        "wallet": wallet,
                        "coin": coin,  # Include coin in the result
                        "buy_cost_usd": total_buy_cost,
                        "sell_value_usd": total_sell_value,
                        "net_profit": net_profit,
                        "percentage_profit": percentage_profit,
                        "buy_tx_hashes": buy_tx_hashes,  # List of buy transaction hashes
                        "sell_tx_hashes": sell_tx_hashes,  # List of sell transaction hashes
                        "buy": trades["buy"]  # Include buy trades
                    })

    return very_profitable_wallets
