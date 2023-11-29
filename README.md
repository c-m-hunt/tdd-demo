# TDD Demo

## What is TDD?
RED -> GREEN -> REFACTOR

* RED - Write a failing test
* GREEN - Write the minimum amount of code to pass the test
* REFACTOR - Refactor the code

## Why TDD?
* Preparation is completed before writing the code
* Code is documented through tests
* Simplifies code
* Avoids code duplication
* Quick feedback
* Long term investment in your code
* Removing "the code is done, but I still need to write the tests" mentality
  * Reduces the chance of not writing tests
  * Removing stakeholder pressure to release code without tests

Byproducts:
* High test coverage
* Creates confidence from customers
* Increase agility in developing
* No unnecessary code
* SAVED TIME AND MONEY LONG TERM
* HAPPIER CUSTOMERS AND DEVELOPERS

## Setup
- Open in VS Code
- Open in devcontainer
- Open a terminal in VS Code and run `poetry shell`

## Run Pytest Watcher
```bash
ptw .
```

## Run coverage report
```bash
coverage run -m pytest
coverage report
```
```
Name           Stmts   Miss  Cover
----------------------------------
main.py            9      0   100%
main_test.py      27      0   100%
----------------------------------
TOTAL             36      0   100%
```

## Follow up resources
- https://www.youtube.com/watch?v=tP25Otcrmpo