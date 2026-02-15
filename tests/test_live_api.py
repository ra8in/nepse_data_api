from nepse_data_api import Nepse
import json
import sys

def main():
    print("--- NEPSE Live API Test ---")
    
    try:
        # 1. Initialize Nepse (this triggers authentication and WASM descrambling)
        print("\n1. Initializing Nepse/Authenticating...")
        nepse = Nepse(enable_cache=False)
        print("✓ Authentication successful.")

        # 2. Get Market Status
        print("\n2. Fetching Market Status...")
        status = nepse.get_market_status()
        print(f"✓ Market Status: {'Open' if status.get('isOpen') == 'OPEN' else 'Closed'} (As of: {status.get('asOf')})")

        # 3. Get Market Summary
        print("\n3. Fetching Market Summary...")
        summary = nepse.get_market_summary()
        # Summary is usually a list of dicts or a single dict
        if summary:
            print(f"✓ Market Summary fetched. Found {len(summary) if isinstance(summary, list) else 1} entries.")
        else:
            print("! Market Summary returned empty.")

        # 4. Get NEPSE Index
        print("\n4. Fetching NEPSE Index...")
        index_data = nepse.get_nepse_index()
        if index_data:
            # Handle potential nested structure
            current_index = index_data[0].get('currentValue') if isinstance(index_data, list) and index_data else index_data.get('currentValue')
            print(f"✓ NEPSE Index: {current_index}")
        else:
            print("! NEPSE Index data not found.")

        # 5. Get Top Gainers
        print("\n5. Fetching Top Gainers...")
        gainers = nepse.get_top_gainers(limit=3)
        print(f"✓ Top 3 Gainers:")
        for stock in gainers:
            print(f"  - {stock.get('symbol')}: {stock.get('lastTradedPrice')} ({stock.get('percentageChange')}%)")

        # 6. Get Live Stock Prices
        print("\n6. Fetching Live Stock Prices (First 5)...")
        stocks = nepse.get_stocks()
        print(f"✓ Total Stocks: {len(stocks)}")
        for i, stock in enumerate(stocks[:5]):
            print(f"  {i+1}. {stock.get('symbol')}: OHLC {stock.get('openPrice')}/{stock.get('highPrice')}/{stock.get('lowPrice')}/{stock.get('closePrice')}")

        print("\n--- Test Completed Successfully ---")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        # Print traceback details if needed
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
