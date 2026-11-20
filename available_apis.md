# 📡 Available APIs

A flat list of every method available in `nepse-data-api`. All sync methods live on `Nepse`, async on `AsyncNepse`.

| # | Method | Parameters | Description |
|---|--------|-----------|-------------|
| 1 | `get_market_status()` | `use_cache=True` | Whether the market is currently open or closed |
| 2 | `get_market_summary()` | `use_cache=True` | Total turnover, transactions, and market summary for the day |
| 3 | `get_nepse_index()` | `use_cache=True` | Live NEPSE main index value |
| 4 | `get_sub_indices()` | `use_cache=True` | Live sector sub-indices (Banking, Hydro, Finance, etc.) |
| 5 | `get_all_indices()` | `use_cache=True` | All market indices in a single call |
| 6 | `get_index_history()` | `index`, `start_date`, `end_date`, `size`, `limit`, `use_cache` | Historical OHLCV data for any index. `index` can be a name (`"Banking"`), ID (`51`), or `"all"` |
| 7 | `get_stocks()` | `date=None`, `use_cache=True` | Live stock prices for all listed companies. Pass `date="YYYY-MM-DD"` for historical data |
| 8 | `get_today_price()` | `size=500`, `date=None`, `use_cache=True` | Raw OHLCV price data for all companies. Historical with `date` param |
| 9 | `get_security_details()` | `security_id` (int), `use_cache=True` | Full details for a single security — market cap, listed shares, sector, etc. |
| 10 | `get_historical_chart()` | `security_id` (int), `start_date`, `end_date`, `use_cache` | OHLCV chart data for a company or the NEPSE index |
| 11 | `get_top_gainers()` | `limit=None`, `use_cache=True` | Stocks with the highest % gain today |
| 12 | `get_top_losers()` | `limit=None`, `use_cache=True` | Stocks with the highest % loss today |
| 13 | `get_top_turnover()` | `use_cache=True` | Top 10 stocks by turnover value |
| 14 | `get_top_trade()` | `use_cache=True` | Top 10 stocks by number of trades |
| 15 | `get_top_transaction()` | `use_cache=True` | Top 10 stocks by number of transactions |
| 16 | `get_market_depth()` | `symbol` (str) | Live order book (buy/sell depth) for a specific stock |
| 17 | `get_floorsheet()` | `symbol=None`, `date=None`, `size=500`, `limit=None`, `page=0` | Transaction records (floorsheet) for the latest session. Filter by stock symbol |
| 18 | `get_daily_trade()` | `date` (str `YYYY-MM-DD`), `size=500`, `use_cache=True` | All trade statistics for a specific business date |
| 19 | `get_marcapbydate()` | `date=None`, `use_cache=True` | Market cap, sensitive market cap, float market cap. Defaults to latest |
| 20 | `get_company_list()` | `use_cache=True` | Full list of all companies listed on NEPSE |
| 21 | `get_security_list()` | `use_cache=True` | Full list of all non-delisted securities |
| 22 | `get_promoter_list()` | `use_cache=True` | List of all promoter securities (paginated internally) |
| 23 | `get_company_news()` | `symbol` (str), `use_cache=True` | Latest news articles for a specific company |
| 24 | `get_news_alerts()` | `use_cache=True` | General NEPSE market news and alerts |
| 25 | `get_press_releases()` | `use_cache=True` | Official NEPSE press releases |
| 26 | `get_dividends()` / `get_dividend()` | `symbol` (str), `use_cache=True` | Official dividend declaration notices, AGM dates, book closure dates, agendas, and filing PDFs |
| 27 | `get_agm()` | `symbol` (str), `use_cache=True` | AGM announcements for a specific company |
| 28 | `get_holiday_list()` | `year=2025`, `use_cache=True` | Market holidays for a given year |
| 29 | `get_sector_list()` | `use_cache=True` | Complete list of all NEPSE market sectors |
| 30 | `get_price_volume()` | `use_cache=True` | Daily price and volume stats for all securities |
| 31 | `clear_cache()` | — | Clears all in-memory cached data |
| 32 | `get_dividend_history()` / `get_corporate_actions()` | `symbol` (str), `use_cache=True` | Structured per-fiscal-year dividend breakdown — bonus shares %, cash dividend %, right shares % |
| 33 | `get_financial_reports()` | `symbol` (str), `use_cache=True` | Quarterly and annual financial reports with EPS, PE, net worth per share, profit, paid-up capital |
| 34 | `get_broker_trades()` | `broker_id` (int), `size=500`, `limit=None`, `page=0` | Today's floorsheet trades filtered by broker number (buyer + seller side) |
| 35 | `get_stock_ohlcv()` | `symbol` (str), `page=1`, `size=500`, `date=None`, `use_cache=True` | Per-security datewise OHLCV price history (open, high, low, close, volume, avg price) |
| 36 | `get_security_profile()` | `symbol` (str), `use_cache=True` | Company profile — address, contacts, sector, description |
| 37 | `get_board_of_directors()` | `symbol` (str), `use_cache=True` | Board of directors list for a company |

> **Note:** `symbol` parameters accept stock tickers like `"NABIL"`, `"NLIC"`, etc. Date strings are `YYYY-MM-DD` unless noted otherwise.

---

← Back to [README](README.md)

