SQL Practice Project
This repository contains my practice project for SQL where I interact with a SQLite database, 'market.db'.

Project Overview
In this project, I created a simple database for a hypothetical supermarket that includes three tables - products, clients, and orders.

The products table contains details about the products available in the supermarket such as name, description, price, and the quantity currently in stock.

The clients table holds information about the customers including their name, email, phone number, and address.

The orders table maintains a record of all the orders placed by the customers, the date of purchase, and the total amount of the order. It also includes a foreign key to associate each order with a particular client.

This practice project helped me to understand how to plan, create, and interact with SQL databases. It also includes operations such as creating tables, inserting data, updating data, and querying data.

Files in the Repository
market.db: This is the SQLite database file.
database_interaction.py: This Python script is used to interact with the SQLite database. It includes functions to insert, select, update, and delete data.
Running the Project
You need Python 3 and SQLite installed on your system to run this project.

Clone this repository.
Open a terminal/command prompt and navigate to the repository directory.
Run the database_interaction.py script using the command python3 database_interaction.py.
You should see some output that demonstrates various operations on the database such as inserting, selecting, updating, and deleting data.
