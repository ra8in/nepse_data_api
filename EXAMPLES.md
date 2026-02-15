# Examples

Ready-to-run examples demonstrating nepse_data_api usage.

## Basic Usage

```python
from nepse_data_api import Nepse

nepse = Nepse()
stocks = nepse.get_stocks()
print(f"Got {len(stocks)} stocks")
```

## Get Specific Stock

```python
from nepse_data_api import Nepse

nepse = Nepse()
stocks = nepse.get_stocks()

# Filter for NABIL
nabil = next((s for s in stocks if s['symbol'] == 'NABIL'), None)

if nabil:
    print(f"{nabil['securityName']}")
    print(f"  LTP: {nabil['lastTradedPrice']}")
    print(f"  Volume: {nabil['totalTradeQuantity']}")
```

## Monitor Top Gainers

```python
from nepse_data_api import Nepse

nepse = Nepse()
gainers = nepse.get_top_gainers(limit=5)

for stock in gainers:
    print(f"{stock['symbol']:6} +{stock.get('percentageChange', 0):.2f}%")
```

## Historical Data

```python
from datetime import date
from nepse_data_api import Nepse

nepse = Nepse()

# Get data for today
today = date.today().strftime("%Y-%m-%d")
stocks = nepse.get_stocks(date=today)

for stock in stocks[:5]:
    print(f"{stock['symbol']}: {stock['closePrice']}")
```

## Track Portfolio

```python
from nepse_data_api import Nepse

# Your holdings
portfolio = {
    'NABIL': 50,
    'ADBL': 100,
    'NICA': 200
}

nepse = Nepse()
stocks = nepse.get_stocks()

total_value = 0
for symbol, quantity in portfolio.items():
    stock = next((s for s in stocks if s['symbol'] == symbol), None)
    if stock:
        value = stock['lastTradedPrice'] * quantity
        total_value += value
        print(f"{symbol}: {quantity} @ {stock['lastTradedPrice']} = Rs. {value:,.2f}")

print(f"\nTotal Portfolio Value: Rs. {total_value:,.2f}")
```

## Async Example

```python
import asyncio
from nepse_data_api import AsyncNepse

async def monitor_market():
    nepse = AsyncNepse()
    
    while True:
        stocks = await nepse.get_stocks()
        index = await nepse.get_nepse_index()
        
        # Check if we got valid data (index is list)
        if index and isinstance(index, list):
             print(f"NEPSE: {index[0]['close']} ({index[0]['perChange']}%)")
        
        print(f"Stocks trading: {len(stocks)}")
        
        await asyncio.sleep(60)  # Update every minute

asyncio.run(monitor_market())
```

See the `test_suite/` directory for comprehensive examples of all features.
