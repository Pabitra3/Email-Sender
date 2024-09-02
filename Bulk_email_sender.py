import requests
from bs4 import BeautifulSoup
# Send the mail
import smtplib
# Email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# System data and time manipulation 
import datetime
now = datetime.datetime.now()
# email content placeholder
content = ""
# Extracting Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories.....')
    cnt = ''
    cnt += ('<b>HN Top Stories:<b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+': :'+tag.text + "\n"+'<br>')if tag.text != 'More'else '')
        # print((tag.prettify)#find_all('span',attrs={'class':'sitestr'}))
    return(cnt)
cnt= extract_news('https://news.ycombinator.com/')
content = cnt
content += ('<br>-------------------- <br>')
content += ('<br> <br> End of Message')
# lets send the Email
print('Composing Email......')
# Update your email details
SERVER = 'smtp.gmail.com' # Your smtp server
PORT =587 # Your port number
FROM = '' # Your email ID
TO = '' # Your to email ID (Can be a list)
PASS = ''# Your email ID's Password
# fp = open(file_name,'rb')
# Create a text/plain message
# msg= MIMEText('')
msg = MIMEMultipart()
# msg.add_header('content-Disposition','attachment', filename='empty.text')
msg['subject']= 'Top News Stories HN[Automated Email]' + ''+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']= FROM   
msg['To']=  TO
msg.attach(MIMEText(content,'html'))
#fp.close()
print('Initiating Server.......')
server = smtplib.SMTP(SERVER,PORT)
# server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo()
server.login(FROM,TO,msg.as_string())
print('Email sent......')
server.quit()
