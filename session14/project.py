import smtplib as s

server = s.SMTP('smtp.gmail.com' , 587)
server.ehlo()
server.starttls()

server.login("email.com" , "password")

subject = "Interview Result"
body = "You are selected!! Congratulations"
msg = "subject: {}\n\n{}".format(subject , body)

listAddress = ['email.com' , "email.com" , 'email.com']

server.sendmail("avnigoel216@gmail.com" , listAddress , msg)
print("sent the mail")
server.quit()


















