import subprocess
import my_beautify as mb

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



if __name__ == "__main__":

    mb.log_print(variable_name="suspend_machine",variable=suspend_machine("Dora456."))
    print("==================================================================\n")
