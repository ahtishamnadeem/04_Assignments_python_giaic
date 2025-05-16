class Logger:
    def __init__(self):
        print("📥 Logger created! Ready to track everything.")

    def __del__(self):
        print("📤 Logger destroyed! Shutting down the log.")

# Example usage
def create_logger():
    log = Logger()

create_logger()

# Logger will be destroyed automatically when it goes out of scope
