# API Automation with python, pytest for reqres.in

This project is a Python-based API automation framework for testing the `reqres.in` RESTful web service. It uses the pytest testing framework and GitHub Actions for continuous integration.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Test execution](#runtests)

## Features

- Automated testing of various API endpoints.
- Continuous integration with GitHub Actions.
- Test report generation and saving as an artifact.

## Prerequisites

Before you get started, ensure you have the following prerequisites:

- Python 3.x
- `pip` for package management

## Installation

git clone https://github.com/yourusername/reqres-api-automation.git

cd reqres-api-automation

pip install -r requirements.txt


## Test execution

pytest tests/test_api.py

## Test Reports
The tests generate an HTML test report, which can be found in the project directory as report.html.