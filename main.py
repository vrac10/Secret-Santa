import smtplib,ssl
import random
names = {'Rahdwgdwgudwgdul' : 'rachit.prince11@gmail.com', 'Radwdiwhdiwhdiwm' : 'secretsanta.py12@gmail.com', 'Rachdit' : 'vrachit106@gmail.com'}
l = []
for i in names.keys():
    while True:
        name = random.choice(list(names.keys()))
        if name not in l or name != i:
            break
    message = f"You will gift {name}"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("secretsanta.py12@gmail.com", "qunmiyytnzlbwlnx")
        server.sendmail("secretsanta.py12@gmail.com", names[i], message)
    


