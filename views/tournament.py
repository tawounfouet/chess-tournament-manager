class TournamentView:
    """Tournament view class"""

    def display_tournament_menu(self):
        """Display tournament main menu and return user's choice"""

        while True:
            print("\n----- Tournament Menu -----\n")
            print("1. Create Tournament")
            print("2. Display Tournaments")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_tournament_info(self):
        """Get tournament information from user"""

        print("\nEnter Tournament Information:")
        name = input("Name: ")
        location = input("Location: ")
        date = input("Date: ")

        return {"name": name, "location": location, "date": date}

    def display_tournaments(self, tournaments):
        """Display a list of tournaments"""

        print("\nTournaments:")
        for tournament in tournaments:
            print(f"Name: {tournament.name}")
            print(f"Location: {tournament.location}")
            print(f"Date: {tournament.date}")
            print("-------------------------------")
