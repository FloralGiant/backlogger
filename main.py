from pathlib import Path
import json

import gather_data as gd

# Prompt the user for their input
prompt = "\nAdding media to your backlog: "
prompt += "\nBook or Game? "
prompt += "\n(Enter 'quit' when you are finished.)\n"

# The While loop that keeps the program running
while True:
    media_type = input(prompt)

    if media_type.title() == 'Quit':
        break

    elif media_type.title() == 'Book':
        gd.book_info()

    elif media_type.title() == 'Game':
        gd.game_info()
    
    else:
        print("\nPlease enter one of the available options.")

# Query whether they are adding or appending

# Query which media type user is adjusting