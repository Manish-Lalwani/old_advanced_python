
class MyDict(dict):
    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        print("BottomBar Value Dictionary has been updated")


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




    # print("value_dict is {} type is {}".format(self.values_dict, type(self.values_dict)))
    # self.values_dict["ethernet"] = 1
    # wifi_dict["connected_to"] = 1

