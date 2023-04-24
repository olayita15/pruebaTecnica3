<h1>Employee and Office Management Web App</h1>
<p>This is a simple web application built with Django that allows users to manage employees and offices. The project contains two main models, <strong>Office</strong> and <strong>Employee</strong>.</p>
<h2>Office Model</h2>
<p>🏢 The <strong>Office</strong> model represents the different offices in the organization. It contains the following fields:</p>
<ul>
  <li><strong>name:</strong> The name of the office.</li>
  <li><strong>city:</strong> The city where the office is located.</li>
  <li><strong>phone:</strong> The phone number of the office.</li>
</ul>
<h2>Employee Model</h2>
<p>👨‍💼 The <strong>Employee</strong> model represents the employees in the organization. It contains the following fields:</p>
<ul>
  <li><strong>first_name:</strong> The first name of the employee.</li>
  <li><strong>last_name:</strong> The last name of the employee.</li>
  <li><strong>email:</strong> The email address of the employee.</li>
  <li><strong>phone_number:</strong> The phone number of the employee.</li>
  <li><strong>office:</strong> A foreign key to the <strong>Office</strong> model, representing the office where the employee works.</li>
</ul>
<h2>Usage</h2>
<p>To run the application locally, you will need to have Python and Django installed on your machine. Once you have cloned the repository, navigate to the project directory and run the following command:</p>
<pre><code>python manage.py runserver</code></pre>
<p>This will start the Django development server, and you can access the application by navigating to <a href="http://localhost:8000/">http://localhost:8000/</a> in your web browser.</p>
<h2>Contribution</h2>
<p>🤝 Contributions to this project are welcome. If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.</p>
<p><em>Created by the user 'pedro' with password 'pedrocompany123' for managing their employees and offices.</em></p>