# PythonAutomationTraining

## Description

Project contains tasks for Auomation QA Python Course:
* Phase 1: Python Basics
* Phase 2: Working with files
* Phase 3: UI Testing (Selenium)
* Phase 4: Reporting (Allure)
* Phase 5: API Testing with Requests
* Phase 6: PyTest Parallel Execution

**Project Status:**

[![CircleCI](https://circleci.com/gh/vs-odessa/PythonAutomationTraining/tree/master.svg?style=svg)](https://circleci.com/gh/vs-odessa/PythonAutomationTraining/tree/master)


## Prerequisites

* Python 3 is required
* Install python packages from requirements.txt:  

      pip install -r requirements.txt
* Install Allure according to docs:
https://docs.qameta.io/allure/

## Running tests

### Unit tests

    pytest -v tests_functions/

### API tests

    pytest -v tests_api/
    
### UI tests

    pytest -v tests_ui/
    
## Creating Allure reports

Add option --alluredir={path_to_allure_reports_dir} at pytest run command.
_Example:_

    pytest -v tests_api/ --alluredir=./test-reports/allure
    
To generate an html report, run command:

    allure generate -c ./test-reports/allure -o ./test-reports/allure_html_reports
    
## Running tests in parallel

To run tests in parallel, run command:

    pytest -n NUM

Select NUM according to CPU number for your testing host.
