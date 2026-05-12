from loguru import logger

logger.add("logs/app.log", level="INFO", rotation="1 day", retention="7 days")
