class ViewPlayer:

    def display_player_menu(self):
        """Display the player menu and return user choice."""
        
        while True:
            print("Player Menu".center(80, "-"))
            print("1. Create new player")
            print("2. Modify player")
            print("3. List players by name")
            print("4. List players by rank")
            print("5. Back to main menu")
            
            choice = input("Enter your choice: ")
            
            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("Invalid choice. Please try again.")
                print()
                continue