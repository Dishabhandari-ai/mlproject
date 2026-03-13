import logging
import os
from datetime import datetime

# Create log file name using current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create logs folder if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

LOG_FILE_PATH = logs_path

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
