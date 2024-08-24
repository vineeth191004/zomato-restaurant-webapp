
## Zomato Restaurant Web Application

This project is a web-based application that allows users to search and view restaurant details from the Zomato dataset. The application provides RESTful APIs for accessing restaurant information and filters based on various criteria such as restaurant ID, country, average cost, and cuisines.

# Table of Contents

- [Technologies Used](#technologies-used)
- [Project Architecture](#project-architecture)
- [Modules](#modules)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [REST APIs](#rest-apis)
- [Utilities Developed](#utilities-developed)

# Technologies Used

- **Python**: The core programming language used for backend development.
- **Flask**: A lightweight WSGI web application framework for Python.
- **MySQL**: A relational database management system used for storing restaurant data.
- **SQLite**: Initially used for data storage and later migrated to MySQL.
- **HTML/CSS**: For building the frontend templates.
- **Flask-CORS**: For enabling Cross-Origin Resource Sharing in the application.

## Project Architecture

The project follows a basic MVC (Model-View-Controller) architecture:

- **Model**: Handles the database interactions, using SQLite for local storage and MySQL for the production database.
- **View**: HTML templates rendered by Flask to display restaurant data.
- **Controller**: Handles HTTP requests, processes data, and returns responses.

## Modules

- **Database Connection Module**: Handles connections to the MySQL database.
- **REST API Module**: Contains endpoints for fetching restaurant data based on various filters and criteria.
- **Template Rendering Module**: Renders HTML pages with restaurant data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/zomato-restaurant-webapp.git
   cd zomato-restaurant-webapp
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. Make sure MySQL is installed and running.
2. Create a MySQL database named `final_zomato_restaurants`.
3. Import the initial dataset into MySQL by running the provided SQL migration script or by using the migration function in the code.

## Running the Application

1. Start the Flask application:

   ```bash
   flask run
   ```

2. Access the application in your web browser at `http://localhost:5000`.

## REST APIs

- **`GET /restaurants`**: Retrieves a list of restaurants with optional filters like `restaurant_id`, `country`, `avg_cost_min`, `avg_cost_max`, `cuisines`, and `search`.
- **`GET /restaurant/<int:restaurant_id>`**: Retrieves details of a specific restaurant by its ID.

## Utilities Developed

- **Data Migration Utility**: A script for migrating SQLite data to MySQL.
- **Database Connection Utility**: A reusable function for establishing and closing database connections.
- **Search and Filter Utility**: Logic for building dynamic SQL queries based on user input.
