from bs4 import BeautifulSoup
import requests
import lxml
import smtplib, ssl

#Accessing the html code of the product
headers = { 'Accept-Language' : "en-US",
            'User-Agent': "Chrome",
            'Referer': 'https://google.com'}

url = "Enter the url of your product"

website_structure = requests.get(url=url, headers=headers)

#Getting the price of the product as a floating point number
soup = BeautifulSoup(website_structure.text, "lxml")
tag = soup.find(name="span", class_="a-offscreen")
price = float(tag.getText()[1:])
budget = "Enter your budget as a floating point"

if price <= budget:
    new_price = price
    
    #Securing an smtp connection to send the mail when the price drops
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "Insert sender email"
    receiver_email = "Insert receiver email"
    password = "Enter google app password(not account password. Follow https://support.google.com/mail/answer/185833?hl=en)"
    message = f"""\
    Subject: Price for your product has dropped

    The price of your product is {new_price}"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)