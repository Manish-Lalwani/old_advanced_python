import subprocess
import my_beautify as mb

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



if __name__ == "__main__":
    mb.log_print(variable_name="firewall_status", variable=firewall_status())
    print("==================================================================\n")
    mb.log_print(variable_name="firewall_active", variable=firewall_active())
    print("==================================================================\n")
    mb.log_print(variable_name="firewall_deactivate", variable=firewall_deactivate())
    print("==================================================================\n")
