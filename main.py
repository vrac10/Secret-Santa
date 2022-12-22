import smtplib,ssl
import random
f = open("data.txt",'r')
names = {i.split(',')[0] : i.split(',')[1].replace('\n', '') for i in f.readlines()}
name = random.sample(list(names.keys()),k=len(names))
n = 0
for i in names.keys():
    message = f"""
    The secret santa event is being organised and 
    You will be gifting {name[n]}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("secretsanta.py12@gmail.com", "qunmiyytnzlbwlnx")
        server.sendmail("secretsanta.py12@gmail.com", names[i], message)
    n += 1