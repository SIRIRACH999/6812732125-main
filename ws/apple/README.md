# Project Overview

This project is a web application that utilizes HTML templates to create a dashboard interface. The dashboard is designed to display user information and various data visualizations.

## Project Structure

- **templates/base.html**: This file serves as the base template for the application. It contains the common HTML structure and elements that will be used across different pages.
  
- **templates/index.html**: This file is the dashboard template. It has been modified to remove existing content and now includes a new table to display users based on specific criteria.

## Setup Instructions

1. **Database Setup**:
   - Open SQLite3 in the `apple` folder to manage your database.
   - Ensure that your database is set up correctly to store user information.

2. **Modifications**:
   - The `index.html` file has been updated to include a new table that displays users with the following columns:
     - `studentID`
     - `prefix`
     - `Firstname`
     - `Lastname`
   - This table is filtered to show only users with `#` as their `runnumber`.

3. **Adding Data**:
   - You can add data to the new table later as needed.

## Usage

- To view the dashboard, navigate to the appropriate route in your web application.
- Ensure that your database is populated with user data to see the results in the new table.