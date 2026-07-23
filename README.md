# 🎯 Number Guessing Game (Python)

A simple and interactive **Number Guessing Game** built using Python. The program generates a random number between **1 and 100**, and the player has **3 attempts** to guess it correctly.

## 📌 Features

* 🎲 Random number generation between 1 and 100
* 🔢 Three guessing attempts
* 📈 Smart hints after every incorrect guess:

  * **High** – Guess is higher than the secret number but within 10.
  * **Too High** – Guess is much higher than the secret number.
  * **Low** – Guess is lower than the secret number but within 10.
  * **Too Low** – Guess is much lower than the secret number.
* 🎉 Congratulates the player when the correct number is guessed.
* ❌ Displays the correct number if all three attempts are used.

## 🛠️ Technologies Used

* Python 3
* `random` module
* `sys` module (used to end the game after a correct guess)

## 📂 Project Structure

```text
Number-Guessing-Game/
│── number_guessing_game.py
│── README.md
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

3. Open the project folder:

```bash
cd Number-Guessing-Game
```

4. Run the program:

```bash
python number_guessing_game.py
```

## 🎮 Sample Gameplay

```text
================== Number Guessing Game ==================
Guess the number between 1 to 100
You have 3 attempts.

Enter your number: 45
Low

Enter your number: 52
High

Enter your number: 50
Congratulations! You guessed the right number.
```

## 📚 Concepts Practiced

* Variables
* User Input
* Conditional Statements (`if`, `else`)
* Nested Conditions
* Random Number Generation
* Basic Game Logic
* Python Modules

## 🚀 Future Improvements

* Add difficulty levels (Easy, Medium, Hard)
* Let the user choose the number of attempts
* Display a score based on remaining attempts
* Add a "Play Again" option
* Use colors in the terminal with the `colorama` library
* Store high scores in a file

## 👨‍💻 Author

**Harsh Kumar**

GitHub: https://github.com/harshkumar939392-tech

---

⭐ If you like this project, consider giving the repository a star!
