
class ViewTournament:
    
    def display_tournament_menu(self):
        """Display the tournament menu and return the user's choice."""
        
        while True:
            print("Tournament Menu".center(80, "-"))
            print("1. Create new tournament")
            # charger un tournoi
            print("2. Load a tournament")
            # Affciher les tournois par date
            print("3. List tournaments by date")
            # consulter la liste des rounds d'un tournoi
            print("4. List rounds of a tournament")
            # Consulter les matchs d'un round
            print("5. List pairings of a round")
            # add player to tournament
            print("6. Add player to tournament")
            # retourner au menu principal
            print("7. Back to main menu")
            
            choice = input("Enter your choice: ")

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                return choice
            else:
                print("Invalid choice. Please try again.")
                print()
                continue