is_wifi_on = 0

class Publisher:
    """OBSERVABLE"""
    def __init__(self):
        self.subscribers_dict = dict()
    def register(self,subscriber_name,subs_callback_func_name):
        self.subscribers_dict[subscriber_name] = subs_callback_func_name
    def unregister(self,subscriber_name):
        del self.subscribers_dict[subscriber_name]
    def send(self,message):
            for subscriber,callback in self.subscribers_dict.items():
                callback(message)


class SubscriberOne:
    """OBSERVER / Listener"""
    def recieve(self,message):
        print("Recieved message from Publisher:",message)


class SubscriberTwo:
    """OBSERVER / Listener"""
    def listen(self,message):
        print("Recieved message from Publisher:",message)
    def recieve(self):
        print("Recieved message from Publisher:", message)

##############################################################################################



class BottomBarValueHolder:
    def __init__(self):
        self.values_dict = {
        'ethernet': None,
        'wifi': {
            'device_name': None,
             'mac': None,
            'status': None,
            'connecte_to':None
            },
        'logged_user': None,
        'vpn_status': None,
        'firewall_status': None
        }








if __name__ == "__main__":

    publisher_obj = Publisher()
    alice = SubscriberOne()
    tom = SubscriberTwo()

    publisher_obj.register(alice,alice.recieve)
    publisher_obj.send(" Morning Folks!!!")
    publisher_obj.register(tom, tom.listen)
    publisher_obj.send(" Evening Folks!!!")