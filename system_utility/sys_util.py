from wifi import Cell, Scheme
import wifi
import os
import subprocess
import requests
import my_beautify as mb

################Internet################
def get_all_interface_names():
    return os.listdir('/sys/class/net/')

def get_wifi_interface():
    wifi_list = []
    all_list = os.listdir('/sys/class/net/')
    for x in all_list:
        if x[0] =="w":
            wifi_list.append(x)
    return wifi_list

def get_available_wifi_networks(interface):
    wifilist = []
    cells = wifi.Cell.all(interface)

    for cell in cells:
        wifilist.append(str(cell).replace('Cell(','')[:-1])
    print(wifilist)
    return wifilist

def find_from_saved_wifi_networks(interface,ssid):
    cell = wifi.Scheme.find(interface,ssid)
    if cell:
        return cell
    else:
        return False

def find_from_search_wifi_networks(interface,ssid):
    wifilist = get_available_wifi_networks(interface)

    if ssid in wifilist:
        return ssid
    else:
        return False

def wifi_status():
    sp1 = subprocess.Popen(["nmcli radio wifi"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res, error = sp1.communicate()
    status_code = sp1.wait()
    print("Executed with status code", status_code)
    print("Result is:", res)

def wifi_turn_on():
    sp1 = subprocess.Popen(["nmcli radio wifi on"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    status_code = sp1.wait()
    print("Executed with status code", status_code)
    return status_code

def wifi_turn_of():
    sp1 = subprocess.Popen(["nmcli radio wifi off"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    status_code = sp1.wait()
    print("Executed with status code", status_code)
    return status_code

def wifi_network_connect(wifi_ap_name,password):
    sp1 = subprocess.Popen(["nmcli", "d", "wifi", "connect", wifi_ap_name, "password", "griffynwifiXC12!@#"])
    res = sp1.wait()
    print("result is", res)

def internet_check(url="http://google.com"):
    try:
        requests.head(url)
        print("Success")
        return 0
    except requests.ConnectionError as e:
        print(e)
        return 1
################END################


################Machine################
def suspend_machine(password):
    sp1 = subprocess.Popen(["sudo", "pm-suspend"])
    sp1.communicate(input=password)
    res = sp1.wait()
    print("result is", res)
    return 0

def shutdown_machine(password):
    sp1 = subprocess.Popen(["sudo", "init","0"])
    sp1.communicate(input=password)
    res = sp1.wait()
    print("result is", res)
    return 0

def restart_machine(password):
    sp1 = subprocess.Popen(["sudo", "init","6"])
    sp1.communicate(input=password)
    res = sp1.wait()
    print("result is", res)
    return 0
################END################


################User################
def list_human_users():
    sp1 = subprocess.Popen(["cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1"], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    users, err = sp1.communicate()
    res = sp1.wait()
    print("Executed with error:", res)
    print("Users are:",users)
    return users

def current_logged_user():
    sp1 = subprocess.Popen(["whoami"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    user, err = sp1.communicate()
    res = sp1.wait()
    print("Executed with error:", res)
    print("User is:", user)
    return user

def logout():
    sp1 = subprocess.Popen(["gnome-session-quit"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #user, err = sp1.communicate()
    res = sp1.wait()
    print("Executed with error:", res)
    print("User is:", user)
    return user
################END################


################VPN################
def list_vpns():
    sp1 = subprocess.Popen(["nmcli con show | grep -i vpn | awk '{print $1}' "], shell=True)
    vpn_list, err = sp1.communicate()
    res = sp1.wait()
    print("result is", res)
    return vpn_list

def vpn_connect(vpn_name,password_file):
    temp_str = "nmcli con up id " + vpn_name + " passwd-file " + password_file
    sp1 = subprocess.Popen([temp_str], shell=True)
    res = sp1.wait()
    print("result is", res)

def active_vpn():
    sp1 = subprocess.Popen(["nmcli con show --active | grep -i vpn | awk '{print $1}'"], shell=True,
                           stdout=subprocess.PIPE)
    active_vpn, err = sp1.communicate()
    res = sp1.wait()
    print("result is", res)
    return active_vpn

def disconnect_vpn(vpn_name):
    temp_str = "nmcli con down id " + vpn_name
    sp1 = subprocess.Popen([temp_str], shell=True, stdout=subprocess.PIPE)
    res = sp1.wait()
    print("result is", res)
################END################


################Firewall################
def firewall_status():
    sp1 = subprocess.Popen(["sudo ufw status"], shell=True, stdout=subprocess.PIPE)
    out, err = sp1.communicate()
    res = sp1.wait()
    print("result is", res)
    status = str(out)
    return status

def firewall_active():
    sp1 = subprocess.Popen(["sudo ufw enable"], shell=True, stdout=subprocess.PIPE)
    out, err = sp1.communicate()
    res = sp1.wait()
    print("result is", res)
    status = str(out)
    return status

def firewall_deactivate():
    sp1 = subprocess.Popen(["sudo ufw disable"], shell=True, stdout=subprocess.PIPE)
    out, err = sp1.communicate()
    res = sp1.wait()
    print("result is", res)
    status = str(out)
    return status
################END################




if __name__ == "__main__":

    mb.log_print(variable_name="get_all_interface_names",variable=get_all_interface_names())
    print("==================================================================\n")
    mb.log_print(variable_name="get_wifi_interface", variable=get_wifi_interface())
    print("==================================================================\n")
    mb.log_print(variable_name="get_available_wifi_networks", variable=get_available_wifi_networks('wlp2s0'))
    print("==================================================================\n")
    mb.log_print(variable_name="find_from_saved_wifi_networks", variable=find_from_saved_wifi_networks('wlp2s0','ssid=GR-1.2'))
    print("==================================================================\n")
    mb.log_print(variable_name="find_from_search_wifi_networks", variable=find_from_search_wifi_networks('wlp2s0','ssid=GR-1.2'))
    print("==================================================================\n")
    mb.log_print(variable_name="wifi_network_connect", variable=wifi_network_connect('GR-1.2',"'griffynwifiXC12!@#'"))
    mb.log_print(variable_name="internet_check", variable=internet_check())
    print("==================================================================\n")
