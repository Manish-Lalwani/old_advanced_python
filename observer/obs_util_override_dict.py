#https://stackoverflow.com/questions/2390827/how-to-properly-subclass-dict-and-override-getitem-setitem
class MyDict(dict):
    set_count =-1
    def __init__(self, **kwargs):
            dict.__init__(self, **kwargs)

        #
        # def __getitem__(self, key):
        #     val = dict.__getitem__(self, key)
        #     return val

    def __setitem__(self, key, val):
        if MyDict.set_count >7:
            old_val = dict.__getitem__(self,key)
            if old_val != val:
                dict.__setitem__(self, key, val)
                print("BottomBar Value Dictionary has been updated")
        else:
            dict.__setitem__(self, key, val)
            MyDict.set_count += 1
            print(self.set_count,key)
        #if val != None or type(val) != dict:
        # if dict.__getitem__(self, key) != val:



class BottomBarValueHolder:
    def __init__(self):
        self.values_dict = MyDict()
        wifi_dict = MyDict()
        self.values_dict["ethernet"] = None
        self.values_dict["wifi"] = wifi_dict
        wifi_dict["device_name"] = None
        wifi_dict["mac"] = None
        wifi_dict["status"] = None
        wifi_dict["connected_to"] = None
        self.values_dict["logged_user"] = None
        self.values_dict["vpn_status"] = None
        self.values_dict["firewall_status"] = None


if __name__ == "__main__":
    b1 = BottomBarValueHolder()
    print("value_dict is {} type is {}".format(b1.values_dict,type(b1.values_dict)))
    b1.values_dict["ethernet"] =1
    b1.values_dict["ethernet"] = 1

    b1.values_dict["ethernet"] = 2




    # print("value_dict is {} type is {}".format(self.values_dict, type(self.values_dict)))
    # self.values_dict["ethernet"] = 1
    # wifi_dict["connected_to"] = 1

