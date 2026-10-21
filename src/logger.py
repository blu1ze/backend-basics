import logging

# Print messages of level INFO and above (INFO, WARNING, ERROR)
logging.basicConfig(level=logging.INFO)

# One named logger for the whole task service
logger = logging.getLogger("tasks")
