# Email-Sender

## Overview
This project is a web application that integrates a Python script for automating email sending. The application extracts top stories from Hacker News and sends them via email using a Flask backend, with a simple HTML/CSS/JavaScript frontend for user interaction.

## Features
- Extracts top stories from Hacker News
- Sends the extracted stories via email
- Simple web interface for inputting email details

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Email Sending**: `smtplib`, `email.mime`
- **Web Scraping**: `requests`, `BeautifulSoup`

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Flask
- Requests
- BeautifulSoup

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Pabitra3/Email-Sender.git
   cd Email-Sender
   ```

2. **Set Up a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install flask requests beautifulsoup4
   ```

## Configuration

1. **Update Email Credentials**
   Open `app.py` and update the `send_email` function with your email credentials:

   ```python
   SERVER = 'smtp.gmail.com'  # Your SMTP server
   PORT = 587  # Port number for TLS
   FROM = 'your-email@gmail.com'  # Your email ID
   PASS = 'your-email-password'  # Your email password
   ```

   **Security Note**: Avoid hard-coding your email password. Use environment variables or a secure vault for storing sensitive information.

## Usage

1. **Run the Flask Application**
   Start the Flask server by running:
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000/`.

2. **Access the Web Application**
   Open your web browser and go to `http://127.0.0.1:5000/`. You will see a form where you can input:
   - Your email address
   - Your email password
   - The recipient's email address

   After filling in the details, click "Send Email" to send the email with Hacker News stories.

## Code Structure
- `app.py`: Contains the Flask application and the Python script for extracting and sending emails.
- `templates/index.html`: The HTML form used for inputting email details.
- `static/`: (Optional) Place for any static files like CSS or JavaScript (currently not used).

## Troubleshooting
- **SMTP Authentication Error**: Ensure that you have enabled "Less secure app access" for your Gmail account or use OAuth for a more secure method.
- **Email Not Sent**: Check your email server settings and credentials. Ensure you have an active internet connection.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure to follow the coding standards and include tests if applicable.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please contact developersivaay@gmail.com.