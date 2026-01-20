## Project Title
Rio de Janeiro Multiple-Choice Quiz (Python)

## Project Overview
This is a console-based quiz application about Rio de Janeiro. The program selects random questions, shuffles answer options, validates user input, calculates a final score and percentage, and allows replay. An optional review of incorrect answers is shown when feedback is set to “end only”.

## Features
- Random selection of questions (no duplicates per session)
- Shuffled answer options (A–D) for each question
- Input validation (prevents crashes on invalid input)
- Two feedback modes:
  - A: instant feedback after each question
  - B: feedback only at the end (+ optional review)
- Final score + percentage
- Play again option

## Requirements
- Python 3.x
- No external libraries required (uses `random` only)

## How to Run
1. Download or clone the repository
2. Open a terminal in the project folder
3. Run:

```bash
python quiz.py

How to Use (Program Flow)
Enter your name (or press Enter for "Player")

Choose feedback mode (A or B)

Choose how many questions you want to answer

Answer each question using A/B/C/D

View your final results

Choose whether to play again

File List
quiz.py — main Python quiz program

README.md — project information and run instructions

Notes / Limitations
Questions are stored directly in the source code (not loaded from a file)

The quiz runs in the terminal (no GUI)

Author
Caua de Araujo Ferreira (2402220)