from tabulate import tabulate
from colorama import Fore, Style

from datetime import datetime


class RoundView:
    def display_round_menu(self):
        """Display round main menu and return user's choice"""

        while True:
            print("\n----- Round Menu -----\n")
            print("1. " + Fore.BLUE + "Create Round" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "Display Rounds" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Generate Matches" + Style.RESET_ALL)
            print("4. " + Fore.BLUE + "Exit" + Style.RESET_ALL)

            choice = input("\nEnter your choice: ")

            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_round_data(self):
        round_number = int(input("Enter round number: "))
        name = "Round " + str(round_number)
        #start_time = None   
        #end_time = None

        details = {
            "round_number": round_number,
            "name": name,
            #"start_time": start_time,
            #"end_time": end_time,
        }

        return details

    def display_rounds(self, rounds):
        """Display the list of rounds"""
        if not rounds:
            print("No rounds found.")
            return

        headers = ["Round Number", "Name", "Start Time", "End Time"]
        round_data = [
            [
                round.round_number,
                round.name,
                round.start_time,
                round.end_time,
            ]
            for round in rounds
        ]

        print(tabulate(round_data, headers=headers))

    def display_message(self, message):
        print(message)

    def display_matches(self, matches):
        """Display the list of matches"""
        if not matches:
            print("No matches found.")
            return

        headers = [
            "Player 1",
            "Score",
            "Player 2",
            "Rank",
            "Score",
        ]
        match_data = [
            [
                match[0],
                match[1],
                match[2],
                match[3],
                match[4],
            ]
            for match in matches
        ]

        print(tabulate(match_data, headers=headers))


if __name__ == "__main__":
    round_view = RoundView()
    round_view.display_round_menu()
