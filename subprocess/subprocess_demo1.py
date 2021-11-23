#ref https://stackabuse.com/executing-shell-commands-with-python/



import subprocess

# list_dir = subprocess.Popen(["ls", "-l"])
# res =list_dir.wait()
# print(res)


# list_dir = subprocess.Popen(["nethogs", "-v","3"])
# res =list_dir.wait()
# print(res)




# nmcli d wifi connect GR-1.2 password griffynwifiXC12!@#
# nmcli d wifi connect GR-1.2 password 'griffynwifiXC12!@#'


# #wifi connect
# sp1 = subprocess.Popen(["nmcli","d","wifi","connect","GR-1.2","password","griffynwifiXC12!@#"])
# res = sp1.wait()
# print("result is",res)

# #suspend
# sp1 = subprocess.Popen(["sudo","pm-suspend"])
# sp1.communicate(input="Dora456.")
# res = sp1.wait()
# print("result is",res)


#list all human users
#cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1
#sp1 = subprocess.Popen(["cut","-d:","-f1,3","/etc/passwd","|","egrep","':[0-9]{4}$'","|","cut","-d:","-f1"])
##sp1 = subprocess.Popen(["cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1"],shell=True)
#out,err = sp1.communicate() #for saving output to vaiable out 
##res = sp1.wait()
##print("result is",res)



# #getting current username:
# sp1 = subprocess.Popen(["whoami"])
# out,err = sp1.communicate()
# res = sp1.wait()
# print("result is",res)


# #user logout with prompt
# #gnome-session-quit
# sp1 = subprocess.Popen(["gnome-session-quit"])
# res = sp1.wait()
# print("result is",res)


# # #listing all vpn's
# #nmcli con show | grep -i vpn
# sp1 = subprocess.Popen(["nmcli con show | grep -i vpn | awk '{print $1}' "],shell=True)
# out,err = sp1.communicate()
# res = sp1.wait()
# print("result is",res)


# #connecting to vpn
# #nmcli con up id  Xcaliber_VPN passwd-file xcal_pass
# vpn_name = "Xcaliber_VPN"
# password_file = "xcal_pass"
# temp_str = "nmcli con up id " + vpn_name + " passwd-file " + password_file
# sp1 = subprocess.Popen([temp_str],shell=True)
# res = sp1.wait()
# print("result is",res)


# #active vpn 
# #nmcli con show --active | grep -i vpn
# sp1 = subprocess.Popen(["nmcli con show --active | grep -i vpn | awk '{print $1, $4}'"],shell=True,stdout=subprocess.PIPE)
# out,err = sp1.communicate()
# res = sp1.wait()
# print("result is",res)


# #deactivate vpn
# #nmcli con down id ConnectionName
# vpn= 'Xcaliber_VPN'
# temp_str = "nmcli con down id " + vpn_name
# sp1 = subprocess.Popen([temp_str],shell=True,stdout=subprocess.PIPE)
# res = sp1.wait()
# print("result is",res)


# # sudo ufw status
# sp1 = subprocess.Popen(["sudo ufw status"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# out,err = sp1.communicate()
# res = sp1.wait()
# print("result is",res)
# print(out)


# #Enable wifi 
# # nmcli radio wifi on
# sp1 = subprocess.Popen(["nmcli radio wifi on"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# status_code = sp1.wait()
# print("Executed with status code",status_code)


#Enable wifi 
# nmcli radio wifi on
sp1 = subprocess.Popen(["nmcli radio wifi"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
res,error = sp1.communicate()
status_code = sp1.wait()
print("Executed with status code",status_code)
print("Result is:",res)

