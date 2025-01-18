# Quiz Game in Python

This project is a simple Python-based quiz game where users can test their knowledge by answering multiple-choice questions. The game keeps track of the score and calculates the final percentage at the end.

---

## Features

- **Multiple Choice Questions**: Each question has four answer options (A, B, C, D).
- **Dynamic Feedback**: Users are informed if their answer is correct or incorrect.
- **Score Tracking**: The game keeps track of the user's score as they progress.
- **Percentage Calculation**: At the end of the quiz, the user is shown their final score and percentage.

---

## How It Works

1. The program presents a series of questions with multiple-choice answers.
2. The user selects their answer by typing `A`, `B`, `C`, or `D`.
3. The program checks the user's answer against the correct answer and provides immediate feedback.
4. At the end of the quiz, the program displays the total score and percentage.

---

## Code Structure

### **question_bank**
A list of dictionaries where each dictionary contains:
- `text`: The question text.
- `Answer`: The correct answer (e.g., `"A"`).

### **option**
A list of lists, where each sublist contains the answer options for the corresponding question.

### **Functions**
- **`check_answer(user_guess, correct_answer)`**: Compares the user's guess with the correct answer and returns `True` if they match, or `False` otherwise.

### **Main Logic**
The program loops through all questions in the `question_bank`, displaying the question and answer options. It prompts the user for their answer, checks if it's correct, and updates the score. Finally, it displays the total score and percentage.

---

## How to Run

1. Clone the repository or download the script.
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Run the Python script:
   ```bash
   python quiz_game.py
   ```

---

## Example Usage

### Sample Question Output:
```plaintext
###**************************************###
The ability of one class to acquire the methods and attributes of another class is called________
A.inheritances
B.Abstration
C.polymorphism
D.object
Enter your choice A/B/C/D:
```

### Correct Answer Feedback:
```plaintext
Correct Answer
1/1
```

### Incorrect Answer Feedback:
```plaintext
Incorrect Answer
The correct answer is A
```

### Final Score Output:
```plaintext
The final score is = 3, In percentage = 60.0%
```

---

## Customization

### Adding Questions:
To add new questions:
1. Update the `question_bank` list with new questions and their correct answers.
2. Add corresponding answer options to the `option` list.

Example:
```python
question_bank.append({"text": "New question here", "Answer": "B"})
option.append(["A.Option1", "B.Option2", "C.Option3", "D.Option4"])
```

---

## Dependencies
- Python 3.6 or higher

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bugs.

---

## Contact
For questions or feedback, please contact Shajan J Jacob (mailto:shajanjjacob369gmail.com).

