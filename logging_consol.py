import logging

# Configure the logging module to display logs in the console
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to control what is displayed
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    # Static prints
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")

    try:
        # Dynamic print with a variable
        x = 10
        logging.debug(f"The value of x is: {x}")
    except Exception as e:
        # Catching a general exception
        logging.error(f"An error occurred: {e}", exc_info=True)

    # Loop with dynamic prints
    for i in range(5):
        logging.debug(f"Loop iteration {i}")

if __name__ == "__main__":
    main()
