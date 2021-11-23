import subprocess
import my_beautify as mb

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



if __name__ == "__main__":
    mb.log_print(variable_name="list_vpns", variable=list_vpns())
    print("==================================================================\n")
    mb.log_print(variable_name="active_vpn", variable=active_vpn())
    print("==================================================================\n")
    mb.log_print(variable_name="disconnect_vpn", variable=disconnect_vpn())
    print("==================================================================\n")
