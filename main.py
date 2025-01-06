import time
from app.fetch_data import fetch_new_pools_data, fetch_trending_pools_data, fetch_trades_data
from app.db_manager import init_database, save_profitable_wallets, save_wallet_coin_purchases, save_wallet_tx_hashes
from app.analysis import analyze_highly_profitable_trades
from app.alert import send_alert

def main():
    # Initialize database
    init_database()

    # Fetch pool data for new pools
    new_pools_data = fetch_new_pools_data()
    time.sleep(2)

    for new_pool in new_pools_data.get("data", []):
        mint_x = new_pool['relationships']['base_token']['data']['id'].replace('solana_', '')
        mint_y = new_pool['relationships']['quote_token']['data']['id'].replace('solana_', '')

        if not mint_x.endswith('pump') or mint_y != 'So11111111111111111111111111111111111111112':
            continue

        # Fetch trades data for each new_pool
        trades_data = fetch_trades_data(new_pool['attributes']['address'])
        
        # Analyze trades for highly profitable wallets (those with > 200% profit)
        very_profitable_wallets = analyze_highly_profitable_trades(trades_data)
        
        # Display and store profitable wallets
        for wallet in very_profitable_wallets:
            print(f"Highly Profitable Wallet: {wallet['wallet']}, Buy Cost: ${wallet['buy_cost_usd']:.2f}, "
                  f"Sell Value: ${wallet['sell_value_usd']:.2f}, Profit: ${wallet['net_profit']:.2f}, "
                  f"Percentage Profit: {wallet['percentage_profit']:.2f}%")

            # Save the profitable wallets in the database
            save_profitable_wallets([wallet])

            # Save the transaction hashes for buy and sell trades
            if 'buy_tx_hashes' in wallet:
                save_wallet_tx_hashes(wallet['wallet'], wallet['buy_tx_hashes'], 'buy')

            if 'sell_tx_hashes' in wallet:
                save_wallet_tx_hashes(wallet['wallet'], wallet['sell_tx_hashes'], 'sell')

            # Save coin purchases if 'buy' data exists
            if 'buy' in wallet:  # Ensure 'buy' key exists
                purchases = []
                for trade in wallet['buy']:
                    # Ensure necessary keys exist in each trade
                    purchases.append({
                        "wallet_address": wallet['wallet'],
                        "coin": mint_x,  # Default to 'Unknown Coin' if 'coin' is missing
                    })
                
                # Save the purchases to the database
                if purchases:
                    save_wallet_coin_purchases(purchases)
            else:
                print(f"No 'buy' data found for wallet {wallet['wallet']}")
            time.sleep(1)

    # Fetch pool data for trending pools
    trending_pools_data = fetch_trending_pools_data()
    time.sleep(2)
    
    for trending_pool in trending_pools_data.get("data", []):
        mint_x = trending_pool['relationships']['base_token']['data']['id'].replace('solana_', '')
        mint_y = trending_pool['relationships']['quote_token']['data']['id'].replace('solana_', '')

        if not mint_x.endswith('pump') or mint_y != 'So11111111111111111111111111111111111111112':
            continue

        # Fetch trades data for each trending_pool
        trades_data = fetch_trades_data(trending_pool['attributes']['address'])
        
        # Analyze trades for highly profitable wallets (those with > 200% profit)
        very_profitable_wallets = analyze_highly_profitable_trades(trades_data)
        
        # Display and store profitable wallets
        for wallet in very_profitable_wallets:
            print(f"Highly Profitable Wallet: {wallet['wallet']}, Buy Cost: ${wallet['buy_cost_usd']:.2f}, "
                  f"Sell Value: ${wallet['sell_value_usd']:.2f}, Profit: ${wallet['net_profit']:.2f}, "
                  f"Percentage Profit: {wallet['percentage_profit']:.2f}%")

            # Save the profitable wallets in the database
            save_profitable_wallets([wallet])

            # Save the transaction hashes for buy and sell trades
            if 'buy_tx_hashes' in wallet:
                save_wallet_tx_hashes(wallet['wallet'], wallet['buy_tx_hashes'], 'buy')

            if 'sell_tx_hashes' in wallet:
                save_wallet_tx_hashes(wallet['wallet'], wallet['sell_tx_hashes'], 'sell')

            # Save coin purchases if 'buy' data exists
            if 'buy' in wallet:  # Ensure 'buy' key exists
                purchases = []
                for trade in wallet['buy']:
                    # Ensure necessary keys exist in each trade
                    purchases.append({
                        "wallet_address": wallet['wallet'],
                        "coin": mint_x,  # Default to 'Unknown Coin' if 'coin' is missing
                    })
                
                # Save the purchases to the database
                if purchases:
                    save_wallet_coin_purchases(purchases)
            else:
                print(f"No 'buy' data found for wallet {wallet['wallet']}")
            time.sleep(1)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(30)