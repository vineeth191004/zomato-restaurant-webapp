
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
   git clone https://github.com/vineeth191004/zomato-restaurant-webapp.git
   cd zomato-restaurant-webapp
   ```

2. Install the required packages as per the code.
   **pandas**
   **sqlite3**
   **Flask**
   **mysql-connector-python**
   **flask-cors**


## Database Setup

1. Make sure MySQL is installed and running.
2. Create a MySQL database named `final_zomato_restaurants`.
3. Import the initial dataset into MySQL by running the provided SQL migration script or by using the migration function in the code.

## Running the Application

1. Firstly run the **data.py** so that the 2 dataframes i.e zomato.csv and Country code.xlsx will be merged as the Country Code is common in both the dataframes.
2. Secondly run the **sql.py** so that sqllite3 stored database is converted to MySQL Workbench database. (I done for my convenience)
3. Then run the **app.py** for the web application to handle the routes and rendering the templates.
4. Access the application in your web browser at `http://localhost:5000`.

## REST APIs

- **`GET /restaurants`**: Retrieves a list of restaurants with optional filters like `restaurant_id`, `country`, `avg_cost_min`, `avg_cost_max`, `cuisines`, and `search`.
- **`GET /restaurant/<int:restaurant_id>`**: Retrieves details of a specific restaurant by its ID.

## Utilities Developed

- **Data Migration Utility**: A script for migrating SQLite data to MySQL.
- **Database Connection Utility**: A reusable function for establishing and closing database connections.
- **Search and Filter Utility**: Logic for building dynamic SQL queries based on user input.
