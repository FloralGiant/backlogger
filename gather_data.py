from pathlib import Path
import json

# Empty dictionaries to hold backlog data for media types
books = {}
games = {}

# Gather book name and status from user input
def book_info():
    books['name'] = input("What is the book's title? ")
    books['status'] = input("Is the book read or unread? ")

    print(f"{books['name'].title()} has been added as {books['status'].title()}.")

    # Write the backlog book data to a json file
    path = Path('book_backlog.json')
    contents = json.dumps(books)
    path.write_text(contents)

# Gather game name and status from user input
def game_info():
    games['name'] = input("What is the game's title? ")
    games['status'] = input("Is the game completed or uncompleted? ")

    print(f"{games['name'].title()} has been added as {games['status'].title()}.")

    # Write the backlog game data to a json file
    path = Path('game_backlog.json')
    contents = json.dumps(games)
    path.write_text(contents)