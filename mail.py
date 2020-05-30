import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()   
s.login("sender's email", "pass") 
message = "Hey Developer, Finally we got the model trained and accuracy is more than 95%"
s.sendmail("sender mail", "reciever mail", message) 
s.quit()
