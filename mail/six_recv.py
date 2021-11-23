import imaplib
import email
import os

output_dir = "./attached_files"
hostname = "outlook.office365.com"
username = "wirelineproject@pi108.com"
password = "RHryLbzux6VjRWFw"

email_data = {
    "from": None,
    "date": None,
    "subject": None,
    "body": None,
    "attached_file": []
}



imap_obj = imaplib.IMAP4_SSL(hostname)
imap_obj.login(username,password)
imap_obj.select(mailbox='inbox',readonly=True)

_,email_serial_numbers = imap_obj.search(None,'unseen')
email_serial_number_list = email_serial_numbers[0].split()
_,raw_mail_data = imap_obj.fetch(email_serial_number_list[2],'(RFC822)')

email_obj = email.message_from_bytes(raw_mail_data[0][1])

email_data["from"] = email_obj["From"]
email_data["date"] = email_obj["Date"]
email_data["subject"] = email_obj["Subject"]

for i,section in enumerate(email_obj.walk()):
    #body
    if section.get_content_type() == "text/plain":
        if section.get_payload(decode=False) == section.get_payload(decode=True).decode():
            print("yesy")
        body= section.get_payload(decode=False)
        email_data["body"] = body
    #file
    #if section.get_content_type() == "application"
    if section.get_content_maintype() != "multipart" and section.get_content_disposition():
        filename = section.get_filename()
        email_data["attached_file"].append(filename)
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        with open(output_dir +"/"+ filename,"w") as fp:
            fp.write(section.get_payload())


for key,val in email_data.items():
    print(key,":",val)
imap_obj.close()



#>>> complexSearch1 = '(SENTSINCE "01-May-2021" SUBJECT "Process File" UNSEEN)'
