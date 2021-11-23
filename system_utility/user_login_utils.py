import subprocess
import my_beautify as mb

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
    user, err = sp1.communicate()
    res = sp1.wait()
    print("Executed with error:", res)
    print("User is:", user)
    return user



if __name__ == "__main__":

    mb.log_print(variable_name="list_human_users",variable=list_human_users())
    print("==================================================================\n")
    mb.log_print(variable_name="current_logged_user", variable=current_logged_user())
    print("==================================================================\n")
    mb.log_print(variable_name="logout", variable=logout())
    print("==================================================================\n")

