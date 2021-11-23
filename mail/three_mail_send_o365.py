from O365 import Account

credentials = ('c9fbf432-3392-4b1d-b0d6-ca1c2586b2b2', 'vAmyyau-SjO~81~U7md90x4NEYajM7k~uq')

account = Account(credentials)
m = account.new_message()
m.to.add('mlalwani@xcaliberinfotech.com')
m.subject = 'Testing!'
m.body = "Success"
m.send()