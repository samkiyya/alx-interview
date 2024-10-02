# Pascal's Triangle

## Description

This project contains tasks for working with Pascal's Triangle, a triangular array of numbers where each number is the sum of the two numbers directly above it. The project is aimed at developing an efficient way to generate Pascal's Triangle for a given number of rows.

## Task Overview

### 0. Pascal's Triangle

[0-pascal_triangle.py](0-pascal_triangle.py) contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal's Triangle of `n` rows:

- If `n <= 0`, the function returns an empty list.
- You can assume `n` will always be an integer.

## Example

For `n = 5`, the function will return:

```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Usage

To use the Pascal's Triangle function:

1. Clone the repository:
   ```bash
   git clone https://github.com/samkiyya/alx-interview.git
   cd alx-interview/0x00-pascal_triangle
   ```
2. Import the function and call it with the desired value of `n`:

   ```python
   from 0-pascal_triangle import pascal_triangle

   print(pascal_triangle(5))
   ```

## Requirements

- The code is written in Python 3.x.
- Make sure Python is installed on your machine to run the code.
