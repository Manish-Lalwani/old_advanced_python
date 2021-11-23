class ObjectHoldingTheValue:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._callbacks = []

    @property       #getter
    def value(self):
        return self._value

    @value.setter       #setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        self._notify_observers(old_value, new_value)

    def _notify_observers(self, old_value, new_value):
        for callback in self._callbacks:
            callback(old_value, new_value)

    def register_callback(self, callback):
        self._callbacks.append(callback)





def print_if_change_greater_than_500(old_value, new_value):
    if abs(old_value - new_value) > 500:
        print(f'The value changed by more than 500 (from {old_value} to {new_value})')



if __name__ == "__main__":
    holder = ObjectHoldingTheValue()
    holder.register_callback(print_if_change_greater_than_500)
    holder.value = 7    # nothing is printed
    holder.value = 70   # nothing is printed
    holder.value = 700  # a message is printed