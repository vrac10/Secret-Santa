from tkinter import *
from tkinter import messagebox as mb
from main import *
root = Tk()
root.title("Secret Santa")
root.geometry("600x600")
names_dict = {}
global n 
x = [0]
z = []


def add_participant(n = x):
    global label_Drop
    global label
    if emailTB.get() != "" and nameTB.get() != "":

        names_dict[nameTB.get()] = emailTB.get()
        print(names_dict)
        

        if len(n) == 1:
            label_Drop = Label(root, text="NAMES ADDED ARE: ", font= 25)
            label_Drop.grid(row=0, column=1)

        
        label = Label(root, text= f" {len(n)}) {nameTB.get()} : {emailTB.get()}")
        label.grid(row=len(n),column=1, padx= 50)
        z.append(label)
        n.append(0)
        nameTB.delete(0,END)
        emailTB.delete(0,END)

    elif emailTB.get() == "" and nameTB.get() != "":
        mb.showerror(message="Please enter email address!")
    elif nameTB.get() == "" and emailTB.get() != "":
        mb.showerror(message="Please enter a name!")
        mb.showerror(message="Please enter the fields!")

def delete_participant():

    a = len(list(names_dict.keys()))
    
    if a == 1:
        names_dict.popitem()
        label_Drop.destroy()
        z[a-1].destroy()
        z.pop(a-1)
        x.clear()
        x.append(0)
        

    elif a > 1:
        names_dict.popitem()
        z[a-1].destroy()
        z.pop(a-1)
        x.pop()

    else:
        mb.showerror(message="No names added!")
        
def send_mail():
    if mb.askyesno(message="Are you sure you want to submit?"):
        mailSend(names_dict)
        label_Drop.destroy()
        for i in z:
            i.destroy()
        z.clear()
        


    

    
name_label = Label(root, text= "Name")
name_label.grid(row=0,column=0)

nameTB = Entry(root, width= 25, bg="white", borderwidth=3, fg= "black")
nameTB.grid(row=1,column=0)

email_label = Label(root, text= "Email Address")
email_label.grid(row=2,column=0)

emailTB = Entry(root, width= 25, bg="white", borderwidth=3, fg= "black")
emailTB.grid(row=3,column=0)

add_button = Button(root, text= "ADD PARTICIPANT", width=12, command= add_participant)
add_button.grid(row=4,column=0)


delete_button = Button(root, text="DELETE LAST ADDED", width=16, command=delete_participant)
delete_button.grid(row=5,column=0)

submit_button = Button(root, text="SEND MAIL", width=8, command=send_mail)
submit_button.grid(row=6,column=0)




root.mainloop()

