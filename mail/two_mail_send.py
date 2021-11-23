import smtplib

sender_email = "wirelineproject@pi108.com"
rec_email = "mlalwani@xcaliberinfotech.com"
#password = input(str("Please enter your password : "))
message = "Subject: Test execution from script \n\n Hey, this is executed via script"

server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.login(sender_email, "RHryLbzux6VjRWFw")
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)