# FizzBuzz Number Game

## Overview

The FizzBuzz Number Game is a Python program based on a popular coding challenge commonly used in programming interviews and beginner exercises. The program iterates through a sequence of numbers and applies specific rules based on divisibility.

## Features

* Accepts a maximum number from the user.
* Generates a sequence from 1 to the specified number.
* Prints:

  * `"Fizz"` for multiples of 5.
  * `"Buzz"` for multiples of 7.
  * `"FizzBuzz"` for numbers divisible by both 5 and 7.
* Displays regular numbers when no conditions are met.

## Technologies Used

* Python 3

## Project Structure

```text
FizzBuzz-Game/
│
├── fizzbuzz.py
└── README.md
```

## How to Run

1. Ensure Python 3 is installed.
2. Save the program as `fizzbuzz.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python fizzbuzz.py
```

## Example

### Input

```text
Welcome to FizzBuzz game!
How many number do you want to play? 15
```

### Output

```text
1
2
3
4
Fizz
6
Buzz
8
9
Fizz
11
12
13
Buzz
Fizz
```

## How It Works

1. The program displays a welcome message.
2. The user enters the maximum number for the game.
3. A list is created containing numbers from `1` to the specified limit.
4. The program iterates through each number in the list.
5. For every number:

   * If it is divisible by both `5` and `7`, print `"FizzBuzz"`.
   * If it is divisible only by `5`, print `"Fizz"`.
   * If it is divisible only by `7`, print `"Buzz"`.
   * Otherwise, print the number itself.
6. Once all numbers have been processed, the program displays a closing message.

## Divisibility Rules

| Condition            | Output   |
| -------------------- | -------- |
| Divisible by 5       | Fizz     |
| Divisible by 7       | Buzz     |
| Divisible by 5 and 7 | FizzBuzz |
| Otherwise            | Number   |

### Example for Numbers 1–35

| Number | Output   |
| -----: | -------- |
|      5 | Fizz     |
|      7 | Buzz     |
|     10 | Fizz     |
|     14 | Buzz     |
|     35 | FizzBuzz |

## Concepts Demonstrated

* `for` loops
* Lists
* Conditional statements
* Modulus operator (`%`)
* User input
* Sequence generation
* Algorithmic thinking

## Known Improvement

The program currently creates an additional list before processing:

```python
number = []
for numbers in range(1, ans + 1):
    number.append(numbers)
```

This step can be simplified by iterating directly over the `range()` object:

```python
for digit in range(1, ans + 1):
    # Process each number
```

This approach is more memory-efficient and aligns with common Python best practices.

## Future Improvements

* Allow users to customize the divisors instead of using 5 and 7.
* Add score tracking and levels.
* Create a graphical user interface (GUI).
* Highlight special outputs using colors in the terminal.
* Support replay functionality without restarting the program.

## Author

Created as a Python practice project to demonstrate loops, conditional logic, and the classic FizzBuzz algorithm.
