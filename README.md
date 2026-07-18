# Secure Coding Review – Python Login System

## Description

This project is a **Secure Coding Review** of a simple **Python-based Login System**. The purpose of the project is to demonstrate how security vulnerabilities can be identified through **manual code inspection** and **static analysis tools**.

The application uses **SQLite** for storing user credentials and provides a basic login interface where users enter a username and password. The code was intentionally designed with common security weaknesses so that they could be detected, analyzed, and documented as part of the security audit.

## Objectives

* Select a programming language and application for security auditing.
* Perform a secure code review of the application.
* Identify common vulnerabilities such as SQL Injection, hardcoded credentials, and insecure password handling.
* Use a static analysis tool (**Bandit**) to detect security issues automatically.
* Recommend secure coding practices and remediation steps.

## Technologies Used

* **Programming Language:** Python
* **Database:** SQLite
* **Static Analysis Tool:** Bandit
* **Code Editor:** Visual Studio Code

## Security Vulnerabilities Reviewed

The audit focused on identifying the following issues:

* SQL Injection
* Hardcoded Passwords
* Plain Text Password Storage
* Missing Input Validation
* Weak Error Handling

## Review Methodology

The application was reviewed using two approaches:

1. **Manual Code Review** – inspecting the source code line by line to identify insecure coding practices.
2. **Static Analysis** – scanning the code using Bandit to automatically detect potential security vulnerabilities.

## Recommendations

The following secure coding practices were recommended:

* Use parameterized SQL queries.
* Hash passwords using secure algorithms such as **bcrypt**.
* Validate and sanitize all user input.
* Store secrets using environment variables instead of hardcoding them in the source code.
* Implement secure error handling and logging.

## Expected Outcome

This project demonstrates the importance of secure coding practices in software development. By identifying vulnerabilities and applying remediation techniques, the security posture of the application can be significantly improved, reducing the risk of unauthorized access and data compromise.
