# Fruit Shop

## Project Description

Fruit Shop is a Django-based web application for managing a fruit shop. It provides various functionalities such as viewing products, user registration, login, and commenting.

## Installation Instructions

1. Clone the repository:
   ```
   git clone https://github.com/ErfanShokrollahzadeh/PyShop.git
   ```
2. Navigate to the project directory:
   ```
   cd PyShop/fruit_shop
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Apply the database migrations:
   ```
   python manage.py migrate
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage Instructions

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. You will see the home page of the Fruit Shop application.
3. Use the navigation bar to access different sections of the application, such as products, user registration, login, and commenting.

## Description of `main.py` and its Functionality

The `main.py` file contains a sample Python script with a function `print_hi` that prints a greeting message. This file is not directly related to the Fruit Shop application but serves as an example of a simple Python script.

## Overview of the Project's Overall Functionality

The Fruit Shop project is a Django-based web application that provides the following functionalities:

- **Home Page**: Displays a welcome message and information about the fruit shop.
- **Products Page**: Lists all the available products in the fruit shop with their details.
- **User Registration**: Allows users to sign up by providing their email, password, and address.
- **User Login**: Allows users to log in using their email and password.
- **Commenting**: Provides a section for users to write and submit comments.
- **Order Page**: Displays more information about the products and provides a payment button.

The project uses Django's built-in features for handling templates, views, and models to create a dynamic and interactive web application.
