# Testbook Telegram Extractor Bot

This Telegram bot allows users to log in via OTP, fetch paid Testbook test series, and sends HTML-formatted tests with Submit and Analysis options.

## Features

- OTP-based login
- Extract test questions from paid test series
- Telegram HTML message + external Flask rendering
- Works on Render or local deployment

## Deployment

1. Add `BOT_TOKEN` to `config.py`
2. Run `bot.py` for the Telegram bot
3. Deploy `server/flask_app.py` for full HTML view

## Note

This bot scrapes Testbook content — use only for educational or personal purposes.
