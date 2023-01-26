# Credit Card Fraud Detection With Machine Learning
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KhaingSuThway/Credit-card-fraud-detection-with-machine-learning/main)

In this repo, the common cause and trace of credit card fraud are analyzed by  distinguishing transaction scenarios and predicted by following the state-of-the-art AI approaches. 

## File Definitions

## Setting Up The Development Environment
* Create a Python virtual environment
```
$ python -m venv .venv
```
* Activate the virtual environment (For Windows)
```
$ .\.venv\Scripts\activate
```
* Install packages required for production code
```
pip install -r requirements.txt
```
* Install packages required for development code (optional)
```
pip install -r requirements_dev.txt
```

## Coding Standards
All the codes written must follow PEP 8 - Stype Guide for Python Code - https://peps.python.org/pep-0008/

### Type Hinting
1. Every functions must have type hinting. For example,
* Good
```python
class MyClass:
    
    def __init__(self):
        # your code here
        pass

def func(text: str, number: float)->MyClass:
    return MyClass(text, number)
```
* Bad
```python
def func(text, number):
    return MyClass(text, number)
```
2. Every class and functions must contain document strings for briefly explaining the purpose.
* Good
```python
class MyClass:

    def __init__(self, param1: str, param2: int):
        """_summary_

        Args:
            param1 (str): _description_
            param2 (int): _description_
        """
        pass

    def func(self, foo: float, baz: list)->None:
        """_summary_

        Args:
            foo (float): _description_
            baz (list): _description_
        """
        pass

```
* Bad
```python
class MyClass:

    def __init__(self, param1, param2):
        pass

    def func(self, foo, baz):
        pass
```

## How To Run Tests
```
$ pytest
```
## Authors
- Khaing Su Thway
- Aung Khant Maw

## Reference 

### Books

- [Reproducible Machine Learning for Credit Card Fraud Detection - Practical Handbook](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Foreword.html)

### Blogs
- [Introduction to Probability with Python](https://ethanweed.github.io/pythonbook/04.02-probability.html)
### Important Topics
- Uniform Distribution
- Normal Distribution
- Poisson Distribution
