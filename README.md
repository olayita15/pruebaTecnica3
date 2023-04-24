<h1>Employee and Office Management Web App</h1>
This is a simple web application built with Django that allows users to manage employees and offices. The project contains two main models, Office and Employee.

<h2>Office Model</h2>
🏢 The Office model represents the different offices in the organization. It contains the following fields:

name: The name of the office.
address: The physical address of the office.

<h2>Employee Model</h2>
👨‍💼 The Employee model represents the employees in the organization. It contains the following fields:

first_name: The first name of the employee.
last_name: The last name of the employee.
email: The email address of the employee.
phone_number: The phone number of the employee.
office: A foreign key to the Office model, representing the office where the employee works.

<h2>Usage</h2>
To run the application locally, you will need to have Python and Django installed on your machine. Once you have cloned the repository, navigate to the project directory and run the following command:

Copy code
python manage.py runserver
This will start the Django development server, and you can access the application by navigating to http://localhost:8000/ in your web browser.

<h2>Contribution</h2>
🤝 Contributions to this project are welcome. If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.