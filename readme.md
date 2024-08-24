# Type Master ⌨️🎢

## Overview 
Type Master is a typing speed game. This game challenges players to type given words as quickly and accurately as possible. This project was created as part of the final checkpoint for the Codédex **'The Legend of Python'** lesson.

## Features 
- **Typing Speed Categories**: The game has three difficulty levels: Easy, Medium, and Hard.
- **Feedback**: After each round, players receive feedback on:
  - Number of mistakes.
  - Time taken.
  - Words per minute (WPM).
  - Typing speed classification (Slow, Average, Decent, Fast).
- **Multiple Rounds**: Each category consists of 2 rounds.
- **User Choices**: After each round, players can choose to:
  - Proceed to the next round.
  - Change the category.
  - Quit the game.

## Typing Speed Classification 
- **Slow Typist**: WPM < 20
- **Average Typist**: 20 <= WPM < 40
- **Decent Typist**: 40 <= WPM < 60
- **Fast Typist**: WPM >= 60

## How to Play 
1. **Choose a Category**: Select from Easy, Medium, or Hard.
2. **Type the Sentences**: Type the displayed sentences as quickly and accurately as possible.
3. **Receive Feedback**: After each round, view your performance metrics.
4. **Make a Choice**: Decide whether to continue to the next round, change the category, or quit the game.

## Installation 
1. **Clone the Repository**:
```sh
   git clone https://github.com/ZainabAlashoor/Type-Master.git
```
2. Install Required Packages:
```python
   pip install pyfiglet
```

## Running the Game 
Run the `type_game.py` script to start the game.
```python
   python type_game.py
```

## Improvments 
- **Add More Categories**: Include additional difficulty levels or special categories.
- **Improve User Interface**: Enhance the game's visual appeal and user experience using a GUI library like Tkinter or PyQt. For example: show wrong words in red, prevent users from deleting what they have wrote. 
- **Add Leaderboard**: Store and display player performance metrics (e.g., highest WPM)
- **Multiplayer**: Allow multiple players to compete against each other.
- **Practice Mode**: Allow players to practice typing without the pressure of a timer.


*That's all, enjoy! 🌷*