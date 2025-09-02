# Trading Bot

A cryptocurrency trading bot with backtesting, paper trading, and live trading modes.

## Features
- Fetches live and historical data from Binance
- Feature engineering for trend detection
- Risk management module
- Backtesting and paper trading
- Live trading with Binance API

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/trading-bot.git
   cd trading-bot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # (Linux/Mac)
   venv\Scripts\activate     # (Windows)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` → `.env` and insert your Binance API keys.

5. Run the bot:
   ```bash
   python src/main.py
   ```
