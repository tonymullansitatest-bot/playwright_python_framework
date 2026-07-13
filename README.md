# Playwright Behave Framework

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Gherkin Language](#gherkin-language)
- [Installation](#installation)
- [Configuration](#configuration)
  - [behave.ini](#behaveini)
  - [config.ini](#configini)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [CI/CD Pipeline](#cicd-pipeline)
  - [.yml file](#yml-file)


## Overview
The **Playwright Behave Framework** is a test automation framework built with Python, Behave, and Playwright. It is designed for efficient, end-to-end testing on multiple browsers and platforms. The framework supports Behavior-Driven Development (BDD), empowering teams to collaborate by writing tests in Gherkin syntax—a natural language style easily understood by developers, testers, and business stakeholders.

Key Features:

- Cross-browser and cross-platform support.
- BDD test scenarios written in Gherkin syntax, facilitating collaboration among developers, testers, and business stakeholders.
- Debugging made easy with Playwright's video recording, tracing, and screenshots.
- Detailed test reports generated with Allure.
- Seamless integration with Azure DevOps for CI/CD pipelines.

Documentation for [Playwright](https://playwright.dev/), [Behave](https://behave.readthedocs.io/en/stable/), and [Allure](https://allurereport.org/docs/) can be found on their respective websites.
## Prerequisites
- Pip (Python package installer)
- Python 3.11+
- Azure DevOps account (for CI/CD pipeline and private package)

## Project Structure
The framework has a modular and organized structure:
```
project-root/
├── src/
│   ├── features/
│   │   ├── feature_folder/ or example.feature 
│   │   ├── steps/
│   │   │   └── step_definitions.py
│   │   └── environment.py
│   ├── pages/
│   │   └── pages.py
│   └── utils/
│       └── util_methods.py
├── behave.ini
├── config.ini
├── requirements.txt
├── requirements_private.txt
├── azure-pipelines.yml
└── README.md
```
### features/
Contains the `.feature` files that describe the test scenarios in Gherkin syntax. The `.feature`  files can reside in any subfolder under `./features` folder.<br>
Also includes the steps folder for step definitions and environment.py for global setup/teardown configurations. Behave needs this file structure in order to run the tests.
 ```
 ├── features/
 │      ├── steps/
 │      ├── environment.py
 ```

### steps/
Contains the step definitions that implement the steps described in the feature files. These are written in Python and link the Gherkin steps to the actual test code.  

### environment.py
A special module in Behave that allows you to set up and tear down test environments. It can be used to configure global settings, initialize resources, and clean up after tests.  
***It contains the framework configurations provided by the private package.***

### pages/
Contains page object models representing the application's web pages. Each model encapsulates page-specific methods and element interactions.

### utils/
Contains utility methods that can be reused across different test scenarios.

### config.ini
Manages the configurations of the framework, such as browser settings, context settings, and paths for screenshots, videos, and traces.  

### behave.ini
A configuration file for Behave that allows you to set default values for various settings, such as the browser, browser platform, and environment to use for the tests, some of these values can be overridden by passing them as command-line arguments.

### azure-pipelines.yml
A configuration file for the Azure DevOps pipeline that defines the steps to build, test, and deploy the project. It integrates with the Azure DevOps services to automate the CI/CD process.

## Gherkin Language
The framework contains examples of Gherkin syntax, check the `./gherkin_examples` folder for implementation examples.
```gherkin
Feature: The feature being tested
    A detailed description of the feature,
    which can span multiple lines.

    Background: Preconditions that must be met before any scenarios are executed.
        Given It can have multiple steps
        And It can have multiple steps

    Scenario: A description of the scenario being tested.
        Given Is used for preconditions (like login to the system or navigating to a page)
        When Is used for actions (like clicking a button or entering some data)
        Then Is used for the expected results (like verifying the output or the state of the system)

    Scenario: Another scenario description, with the option to use the "And" keyword for readability and clarity.
        Given Is used for preconditions (like login to the system or navigating to a page)
        And Is used for additional preconditions
        And Is used for additional preconditions
        When Is used for actions (like clicking a button or entering some data)
        And Is used for additional actions
        And Is used for additional actions
        And Is used for additional actions
        Then Is used for the expected results (like verifying the output or the state of the system)
        And Is used for additional expected results

    Scenario Outline: A description of a scenario outline, for each example from the table the scenario will be executed.
        Given Is used for preconditions (like login to the system or navigating to a page)
        When Is used for actions (like clicking a button or entering some data)
        Then Is used for the expected results (like verifying the output or the state of the system)

        Examples: Defines the data used in the scenario outline
            | parameter1 | parameter2 | parameter3 |
            | value1     | value4     | value7     |
            | value2     | value5     | value8     |
            | value3     | value6     | value9     |
```  

Steps can have parameters as simple parameter, text parameter or table parameter (check examples).

Features, scenario, and example tags are used to filter tests:
    A tag on a feature applies to all scenarios within it.
    A tag on a scenario applies only to that scenario.
    A tag on an example applies only to that specific example.


For more information about Gherkin syntax that Behave covers, check the official documentation:
https://behave.readthedocs.io/en/stable/gherkin.html
  




## Installation
1. Clone the repository: <br>
   Open
    ```sh
    git clone https://sita-pse.visualstudio.com/QE%20Automation/_git/playwright_python_framework
    cd <repository-directory>
    ```
   ***Copy all files and folders, except the `.git` folder, to the directory for the new project.*** <br><br>

2. Create and activate the virtual environment (Optional if the venv is already created):
   <br> Open PyCharm IDE and run the following commands in the terminal: 
   ```sh
    python -m venv venv
    venv\Scripts\activate 
    ```   
3. Install project dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Install Playwright browsers:
    ```sh
    playwright install
    ```
5. Install private dependencies (contains the framework configurations):
    ```sh
    pip install keyring artifacts-keyring
    pip install -r requirements_private.txt --index-url "https://sita-pse.pkgs.visualstudio.com/c2e3f9b6-7c38-48ee-8ec9-8797a525b680/_packaging/python_automation/pypi/simple/"
    ```
   
## Configuration

### `behave.ini`
Configure the test settings in the `behave.ini` file:
```ini
[behave.userdata]
browser = chrome # set the browser to run the tests
browser_platform = desktop # set the platform to run the tests

environment = dev # set the environment to run the tests
dev = https://environment_one.com/
prod = https://environment_two.com/

octane = False # set to True if you want to send the results to Octane
```
**The following parameters are mandatory in the `behave.ini` file: `browser`, `browser_platform`, `octane`, `environment` with the expected options like `dev`, `prod` , and the corresponding URLs for the environments.** <br>
Note: Command-line parameters take precedence over .ini configuration settings if both are provided.
```sh
behave environment=prod -D browser=firefox -D platform_browser=mobile 
```
***If a parameter is missing, the framework will throw an error.***

### `config.ini`
Configure the framework settings in the `config.ini` file, **the following parameters are mandatory**:
```ini
[BROWSER]
HEADLESS = False
VIEWPORT_WIDTH = 0 #if width and height are 0 it will take the screen size
VIEWPORT_HEIGHT = 0 #if width and height are 0 it will take the screen size
IGNORE_HTTP_ERRORS = True

[MOBILE]
MOBILE_DEVICE_MODEL = iPhone 11

[DEBUG]
ENABLE_RECORDING = True
ENABLE_TRACING = True
ENABLE_TRACING_SCREENSHOTS = True
ENABLE_TRACING_SNAPSHOTS = True
ENABLE_TRACING_SOURCES = True

[DATA TYPES]
SCREENSHOT_TYPE = webp

[PATHS]
SCREENSHOT_DIR = debug/screenshots/
VIDEO_DIR = debug/videos/
TRACE_DIR = debug/trace/
LOG_DIR = debug/logs/

[OCTANE]
MODULE = 17928 example
RELEASE = 7084 example
SPRINT = 10429 example
SUITE_ID = 214128 example
SUITE_RUN_NAME = Test Automation Run example
OCTANE_URL = https://octane-qa.sitacloud.aero example
SHAREDSPACE_ID = 2002 example
WORKSPACE_ID = 6002 example
WORKSPACE_USER = 15033 example
USER_ID = user.id@sita.aero
PASSWORD = password
AUTOMATED_TEST_ID = Octane test type: Automated id (ask the automation team for the id)
```
All the parameters from [BROWSER], [MOBILE], [DEBUG], [DATA TYPES], [PATHS] are pre-configured with default values in the framework and can be modified as needed. <br>
For [OCTANE] if a parameter is not set the API calls will fail. <br>
**If a parameter is missing, the framework will use a default value and display a WARNING log in the console with the used value.**
## Running Tests
Run the tests using the following command:
1. Run all tests:
```sh
behave
```
2. Run tests with specific tags:
```sh
behave --tags=@tag_name  
behave --tags="@tag1,@tag2"
or 
behave --tags="@tag1 and @tag2"
```
Logical operators like `and`, `or`, and `not` can be used to combine tags.

3. Run tests with specific configurations:
```sh
behave --tags=<tag> -D environment=<env> -D browser=<browser> -D platform_browser=<platform_browser> -D octane=<octane> 
behave --tags=@regression -D environment=dev -D browser=chrome -D platform_browser=desktop -D octane=True
behave --tags=@practice -D base_url=https://practicesoftwaretesting.com/
```
This command will override the values in the `behave.ini` file just for the current run.

## Test Reports
**To generate and serve the Allure report on the local machine, use the following commands.  <br><br>**
To generate and save the report (a newly generated report will overwrite the existing one):
```sh
allure generate allure-results -o allure-report --clean
```
To view the report in the browser:
```sh
allure serve allure-results
```

## CI/CD Pipeline
The project is integrated with Azure DevOps for CI/CD. The pipeline configuration can be found in the `azure-pipelines.yml` file.
- Parameters like `browser`, `environment`, `platform_browser`, `tags` and `octane` can be passed from the Azure Pipelines UI to run the tests with specific configurations.

### .yml file
The `azure-pipelines.yml` file contains the pipeline configuration. The parameters are configurable, for example:
```yml
- name: environment
  displayName: Select environment
  type: string
  default: dev
  values:
    - dev
    - prod
```
If a new value is added to the `values` list like `qa` , then the `behave.ini` file should be updated with the new environment URL.

 