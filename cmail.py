import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #creating object for gmail
    server.login('angirekulasravya4@gmail.com','bine zhpk amis vmzy')
    msg=EmailMessage() #creating object for EmailMessage to form email
    msg['FROM']='angirekulasravya4@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
