import smtplib,ssl
import random

def mailSend(names_dict):
    name = random.sample(list(names_dict.keys()),k=len(names_dict))
    n = 0
    for i in names_dict.keys():
        message = f"""
        The secret santa event is being organised and 
        You will be gifting {name[n]}"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
         server.login("secretsanta.py12@gmail.com", "qunmiyytnzlbwlnx")
         server.sendmail("secretsanta.py12@gmail.com", names_dict[i], message)
        n += 1


    

