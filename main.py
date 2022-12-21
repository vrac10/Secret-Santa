import smtplib,ssl
import random
names = {'Rahdwgdwgudwgdul' : 'rachit.prince11@gmail.com', 'Radwdiwhdiwhdiwm' : 'secretsanta.py12@gmail.com', 'Rachdit' : 'vrachit106@gmail.com'}
name = random.sample(list(names.keys()),k=len(names))
n = 0
for i in names.keys():
    message = f"You will gift {name[n]}"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("secretsanta.py12@gmail.com", "qunmiyytnzlbwlnx")
        server.sendmail("secretsanta.py12@gmail.com", names[i], message)
    n += 1
    


