import imaplib
import pprint
import email

hostname = "outlook.office365.com"
username = "wirelineproject@pi108.com"
password = "RHryLbzux6VjRWFw"



imap_obj = imaplib.IMAP4_SSL(hostname)      #connect to server

imap_obj.login(username,password) #login to server

imap_obj.select(mailbox='inbox',readonly=True)  #readonly=False


tmp,email_serial_numbers = imap_obj.search(None,'unseen') #charset=None *criteria = 'ALL' #selecting all unseen emails other options are ALL

print(tmp,"\n\n\n",email_serial_numbers)

email_serial_number_list = email_serial_numbers[0].split() #spliting the email numbers to a byte list
#tmp,data = imap_obj.fetch(email_serial_number_list[0],'(RFC822)')
tmp,data = imap_obj.fetch(email_serial_number_list[0],'BODY.PEEK[]') #fetching a single email


email_message = email.message_from_bytes(data[0][1])  #further extracting email
#decoded_data = data[0][1].decode('utf-8')
#email_message = email.message_from_string(decoded_data)
#print(email_message,type(email_message),len(email_message))


#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@email_message.walk() length",len(email_message.walk()))
for i,x in enumerate(email_message.walk()): #traversing single mails section
    print(f"***********************************{i}*****************************")
    print("=======content type is",x.get_content_type(),"\n\n\n")
    #####output#####
    # ***********************************0*****************************
    # =======content type is multipart/alternative
    #
    #
    #
    # ***********************************1*****************************
    # =======content type is text/plain
    #
    #
    #
    # ***********************************2*****************************
    # =======content type is text/html
    print("=======content maintype is type is", x.get_content_maintype(), "\n\n\n")
    #print("=======content disposition is ",x.get("Content-Disposition"), "\n\n\n")
    print("=======content disposition is ", x.get_content_disposition(), "\n\n\n")
    # if x.get_content_type() == "text/plain":
    #     print(x)
    #     payload = x.get_payload(decode=True).decode()
    #     print("\n\npayload type is: ",type(payload))



    # if x.get_content_type() == "text/plain":
    #     body = x.get_payload(decode=True)
    #     print(body)


#imap_obj.close()

