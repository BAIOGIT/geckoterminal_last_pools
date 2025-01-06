import requests

API_URL = "https://api.geckoterminal.com/api/v2/{endpoint}"

def fetch_new_pools_data(page=1):
    """Fetch pools data from Geckoterminal API."""
    params = {
        "included": "raydium",
        "page": page,
    }
    
    response = requests.get(API_URL.format(endpoint='networks/solana/new_pools'), params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return {}

def fetch_trending_pools_data(page=1):
    """Fetch pools data from Geckoterminal API."""
    params = {
        "included": "raydium",
        "page": page,
    }
    
    response = requests.get(API_URL.format(endpoint='networks/solana/trending_pools'), params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return {}

def fetch_trades_data(pool_address):
    """Fetch trades data from Geckoterminal API."""
    response = requests.get(API_URL.format(endpoint=f'networks/solana/pools/{pool_address}/trades'))
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return {}

def fetch_ohlcv_data(pool_address, timeframe='hour', period=1):
    """Fetch trades data from Geckoterminal API."""
    response = requests.get(API_URL.format(endpoint=f'networks/solana/pools/{pool_address}/ohlcv/{timeframe}?aggregate={period}'))
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return {}
