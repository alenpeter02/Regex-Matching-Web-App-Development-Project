# Regex-Matching-Web-App-Development-Project
Regex Matching Web App Development Project and Deploying Application on AWS
## Public Link:
http://54.234.27.237:5000/

## Features:
## 1.	Regex Tester:
• Users can input a test string and a regular expression pattern.
•	Upon submission, the application highlights the matches in the test string and displays the number of matches found.
•	Each match is presented along with its position in the test string and the surrounding text.
## 2.	Email Validator:
•	Users can input an email address and click the "Validate" button to check if the email address is valid.
•	The application communicates with the server to perform the email validation using a regular expression for email format matching.
•	The validation result (valid or invalid) is displayed to the user.

# Technologies Used:
## •	Flask:
Flask is a lightweight Python web framework used for building web applications.
## •	JavaScript: 
JavaScript is used for client-side interactivity, including highlighting regex matches and performing email validation without reloading the page.
## •	Regular Expressions: 
Regular expressions are used for pattern matching in both the Regex Tester and Email Validator functionalities.
## •	HTML/CSS: 
HTML is used for structuring web pages, while CSS is used for styling.

# Deployment:
## AWS EC2 (Elastic Compute Cloud):
•	AWS EC2 is utilized for hosting and deploying the web application.
•	An EC2 instance is provisioned to run the Flask application.
•	The application is accessible to users via the public IP address associated with the EC2 instance

# Project Structure:
## Python Files:
•	app.py: This file contains the Flask application code, including route definitions for handling HTTP requests.
## HTML Template:
•	index.html: This HTML file serves as the main template for the web application. It contains the structure of the web pages and includes JavaScript for client-side functionality.
## CSS Stylesheet:
•	Inline CSS styling and some external CSS stylesheets are used for styling the web pages.
## JavaScript:
•	Inline JavaScript functions and scripts are included within the HTML template for interactivity.
