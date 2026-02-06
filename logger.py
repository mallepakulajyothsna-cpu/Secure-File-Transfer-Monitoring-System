import logging
from config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_event(message):
    logging.info(message)

def alert(message):
    logging.warning("ALERT: " + message)
    print("⚠️ ALERT:", message)
