
from controllers.app import AppController
from colorama import init

init(autoreset=True)


def main():
    """Start the application via the AppController class."""
    app = AppController()

    app.start()

if __name__ == "__main__":
    main()