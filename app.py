# app.py
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

app = Flask(__name__)

# Function to extract news
def extract_news(url):
    print('Extracting Hacker News Stories.....')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b><br>'+'-'*50+'<br>')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        if tag.text != 'More':
            cnt += (str(i+1) + ': ' + tag.text + "<br>")
    return cnt

# Function to send email
def send_email(to_email, from_email, password):
    now = datetime.datetime.now()
    content = extract_news('https://news.ycombinator.com/')
    content += ('<br>--------------------<br><br>End of Message')
    
    # Composing Email
    msg = MIMEMultipart()
    msg['Subject'] = 'Top News Stories HN [Automated Email] ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    msg['From'] = from_email
    msg['To'] = to_email
    msg.attach(MIMEText(content, 'html'))

    # Sending email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print('Email sent successfully!')
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and send email
@app.route('/send_email', methods=['POST'])
def handle_email():
    to_email = request.form['to_email']
    from_email = request.form['from_email']
    password = request.form['password']

    if send_email(to_email, from_email, password):
        return "Email sent successfully!"
    else:
        return "Failed to send email."

if __name__ == '__main__':
    app.run(debug=True)
