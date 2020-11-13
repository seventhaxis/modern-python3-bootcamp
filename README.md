# Personal Notes

[![](https://img.shields.io/badge/Modern%20Python%203%20Bootcamp-2020-DA5D58?logo=udemy)](https://www.udemy.com/course/the-modern-python3-bootcamp/) [![](https://img.shields.io/badge/Python-3.8.5-4473A4?logo=python)](#)

#### Table of Contents
1. [Operators](#operators)
2. [Variables & Data Types](#variables--data-types)
3. [Booleans & Conditional Logic](#booleans--conditional-logic)
1. [Built-In Functions](#built-in-functions)

- [Links & Acknowledgements](#links--acknowledgements)

---

## Operators
- the divide operator(`/`) **always** returns a `Float`
    - use the integer division operator (`//`) instead to discard any fractional component and return and `Int` instead, rounding down
- the exponentiation operator (`**`) raises a number to a given power
- the modulo operator (`%`) returns the **remainder** of the equation

## Variables & Data Types
- most variables are defined with lowercase `snake_case` names
    - constants would be `ALL_CAPS`
    - objects (classes) use `PascalCase`
    - variables beginning and ending with two (2) underscores (aka. **dunder**) are considered private and should be ignored
        - `__no_touchy__`
- variables can change stored data types (i.e. **Dynamic Typing**)
- boolean values must begin with capital **T** or **F**
- includes a special type defined as `None` (i.e. `nil`, `NULL`)
- strings can be defined with either single or double quotes
    - escape sequences defined within [**documentation**](https://docs.python.org/3/reference/lexical_analysis.html)
- string interpolation utilizes **F-Strings** (introduced in Python 3.6)
```python
x = 42
print(f"The answer to the question is {x}!")   # The answer to the question is 42!
```
- strings represent lists of characters which can be accessed by calling its index within the string
    - lists (arrays) start at zero within Python
    - negative indices can be used and start at the _end_ of the list

## Booleans & Conditional Logic
- the `elif` keyword allows you to check an alternative expression
- colons are required at the end of each expression
```python
if expressionA:
    print("Congratulations!")
elif expressionB:
    print("Nice job.")
else:
    print("Maybe next time?")
```
- certain objects have an inherent **truth value** (aka. _truthiness_) associated with the value
    - *truthiness* refers to an expression that resolves as `True`
    - the following constants and objects resolve as `False`:
        - empty sequences and collections (e.g. `""`, `()`, `[]`)
        - zero for any numeric type (e.g. `0`, `0.0`)
        - `False`, `None`
- comparison operator `is` refers to whether an object shares the same place with another **in memory**

## Common Built-In Functions
See the full list within the [documentation](https://docs.python.org/3/library/functions.html).<br>
**Important:** Take care not to override these defined functions.

- `input()` - prompts the user with given message and returns the user response


---

## Links & Acknowledgements
- [Modern Python 3 Bootcamp](https://www.udemy.com/course/the-modern-python3-bootcamp/) (via **Udemy**)
