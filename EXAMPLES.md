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

## Historical Index Data

```python
from nepse_data_api import Nepse

nepse = Nepse()

# 1. Get the latest day's data for the NEPSE Index
latest_nepse = nepse.get_index_history("nepse")
print(f"NEPSE on {latest_nepse[0]['businessDate']}: {latest_nepse[0]['closingIndex']}")

# 2. Get a historical date range for the Banking sub-index
banking_history = nepse.get_index_history(
    "banking", 
    start_date="2026-08-01", 
    end_date="2026-08-31"
)
print(f"Banking Index returned {len(banking_history)} days of history.")

# 3. Get the latest day's data for ALL indices at once
all_indices = nepse.get_index_history("all")
for name, data in all_indices.items():
    if data:
        print(f"{name}: {data[0]['closingIndex']} ({data[0]['percentageChange']}%)")
```

## Corporate Actions & Dividends

```python
from nepse_data_api import Nepse

nepse = Nepse()

# 1. Compact corporate actions per fiscal year (bonus share %, cash dividend %, right share %)
corp_actions = nepse.get_corporate_actions("NABIL")
for ca in corp_actions[:3]:
    print(f"FY: {ca.get('fiscalYear')} | Bonus: {ca.get('bonusPercentage')}% | Cash: {ca.get('cashDividend')}%")

# 2. Detailed dividend notices (with AGM date, book-close date, PDF documents)
dividends = nepse.get_dividends("NABIL")
for div in dividends[:2]:
    news = div.get("companyNews", {})
    print(news.get("newsHeadline"))
```

## Financial Reports (Quarterly / Annual)

```python
from nepse_data_api import Nepse

nepse = Nepse()

# Get quarterly and annual balance sheet reports (EPS, PE, Net Worth Per Share, Profit)
reports = nepse.get_financial_reports("NABIL")
for r in reports[:3]:
    fr = r.get("fiscalReport") or {}
    fy = (fr.get("financialYear") or {}).get("fyNameNepali")
    quarter = (fr.get("quarterMaster") or {}).get("quarterName")
    print(f"{fy} ({quarter}) -> EPS: {fr.get('epsValue')}, PE: {fr.get('peValue')}, NWPS: {fr.get('netWorthPerShare')}")
```

## Broker Information (Floorsheet Trades by Broker)

```python
from nepse_data_api import Nepse

nepse = Nepse()

# Filter today's floorsheet transactions for a specific broker (e.g. Broker #1)
trades = nepse.get_broker_trades(broker_id=1, limit=5)
print(f"Total Broker #1 trades: {trades.get('totalTrades')}")
for t in trades.get("records", [])[:3]:
    print(f"Symbol: {t.get('stockSymbol')} | Qty: {t.get('contractQuantity')} | Rate: {t.get('contractRate')}")
```

## Stock Price History (OHLCV)

```python
from nepse_data_api import Nepse

nepse = Nepse()

# Per-security datewise OHLCV
ohlcv = nepse.get_stock_ohlcv("NABIL", size=10)
for row in ohlcv[:5]:
    print(f"{row.get('businessDate')} | O:{row.get('openPrice')} H:{row.get('highPrice')} L:{row.get('lowPrice')} C:{row.get('lastTradedPrice')} V:{row.get('totalTradeQuantity')}")
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

For a complete list of all endpoints and parameters, see [available_apis.md](available_apis.md) or check the [`tests/`](tests/) directory.
