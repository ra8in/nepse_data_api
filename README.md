# nepse-data-api

**Python library for Nepal Stock Exchange (NEPSE)**

[![PyPI](https://img.shields.io/pypi/v/nepse-data-api.svg)](https://pypi.org/project/nepse-data-api/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**nepse-data-api** is a Python library for accessing market data from the Nepal Stock Exchange. It handles authentication, token management, and data scrambling automatically.

## ✨ Features

- ✅ **26+ API Endpoints** - Complete NEPSE data coverage (Live Market, Floorsheets, Depth, etc.)
- ✅ **WASM Authentication** - Secure, automated token generation and management
- ✅ **Smart Caching** - Built-in caching layer (5700x faster for repeated requests)
- ✅ **Async Support** - Full `async`/`await` support for high-concurrency applications
- ✅ **Validated Data** - Accurate and reliable market information

## 🚀 Quick Start

```bash
pip install nepse-data-api
```

```python
from nepse_data_api import Nepse

# Initialize
nepse = Nepse()

# Get live market data
stocks = nepse.get_stocks()
print(f"Total listed stocks: {len(stocks)}")

# Get market status
status = nepse.get_market_status()
print(f"Market is currently: {status['isOpen']}")

# Get top gainers
gainers = nepse.get_top_gainers(limit=5)
for stock in gainers:
    print(f"{stock['symbol']}: {stock['lastTradedPrice']} ({stock['percentageChange']}%)")
```

## 📖 API Reference

### Market Overview

```python
# Market status (open/close)
status = nepse.get_market_status()

# Market summary (turnover, transactions)
summary = nepse.get_market_summary()

# NEPSE main index
index = nepse.get_nepse_index()

# All sector indices
sectors = nepse.get_sub_indices()
```

### Stock Data

```python
from datetime import date

# Live stock prices (all stocks)
stocks = nepse.get_stocks()

# Historical prices for a specific date (e.g., today)
today = date.today().strftime("%Y-%m-%d")
stocks = nepse.get_stocks(date=today)

# Specific security details
# Use security ID from company list
details = nepse.get_security_details(security_id)

# Historical chart data
# Fetch chart for a date range (YYYY-MM-DD)
chart = nepse.get_historical_chart(58, start_date="2026-01-01", end_date=today)
```

### Top Performers

```python
# Top gainers
gainers = nepse.get_top_gainers(limit=10)

# Top losers
losers = nepse.get_top_losers(limit=10)

# Top by turnover / trade / transaction
turnover = nepse.get_top_turnover()
trades = nepse.get_top_trade()
trans = nepse.get_top_transaction()
```

### Company Information

```python
# Company news
news = nepse.get_company_news(symbol="NABIL")

# Dividend & AGM
dividends = nepse.get_dividends(symbol="NABIL")
agm = nepse.get_agm(symbol="NABIL")

# Metadata
companies = nepse.get_company_list()
securities = nepse.get_security_list()
```

### Trading Data

```python
# Market depth (Order Book)
depth = nepse.get_market_depth(symbol="NABIL")

# Floorsheet (Transactions)
floorsheet = nepse.get_floorsheet(symbol="NABIL")

# Daily trade statistics for a specific date
stats = nepse.get_daily_trade(date="2026-02-12")
```

## ⚡ Advanced Features

### Caching
The library includes a built-in LRU caching layer to respect NEPSE's server load and improve performance.

```python
# Customize cache TTL (default: 30s)
nepse = Nepse(cache_ttl=120, enable_cache=True)

# Force fresh data for a single request
stocks = nepse.get_stocks(use_cache=False)

# Manually clear cache
nepse.clear_cache()
```

### Async Support
For web applications or high-frequency polling, use `AsyncNepse`.

```python
import asyncio
from nepse_data_api import AsyncNepse

async def main():
    nepse = AsyncNepse()
    
    # Parallel fetching
    status, stocks = await asyncio.gather(
        nepse.get_market_status(),
        nepse.get_stocks()
    )
    print(status, len(stocks))

asyncio.run(main())
```

## 📊 Performance

| Operation | Fresh Request | Cached | Improvement |
|-----------|---------------|--------|-------------|
| Market Status | ~48ms | ~0.01ms | **5700x** |
| Stock List | ~180ms | ~0.02ms | **12000x** |
| Top Gainers | ~52ms | ~0.01ms | **5200x** |

## 📁 Project Structure

```
nepse-data-api/
├── README.md              # Documentation
├── LICENSE                # MIT License
├── setup.py               # Package config
└── nepse_data_api/        # Source code
    ├── __init__.py        # Exports
    ├── market.py          # NEPSE & AsyncNepse classes
    ├── security.py        # Token & Security utilities
    └── version.py         # Version info
```

## 🤝 Contributing

Contributions are welcome!
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Disclaimer & Legal

**FOR EDUCATIONAL PURPOSES ONLY**

This library interfaces with publicly accessible APIs from the **Nepal Stock Exchange (NEPSE)**. It is **not** affiliated with, endorsed by, or connected to NEPSE in any official capacity.

- **Data Attribution:** All data is the property of Nepal Stock Exchange Ltd.
- **No Warranty:** The software is provided "as is", without warranty of any kind.
- **Use Responsibly:** Please respect NEPSE's servers. The built-in caching is designed to prevent abuse; do not disable it unless necessary.
- **Not Financial Advice:** Data retrieved via this library should not be the sole basis for financial decisions.

**License:** MIT License - See [LICENSE](LICENSE) for details.
