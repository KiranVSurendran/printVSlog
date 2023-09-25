import logging
from colorlog import ColoredFormatter

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level to INFO or higher

# Create a console handler and set the log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the console handler's level to INFO or higher

# Create a colored formatter
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(log_color)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

# Set the formatter for the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

def main():
    # Static prints
    logger.warning("This is a debug message.")
    logger.info("This is an info message.")

    try:
        # Dynamic print with a variable
        x = 10/0
        logger.debug(f"The value of x is: {x}")
    except Exception as e:
        # Catching a general exception
        logger.critical(f"An error occurred: {e}", exc_info=True)

    # Loop with dynamic prints
    for i in range(5):
        logger.debug(f"Loop iteration {i}")

if __name__ == "__main__":
    main()
