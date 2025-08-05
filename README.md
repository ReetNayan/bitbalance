# BiteBalance - Calorie Tracking Application

BiteBalance is a desktop application designed to help you track your daily calorie and nutrient intake. With a simple and intuitive interface, you can search for food items, add them to your daily log, and visualize your consumption trends over time.

## Table of Contents

  - Project Overview
  - Features
  - How It Works
  - Getting Started
      - Prerequisites
      - Installation
  - Usage
  - File Descriptions

## Project Overview

This application provides a user-friendly platform for monitoring dietary habits. Users can search for various food items, view their nutritional information, and log their consumption. The application then allows users to track their total calorie intake over time with a graphical representation.

## Features

  - **Food Search**: Search for food items from a comprehensive list. 
  - **Nutrient Information**: Get detailed nutritional data for food items, including calories, fat, protein, carbohydrates, sugar, and fiber.
  - **Daily Intake Logging**: Add food items and their consumed amounts to your daily intake log.
  - **Date Picker**: Select the date for which you want to log your food intake.
  - **Calorie Tracking**: Visualize your calorie intake trend over time with a line graph.
  - **Dynamic Calculation**: Adjust the nutritional information based on the consumed amount of the food item.

## How It Works

The application is built with a frontend and a backend component:

  - **Frontend (`frontend.py`)**: The user interface is created using the `flet` library.  It captures user input, displays food data, and visualizes the calorie tracking graph using `matplotlib`. 
  - **Backend (`backend.py`)**: This module handles the data operations.  It retrieves food information from a `food-list.csv` file and detailed nutritional data from a MySQL database named `food_database`. It also manages user consumption data stored in `user-data.csv`.

When a user searches for a food, the backend finds matching items from the CSV file. Upon selecting a food, its detailed nutritional data is fetched from the MySQL database. When the user adds a food to their intake, the date and calorie information are appended to the `user-data.csv` file. The tracking feature then reads from this CSV to generate a plot of calorie intake over time.

## Getting Started

To run this application on your local machine, follow these steps.

### Prerequisites

  - Python 3
  - MySQL Server
  - The following Python libraries:
      - `flet`
      - `mysql-connector-python`
      - `matplotlib`

### Installation

1.  **Clone the repository:**
2.  **Install Python libraries:**
    ```sh
    pip install flet mysql-connector-python matplotlib
    ```
3.  **Database Setup:**
      - Make sure your MySQL server is running.
      - In `backend.py`, update the MySQL connection details with your credentials:
        ```python
        databaseConnection=mysql.connector.connect(
        host='localhost',
        user="your_username",
        password="your_password",
        database='food_database'
        )
        ```
      - You will need a database named `food_database` with a table `food_data` and a `food-list.csv` file with the appropriate data for the application to function correctly.

## Usage

To start the application, run the `frontend.py` file:

```sh
python frontend.py
```

The application window will open, and you can start by searching for a food item to add to your meal. Once a food is added, its nutritional information will be displayed. You can then specify the amount consumed and add it to your daily intake after selecting a date. To see your progress, click on the "Track total calorie intake" button to generate a graph.

## File Descriptions

  - **`frontend.py`**: Contains the code for the user interface using the `flet` library.
  - **`backend.py`**: Manages data retrieval and storage, interacting with CSV files and a MySQL database.
  - **`main.py`**: Appears to be an example file for `flet`'s WebView functionality and is not part of the core BiteBalance application.
