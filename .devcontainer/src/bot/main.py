import os
from telegram.ext import Application
from .handlers import register_handlers
from src.utils.logger import get_logger

logger = get_logger(__name__)

def run_bot():
    try:
        app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
        register_handlers(app)
        logger.info("Starting bot in polling mode...")
        app.run_polling()
    except Exception as e:
        logger.error(f"Bot failed: {str(e)}")
        raise
