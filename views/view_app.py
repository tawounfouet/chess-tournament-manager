from colorama import Fore, Style

class ViewApp:

    def display_main_menu(self):
        """Display the main menu and return the user's choice."""
        
        while True:
            print(Fore.GREEN + "\nWelcome to the Chess Tournament Manager\n".center(120, "-"))
            print(Fore.YELLOW + "\n1. Tournament menu")
            print("2. Player menu")
            print("3. Round menu")
            print("4. Quit")
            print(Style.RESET_ALL)

            choice = input(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL)

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print(Fore.RED + "Goodbye!")
                    print(Style.RESET_ALL)
                return choice
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
                print(Style.RESET_ALL)
                print()
                continue
