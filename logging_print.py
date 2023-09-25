import logging

# Configure the logging module
logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def custom_error():
    try:
        raise ValueError("This is a custom error.")
    except ValueError as e:
        logging.error(f"Custom error occurred: {e}", exc_info=True)

def main():
    # Static prints
    print("This is a static print statement.")
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")

    try:
        # Dynamic print with a variable
        x = 10
        print(f"The value of x is: {x}")
        logging.debug(f"The value of x is: {x}")

        # Custom error handling
        custom_error()
    except Exception as e:
        # Catching a general exception
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}", exc_info=True)

    # Loop with dynamic prints
    for i in range(5):
        print(f"Loop iteration {i}")
        logging.debug(f"Loop iteration {i}")

if __name__ == "__main__":
    main()
