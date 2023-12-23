import smtplib as s

server = s.SMTP('smtp.gmail.com' , 587)
server.ehlo()
server.starttls()

server.login("avnigoel216@gmail.com" , "jetk zgqm hinn wzbn")

subject = "Interview Result"
body = "You are selected!! Congratulations"
msg = "subject: {}\n\n{}".format(subject , body)

listAddress = ['avnigoel98@gmail.com' , "avnigoel4200@gmail.com" , 'singhha134@gmail.com']

server.sendmail("avnigoel216@gmail.com" , listAddress , msg)
print("sent the mail")
server.quit()






















