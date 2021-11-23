import imaplib
import pprint
import email

hostname = "outlook.office365.com"
username = "wirelineproject@pi108.com"
password = "RHryLbzux6VjRWFw"



imap_obj = imaplib.IMAP4_SSL(hostname)      #connect to server

imap_obj.login(username,password)

imap_obj.select(mailbox='inbox',readonly=True)  #readonly=False


tmp,email_serial_numbers = imap_obj.search(None,'unseen') #charset=None *criteria = 'ALL'

print(tmp,"\n\n\n",email_serial_numbers)

email_serial_number_list = email_serial_numbers[0].split()
tmp,data = imap_obj.fetch(email_serial_number_list[2],'(RFC822)')
#tmp,data = imap_obj.fetch(email_serial_number_list[0],'BODY.PEEK[]')

#
# pprint.pprint(str(data[0]),type(data[0]))


# print(data[0])
#
# print("\n\n\n\n")
#
# print("len of data",len(data),type(data))
#
# print("\n\n\n\n")
# print("len of data 0 ",len(data[0]),type(data[0]))
#
# print("\n\n\n\n")
# print("len of data 1 ",len(data[1]),type(data[1]))
#
#
# print("\n\n\n\n")
#
#
# print("data 0 \n\n",data[0])
#
# print("\n\n\n\n")
#
# print("data 1 \n\n",data[1])
#
#
# print("datatype of data is", type(data))
email_message = email.message_from_bytes(data[0][1])
#decoded_data = data[0][1].decode('utf-8')
#email_message = email.message_from_string(decoded_data)
#print(email_message,type(email_message),len(email_message))


d1 = {
    "from": None,
    "date": None,
    "subject": None,
    "body": None,
    "attached_file": None
}
d1["from"] = email_message["From"]
d1["date"] = email_message["Date"]
d1["subject"] = email_message["Subject"]
#d1["body"] = email_message["Body"]

# for x in email_message:
#     print(x,end="\n\n\n\n")



print("FROM: ",d1["from"])
print("Date: ", d1["date"])
print("Subject: ", d1["subject"])
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@email_message.walk() length",len(email_message.walk()))
for i,x in enumerate(email_message.walk()):
    print(f"\n\n\n**********************************{i}*****************************")
    print("=======content type is",x.get_content_type())
    print("=======content maintype is type is", x.get_content_maintype())
    #print("=======content disposition is ",x.get("Content-Disposition"), "\n\n\n")
    print("=======content disposition is ", x.get_content_disposition())
    # if x.get_content_type() == "text/plain":
    #     print(x)
    #     payload = x.get_payload(decode=True).decode()
    #     print("\n\npayload type is: ",type(payload))

        # print("========\nx.get_payload(decode=False)", type(x.get_payload(decode=False)),x.get_payload(decode=False))
        # print("========\nx.get_payload(decode=True)",type(x.get_payload(decode=True)),x.get_payload(decode=True))
        # print("========\nx.get_payload(decode=True).decode()", type(x.get_payload(decode=True).decode()),x.get_payload(decode=True).decode())
        # print("========\nx.get_payload(decode=False).decode()", type(x.get_payload(decode=False).decode()),x.get_payload(decode=False).decode())

    # if x.get_content_type() == "text/plain":
    #     body = x.get_payload(decode=True)
    #     print(body)


imap_obj.close()

