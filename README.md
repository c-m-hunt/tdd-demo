# TDD Demo

## What is TDD?
RED -> GREEN -> REFACTOR

* Write a failing test
* Write the minimum amount of code to pass the test
* Refactor the code

## Why TDD?

* The thinking is completed while writing the tests and not code
* The code is written to pass the tests
* The code is written to be testable
* High test coverage
* The code is written in small chunks

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