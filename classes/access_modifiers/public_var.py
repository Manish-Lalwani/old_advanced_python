class A:
    def __init__(self,name,surname):
        #public variables
        self.name = name
        self.surname = surname


if __name__ == "__main__":
    obj = A(name="Suresh",surname="Raina")
    print(f"First  is:{obj.name},Last  is:{obj.surname} ")
