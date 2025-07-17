#!/bin/bash

# Start services
python src/services/health_api.py &
python src/services/keepalive.py &

# Start main bot
python -m src.bot.main
