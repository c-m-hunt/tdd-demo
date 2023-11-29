# TDD Demo

## What is TDD?
RED -> GREEN -> REFACTOR

* Write a failing test
* Write the minimum amount of code to pass the test
* Refactor the code

## Why TDD?
* The thinking is completed while writing the tests and not code
* No unnecessary code
* Byproduct - High test coverage

* Creates confidence
* Increase agility in developing 

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