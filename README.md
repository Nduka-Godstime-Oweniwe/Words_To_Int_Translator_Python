# Number-to-Words and Words-to-Number Converter

## Project Overview

This project is a Python application that converts numbers into their English word representations and converts number words back into numeric values. It also includes an automated test mode that checks whether both conversion functions work correctly together across a user-specified range.

The application is operated through a simple command-line menu in `main.py`.

## Team Responsibilities

Each team member is responsible for a specific part of the project.

| Person | Team Member | Responsibility | File(s) |
|---|---|---|---|
| Person 1 | **Micah** | Convert numbers into words | `nums_to_words.py` |
| Person 2 | **Lawrence** | Convert words into numbers | `words_to_nums.py` |
| Person 3 | **Ghost** | Validate inputs and build the command-line menu/interface | `validate.py`, `main.py` |
| Person 4 | **Jomiloju** | Build automated round-trip testing | `automate_test.py` |

### 1. Micah — `nums_to_words.py`

Micah is responsible for implementing the `nums_to_words(num)` function.

**Purpose:** Convert a numeric input into its English word representation.

Example:

```python
nums_to_words(25)
# "twenty-five"
```

The function should:
- Convert supported numbers into words.
- Validate the number using `validate.valid_num(num)`.
- Return the agreed invalid-input result when the input is not valid.
- Follow the number range and formatting rules agreed by the team.

### 2. Lawrence — `words_to_nums.py`

Lawrence is responsible for implementing the `words_to_num(words)` function.

**Purpose:** Convert a number written in English words into its numeric value.

Example:

```python
words_to_num("twenty-five")
# 25
```

The function should:
- Convert supported number words into the corresponding number.
- Validate the input using `validate.valid_words(words)`.
- Handle invalid words according to the team's agreed error-handling rules.
- Use the same supported range and word-format conventions as Micah's module.

### 3. Ghost — `validate.py` and `main.py`

Ghost is responsible for validating inputs and building the user-facing command-line interface.

#### `validate.py`

Implement these functions:

```python
def valid_num(num):
    pass

def valid_words(words):
    pass
```

`valid_num(num)` should determine whether a numeric input is acceptable. `valid_words(words)` should determine whether an input contains a valid number written in words.

The team must agree on details such as supported number range, whether zero and negative numbers are allowed, whether decimal values are supported, and which word formats are accepted.

#### `main.py`

`main.py` is the entry point for the application. It should display this menu:

```text
1. Convert Words To Numbers
2. Convert Numbers To Words
3. Automate and test option 1 and option 2
4. Exit

Select an Option:
```

**Option 1 — Convert Words To Numbers**

1. Prompt the user with `Enter Word:`.
2. Pass the entered words to `words_to_nums.words_to_num()`.
3. Display the numeric result or the agreed invalid-input message.
4. Prompt: `Press anything to continue...`
5. Return to the main menu after the user continues.

Example interaction:

```text
Select an Option: 1
Enter Word: twenty-five
25

Press anything to continue...
```

**Option 2 — Convert Numbers To Words**

1. Prompt the user with `Enter Number:`.
2. Pass the entered number to `nums_to_words.nums_to_words()`.
3. Display the result or the agreed invalid-input message.
4. Prompt: `Press anything to continue...`
5. Return to the main menu after the user continues.

Example interaction:

```text
Select an Option: 2
Enter Number: 25
twenty-five

Press anything to continue...
```

The input should be converted to the appropriate Python type where necessary, and invalid input should be handled without crashing the application.

**Option 3 — Automated Testing**

1. Prompt with `Start From:`.
2. Prompt with `Ends From:`.
3. Call `automate_test(start, end)` using the supplied range.
4. Display the test output.
5. When testing finishes, return to the main menu.

Example interaction:

```text
Select an Option: 3
Start From: 1
Ends From: 1000
```

If the user enters an option other than `1`, `2`, or `3`, display:

```text
Invalid Option!
```

Then prompt the user to continue and return to the menu.

**Menu loop and exit behaviour:** The menu should repeat after each operation. An exit option has not yet been specified; the team should agree whether to add `4. Exit` or allow the user to terminate the program with `Ctrl+C`.

### 4. Jomiloju — `automate_test.py`

Jomiloju is responsible for implementing the automated test function:

```python
def automate_test(start, end):
    pass
```

**Purpose:** Check that a number can be converted to words and then converted back to the original number.

For each number in the inclusive range from `start` to `end`, the test should:

1. Convert the number to words using `nums_to_words.nums_to_words(num)`.
2. Pass those words to `words_to_nums.words_to_num(words)`.
3. Compare the result with the original number.
4. If the result differs, record a failure and print a message identifying the number that did not convert correctly.

**Failure rule:**
- For each failed conversion, increase the failure counter.
- If the number of failures is **100 or fewer**, print a message such as `25 didn't convert well`.
- When failures **exceed 100** (the 101st failure), print `too many failures` and stop the automated test immediately.

The test range should include both endpoints. For example, testing from `1` to `1000` means testing every integer from `1` through `1000`.

The automated test is a round-trip check. It verifies that converting a number to words and back returns the original number. It does not, by itself, guarantee that the words are formatted exactly as desired, so direct tests for each conversion function are also useful.

## Project Structure

Keep the files in the same project directory so the modules can import one another:

```text
number_converter/
├── main.py
├── validate.py
├── nums_to_words.py
├── words_to_nums.py
└── automate_test.py
```

Use the exact module and function names agreed by the team. Python imports depend on these names matching.

## How the Modules Work Together

- `main.py` accepts user choices and routes each operation to the appropriate module.
- `nums_to_words.py` converts numeric values into words.
- `words_to_nums.py` converts number words into numeric values.
- `validate.py` provides shared input validation.
- `automate_test.py` checks round-trip conversion between the two conversion modules.

## Shared Decisions to Make Before Implementation

To avoid inconsistent behaviour, the team should agree on:

1. **Supported range:** What is the smallest and largest supported number?
2. **Zero and negatives:** Are zero and negative numbers accepted?
3. **Decimals:** Are decimal numbers supported, or only integers?
4. **Word formatting:** Are variants such as `one hundred five` and `one hundred and five` both accepted?
5. **Capitalization and spacing:** Should inputs such as `Twenty Five` or extra spaces be accepted?
6. **Hyphenation:** Should forms such as `twenty-five` be required, optional, or normalized?
7. **Invalid inputs:** Should conversion functions return a message, return a special value, or raise an exception?
8. **Exit behaviour:** Should the menu include an explicit exit option?

These decisions should be documented and followed by all team members.

## Suggested Workflow

1. Agree on the rules and function interfaces together.
2. Ghost defines the validation behaviour and menu flow.
3. Micah and Lawrence implement the two conversion functions.
4. Jomiloju develops automated tests while the conversion functions are being built.
5. Integrate the modules in the shared project directory.
6. Run small tests first, then increase the test range.
7. Review failures and fix the responsible module.
8. Test invalid inputs and boundary cases as well as ordinary numbers.

## Running the Application

Once the modules have been implemented and saved in the same directory, run:

```bash
python3 main.py
```

Start with a small automated test range, such as `1` through `1000`, before attempting very large ranges. Testing tens or hundreds of millions of values can take a long time because each number requires both conversion functions to run.

## Completion Checklist

- [ ] `nums_to_words.py` converts supported numbers into words.
- [ ] `words_to_nums.py` converts supported number words into numbers.
- [ ] `validate.py` validates numeric and word inputs consistently.
- [ ] `main.py` displays the menu and handles all three options.
- [ ] The program returns to the menu after each operation.
- [ ] Invalid menu choices are handled.
- [ ] `automate_test.py` checks round-trip conversions.
- [ ] Automated testing stops when failures exceed 100.
- [ ] The team has tested boundary cases and invalid inputs.
- [ ] The team has agreed on menu exit behaviour.
