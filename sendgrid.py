import pandas as pd


df = pd.read_csv('sample.csv', sep =',', header =0)
email ="Statistics to review :{ df} Thanks"
# email = email.format(df=df.to_html())

import os
from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='sarah.maleki83@gmail.com',
    to_emails='recipiants',
    subject='statistic review',
    html_content='<h1>helllllo</h1>'
)

sg = SendGridAPIClient(os.environ.get('api_key'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)