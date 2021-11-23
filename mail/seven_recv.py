from typing import Dict, List, Tuple, Any, TypeVar, Optional, Union, Callable
import imaplib
import email
import os
#from logger import log
from logger import log,log1
import traceback
import pickle
#from imap_tools import Q, AND, OR, NOT


ImaplibImap4SSL = TypeVar('imaplib.IMAP4_SSL')
EmailMessageMesage = TypeVar('email.message.Message')

class EmailFetcher:
    def __init__(self,hostname="outlook.office365.com",username="wirelineproject@pi108.com",password="RHryLbzux6VjRWFw"):
        self.hostname:str = hostname
        self.username:str = username
        self.password:str = password

        self.imap_obj:Optional[ImaplibImap4SSL] = None

        self.successfully_fetched_email_ref:List[bytes] = []
        self.failed_fetched_email_ref:List[bytes] = []


        self.imap_object_init()

    def imap_object_init(self) -> ImaplibImap4SSL:
        """LOGIN TO IMAP SERVER AND ASSIGNS TO CLASS IMAP OBJECT"""
        imap_obj = imaplib.IMAP4_SSL(self.hostname)
        imap_obj.login(user=self.username,password=self.password)
        self.imap_obj = imap_obj

    # def get_email_reference(self,mailbox="inbox",readonly=True,charset=None,criteria='unseen') -> List[bytes]:
    #     """FETCHES EMAIL REFERENCE NUMBER AND RETURNS IT"""
    #     self.imap_obj.select(mailbox=mailbox, readonly=readonly)
    #     email_references_byte_string:List[bytes] = self.imap_obj.search(charset,criteria)[1]
    #     email_references_bytes_list:List[bytes] = email_references_byte_string[0].split()
    #
    #     return email_references_bytes_list
    #complexSearch1 = '(SENTSINCE "01-May-2021" SUBJECT "Kindly" UNSEEN)'

    def get_email_reference(self,mailbox="inbox",readonly=False,charset=None,section='UNSEEN',sent_since="01-Apr-2021",subject="Kindly") -> List[bytes]:
        """FETCHES EMAIL REFERENCE NUMBER AND RETURNS IT"""
        self.imap_obj.select(mailbox=mailbox, readonly=readonly)
        criteria = f"""(SENTSINCE "{sent_since}" SUBJECT "{subject}" {section})"""
        print(f"\n\n\n\n{criteria}\n\n\n\n")
        email_references_byte_string:List[bytes] = self.imap_obj.search(charset,criteria)[1]
        email_references_bytes_list:List[bytes] = email_references_byte_string[0].split()

        return email_references_bytes_list

    def mark_email_unread(self,email_references_bytes_list):
        for x in email_references_bytes_list:
            self.imap_obj.uid('STORE', x, '+FLAGS', 'UNSEEN')  # marking the mail as seen


    def get_email_objects(self,email_references_bytes_list) ->List[EmailMessageMesage]:
        """RETURNS ALL EMAIL OBJECTS IN A LIST"""
        raw_email_data:List[List[Tuple[bytes]]] = []
        email_obj_list:List[EmailMessageMesage] = []
        for i,ref in enumerate(email_references_bytes_list):
            raw_email_data.append(self.imap_obj.fetch(ref,'(RFC822)')[1])
            email_obj_list.append(email.message_from_bytes(raw_email_data[i][0][1]))
        return email_obj_list

    def get_email_detail_and_attachments(self):
        """RETURNS A PARTICULAR EMAIL DETAIL AND SAVES IT ATTACHMENTS"""
        pass

    def get_emails_details_and_attachments(self,email_obj_list,email_ref,parent_output_dir="./attachment_files"):
        """RETURNS ALL EMAIL DETAILS AND SAVES ALL ATTACHMENTS"""
        try:
            email_details_list:List[Dict[str:Any]] = []
            for i,mail in enumerate(email_obj_list):
                email_details: Dict[str:Any] = {
                                                    "from": mail["from"],
                                                    "date": mail["date"],
                                                    "subject": mail["subject"],
                                                    "body": None,
                                                    "attached_files": [],
                                                    "attached_files_path":[],
                                                    "email_ref":[]
                                                }
                output_dir:str = f"{parent_output_dir}/{email_details['from']}_{email_details['date']}/"
                email_details["email_ref"].append(email_ref[i])  # appending email ref number to dict
                for j,section in enumerate(mail.walk()):
                    #body
                    if section.get_content_type() == "text/plain" and section.get_content_disposition() == None:
                        body = section.get_payload(decode=False)
                        email_details["body"] = body
                    #file
                    if section.get_content_maintype() != "multipart" and section.get_content_disposition():
                        filename = section.get_filename()
                        email_details["attached_files"].append(filename)
                        file_path = output_dir + "/" + filename
                        email_details["attached_files_path"].append(file_path)
                        if not os.path.exists(output_dir): os.makedirs(output_dir)
                        with open(file_path, "wb") as fp:
                            fp.write(section.get_payload(decode=True))
                email_details_list.append(email_details)
                self.successfully_fetched_email_ref.append(email_ref[i])
                self.imap_obj.uid('STORE', email_ref[i], '+FLAGS', '\SEEN')    #  marking the mail as seen
            return email_details_list
        except Exception as e:
            self.failed_fetched_email_ref(email_ref[i])
            log.error(traceback.format_exc())





if __name__ == "__main__":

    ef = EmailFetcher()
    email_reference_list = ef.get_email_reference()
    print("email_reference_list",email_reference_list)
    ef.mark_email_unread(email_reference_list)
    email_obj_list = ef.get_email_objects(email_references_bytes_list=email_reference_list)
    print(email_obj_list[0]["from"])
    email_detail_list =ef.get_emails_details_and_attachments(email_obj_list,email_ref=email_reference_list)

    #print(len(email_detail_list))
    for x in email_detail_list:
        for y,z in x.items():
            print(y,":",z)




