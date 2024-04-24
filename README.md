# Pig - Dice Game in Python 🐷
A student project by Merjam Farj-Beibani, Sara Shmerti and Frida Jóhannesson.
Pig is a simple dice game where the goal is to be the first player to reach 100 points. The game is played with one dice and involves strategic decision-making and risk-taking.

## About this project
This is a student project for the course Sustainable development course at the university of Kristianstad. If you want to add to the project please contact @FriddeFrid91 at discord.
## Gameplay
Pig offers the option to play with another player or against the computer. When playing against the computer, you can choose the difficulty level.

## Rules 🎲
- Each player takes turns rolling a single die.
- Points accumulate based on the outcome of the dice rolls.
- After every roll, the player has a choice: they can either save the total points they have gathered and pass the die to the other player, or they can roll the die again.
- If a player rolls a 1, they lose all accumulated points from the current round.

## Intelligence 
"""This class is for the computer move"""
- We have implemented and initilazed the computer player.
- There is a difficulty function, and three functions for each difficulty (easy, medium, hard)
- The easy level, rolls the dice with a round of three times. If the computer gets a 1 it loses all points for that round. When the computer has rolled three times, the computer holds and it is the players turn.
- The medium level, takes a dice of (1, 6) exactly as the easy level, but it doesnt lose any points if the roll is 1.
- The hard level has a Dice of (1, 10) so that it rolls higher numbers, and doesnt lose any pointa if the roll is 1.

## Installation
- Clone this repository to your local machine:
```
git clone https://github.com/FriddeFrid91/Pig_Game.git
```
- Make sure you have Python 3 installed.
```
python --version or python -V
```
- Navigate to the project directory:
```
cd Pig
```
Run the makefile to install dependencies and setup the environment:
```
make install

## Generate documentation

Follow these instructions to generate documentation and UML diagrams.

# Installing venv

- Open Directory in Terminal, write (cd Pig) and press enter
- Continue to write (python3 -m venv .venv) and (make venv)
- No you need to activate the venv, write for Windows (. .venv/Scripts/activate)
- Install the virtual packages in venv. write (make install)
- Check the installed virtual packages (make installed)

# Install the dot command to help generating the UML pictures from source code structure.

- choco install graphviz (Window)
# After virtuel enviroment is opened and graphviz is installed open up rpsg map is necessary in Examination2.

cd Examination2 (if not already opened)
cd src
cd rpsg
Should look something like this in the terminal ~/Examination2/src/rpsg
Step: 4

make pyreverse
And now UML diagram is installed.
```
- Navigate to the game directory:
```
cd Pig/src/Pig_Game
```
Now you're ready to play Pig! Have fun rolling the dice and aiming for that 100-point mark! 🐖

