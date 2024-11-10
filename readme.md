# THE X-O Game
#### Video Demo: [https://youtu.be/wjhAN60FYqE](https://youtu.be/wjhAN60FYqE)

#### Description:
This project recreates the classic Tic-Tac-Toe game with a modern twist by providing both single-player and multiplayer options. The game can be enjoyed solo, playing against an AI opponent, or as a duo, where two players can go head-to-head. What’s more, players have the ability to save their games mid-way and resume them later, allowing them to revisit the fun anytime.

The project uses a combination of multiple libraries and tools, taking a highly technical approach to developing this simple yet iconic game. This technical depth adds complexity and a unique charm to a seemingly straightforward game. Below, you’ll find a detailed breakdown of each component, an overview of the game’s functionalities, and insights into the design choices behind this modern version of Tic-Tac-Toe.

### Project Structure
The project consists of the following key files:

1. **ai.py**
   - This file is responsible for the AI functionality in single-player mode. It contains the logic for the AI’s moves, designed to offer a competitive challenge to the player. The AI uses a basic algorithm to assess the current state of the board and make an optimal move, attempting to either win or block the player’s potential winning moves.
   - Within this file, there are functions that analyze each possible move on the grid, checking for opportunities to align three marks in a row, column, or diagonal. This ensures that the AI remains a fair but formidable opponent.

2. **game.db**
   - The `game.db` file serves as the database to store game data, allowing for the save and load functionality of ongoing matches. It is a SQLite database file that keeps track of current board states, players, and match progress for each game session.
   - The database structure has tables that log important game data like player moves, game states, and timestamps. This allows players to save their game mid-way and resume it later, making the game experience flexible and user-friendly.
   - The integration of a database into a simple game such as Tic-Tac-Toe is an innovative approach, adding a unique layer to the project by offering persistence of game states.

3. **x-o_game.py**
   - This file contains the main game logic and the user interface for the Tic-Tac-Toe game. It ties together both the single-player AI mode (via the `ai.py` file) and the two-player mode.
   - The file includes:
     - **User Interface Functions:** These functions handle displaying the game board, managing input, and visualizing each player’s move.
     - **Game Mechanics Functions:** Functions that verify the win conditions and check for a draw are present in this file. These ensure that once three marks align in a row, column, or diagonal, the game recognizes a winner or declares a draw.
     - **Save and Load Functions:** These functions interface with the `game.db` file to allow saving and loading games. The save functionality records the current board state in the database, while the load functionality retrieves saved states, enabling players to continue where they left off.
   - The file is the core of the game, orchestrating interactions between the game’s interface, AI, and database for a seamless experience.

### Functionality and Features
This Tic-Tac-Toe game offers several features that make it stand out:
- **Single-Player Mode with AI:** The AI opponent provides a challenge to players looking for solo play. Using programmed strategies, the AI aims to compete by recognizing potential wins or blocking the player’s moves.
- **Two-Player Mode:** Two players can enjoy a classic game of Tic-Tac-Toe, with each taking turns to mark the board.
- **Save and Resume Game:** With an embedded database, players can save their game mid-way and return to finish it later. This functionality is accessible in two-player mode and allows for a dynamic and flexible play style.
- **Accessible Saved Games:** Players can load any saved game from the database, picking up their competition at any time.

### Design Choices
Several unique design choices were made to elevate the simplicity of Tic-Tac-Toe:
- **AI Integration:** The AI in `ai.py` enhances the single-player experience, making the game not only a fun challenge but also a test of strategic thinking. The AI’s logic is crafted to prevent the player from winning easily, adding replay value.
- **Database for Game State Management:** Adding `game.db` allows for persistent data storage, which is uncommon in most basic implementations of Tic-Tac-Toe. This choice was made to add a new layer to the game, making it possible for players to pick up right where they left off. Using SQLite keeps the setup lightweight while achieving the desired functionality.
- **Modular Design:** Separating the core game logic (`x-o_game.py`), AI (`ai.py`), and data management (`game.db`) into different files ensures the project is modular, organized, and scalable. This design approach makes it easy to modify or upgrade specific components in the future.

### Future Enhancements
There are several potential directions for enhancing this project further:
- **Advanced AI:** Future iterations could implement a more complex AI using the minimax algorithm, making it even more challenging for the player.
- **Online Multiplayer Mode:** Implementing an online multiplayer mode could allow players from different locations to play against each other.
- **Enhanced UI:** Adding a graphical user interface (GUI) using a library such as Tkinter or Pygame could make the game more visually appealing and interactive.
- **Statistics and Leaderboards:** Implementing a leaderboard or basic player statistics (e.g., win/loss ratio) would add a competitive edge to the game.

This project offers a unique and engaging way to experience the timeless Tic-Tac-Toe game, blending simple gameplay with sophisticated technical elements. Through single-player AI, multiplayer options, and save/load capabilities, this Tic-Tac-Toe project brings a fresh, dynamic perspective to an old favorite.
