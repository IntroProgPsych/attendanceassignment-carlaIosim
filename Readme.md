# Introduction to Programming (Psychology) — Make-Up Lab Assignment

This repository contains a short Python assignment designed for students who **do not have enough lab attendance** and need to **recover lab presences** by completing and submitting a set of programming exercises.

## Deadline and submission

* **Deadline:** **24.01.2025 (24 January 2025)**
* **How to submit:** Complete all exercises and **push your solutions to this GitHub Classroom repository** (your assigned repo). Your submission is the latest commit pushed before the deadline.

---

## Exercises

### EX01 — Input & Type Casting (`ex01_input_casting.py`)

**Requirement:**
Ask the user for two values: `age` (integer) and `hours_slept` (float).
Print:

1. the user’s age next year
2. whether `hours_slept` is at least `8.0` (`True/False`)

---

### EX02 — Variables (`ex02_variables.py`)

**Requirement:**
Create variables `first_name` (string), `last_name` (string), and `year_of_birth` (integer).
Compute approximate age as `2026 - year_of_birth` and print a greeting:

`Hello, <first_name> <last_name>. You are about <age> years old.`

---

### EX03 — Collections (list + dict) (`ex03_collections.py`)

**Requirement:**
Ask the user to enter **5 integers** separated by spaces (example: `"3 1 3 5 1"`).

* Store them in a list called `numbers`.
* Build a dictionary called `counts` where each key is a number from the list and each value is **how many times that number appears**.
* Print:

  1. the list on the first line
  2. the dictionary on the second line

---

### EX04 — Conditionals (`ex04_conditionals.py`)

**Requirement:**
Ask the user for an integer `score` from `0` to `100`. Print:

* `"fail"` for `< 50`
* `"pass"` for `50–79`
* `"excellent"` for `80–100`
* `"invalid"` otherwise (outside `0–100`)

---

### EX05 — Loops (`ex05_loops.py`)

**Requirement:**
Ask the user for an integer `n`.
Using a loop, print all **even numbers** from `0` to `n` (inclusive), each on a new line.

---

### EX06 — Functions (`ex06_functions.py`)

**Requirement:**
Write a function `clamp_rating(x)` that returns:

* `1` if `x < 1`
* `5` if `x > 5`
* otherwise `x`

Then:

* read one integer from input
* apply `clamp_rating`
* print the result

---

## What is evaluated

* Correct use of the required concept in each file (input/type casting, variables, collections, functions, conditionals, loops).
* Correct output behavior for valid inputs.
* Code clarity (reasonable naming, readable structure).

## Academic integrity

Submit your own work. You may review course materials and examples, but the final code must be written and understood by you.

