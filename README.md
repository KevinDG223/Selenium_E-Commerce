Hi, There 👋 

📋 Project Overview

This project is an End-to-End (E2E) automated testing framework built with Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.
It automates the testing of an e-commerce demo site by simulating user interactions such as logging in, adding products to the cart, and completing the checkout process.

🎯 Project Objective

The goal of this project is to demonstrate a structured and scalable automation framework capable of handling dynamic test data, multiple browsers, and modular page interactions for better test maintainability and readability.

🚀 How It Works

The test script (test_e2eTestFramework.py) reads user credentials and product names from test_e2eTestFramework.json.

Each test case:

*Opens the browser and navigates to the login page.

*Logs in using the provided credentials.

*Adds the specified product to the cart.

*Proceeds to checkout and confirms the order.

*Validates the success message after order completion.

Browser type (Edge or Chrome) can be chosen via command-line parameters (Default: Edge).



https://github.com/user-attachments/assets/4760db10-f9c8-4632-86c9-57c76073f6b2

