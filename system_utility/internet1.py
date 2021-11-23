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

def get_available_ethernet_networks():
    pass




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

