# PythonAssessment

A Python coursework project developed for university programming studies at UTS. This project is a card/deck-based program that demonstrates foundational object-oriented programming skills, modular code organisation, and basic game logic.

## Overview

PythonAssessment is built around a card game structure. The program separates the main parts of a card-based system into different Python files, including cards, decks, players, dealers, and supporting style or display logic.
The purpose of the project was to practise designing a program using classes rather than writing all code in one file. Each file has a specific role in the overall program, which helped me better understand how larger Python programs can be organised and maintained.
Unlike a basic script that only runs a single task, this project models multiple interacting objects. For example, a deck can contain cards, a player can receive or manage cards, and a dealer can control parts of the game flow. This helped me understand how object-oriented programming can be used to represent real parts of a system.

## What the Program Does

The program models the core logic for a card-based application. It includes:

* Card objects that represent individual cards
* A deck structure for storing and managing cards
* Player logic for representing users in the game
* Dealer logic for managing game actions
* A card library for storing or accessing available card information
* Supporting files for additional behaviour or presentation
* A modular structure where each file has a clear responsibility

The project focuses mainly on the backend logic of a card game rather than a full graphical interface like PythonScaffold. However, it helped me understand how data and behaviour can be organised before being connected to a user interface.

## Main Components

### card.py

Defines the structure of an individual card. This file is responsible for representing card information and any behaviours linked to a single card.

### card_library.py

Stores or manages card-related information used throughout the program. This supports the rest of the project by providing access to the available cards or card data.

### deck.py

Represents the deck of cards. This file is responsible for organising cards and may include behaviours such as creating, storing, drawing, or managing cards.

### player.py

Represents a player in the card system. This file helps manage player-related information and interactions, such as holding cards or participating in game actions.

### dealer.py

Represents the dealer or controller role within the project. This file helps manage the flow of the card system and connects different parts of the program together.

### weapon_style.py

Provides additional supporting logic or styling related to the program. This file helps extend the card system beyond the basic card, deck, player, and dealer structure.

## Technologies Used

* Python (oh fr)

## What I Learned

This project helped me improve my understanding of object-oriented programming in Python. I learned how classes can be used to represent different parts of a program, such as cards, decks, players, and dealers. This made the project easier to organise because each class had a clearer purpose.

I also learned the importance of separating code into different files. Instead of placing all logic into one large script, the project uses multiple files so that each part of the program can focus on a specific responsibility. This improved my understanding of modular programming and made the code easier to read and manage.

Another important lesson was understanding how different objects interact with each other. For example, a player may rely on card objects, while the dealer may interact with both the deck and the player. This helped me understand how object-oriented programs can model relationships between different parts of a system.

Uploading this project to GitHub also helped me begin using version control and project documentation as part of my software development workflow. It gave me practice presenting coursework in a way that can be understood by others, rather than only submitting code for assessment.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or another Python IDE.
3. Make sure Python is installed.
4. Run the main file used to start the program.

```bash
python dealer.py
```

Note: The correct starting file may depend on the final version of the assessment. If `dealer.py` is not the intended entry point, run the file that contains the main program logic.

## Future Improvements

* Add clearer instructions on the correct file to run
* Add example input and output
* Add comments explaining important methods and classes
* Add screenshots or terminal output examples
* Add unit tests for card, deck, player, and dealer behaviour
* Add a `.gitignore` file to remove unnecessary generated files such as `__pycache__`
* Use Github to document my changes

## Author

Adrian Dwyer
Bachelor of Computer Science (Honours)
University of Technology Sydney
