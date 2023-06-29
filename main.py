from controllers import TournamentController
from views import TournamentView


def main():
    controller = TournamentController()
    view = TournamentView(controller)

    while True:
        print("1. Create Tournament")
        print("2. Add Player")
        print("3. Generate Matches")
        print("4. Enter Match Results")
        print("5. Display Players")
        print("6. Display Tournaments")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view.create_tournament_prompt()
        elif choice == "2":
            view.add_player_prompt()
        elif choice == "3":
            view.generate_matches()
        elif choice == "4":
            view.enter_match_results_prompt()
        elif choice == "5":
            view.display_players()
        elif choice == "6":
            view.display_tournaments()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
