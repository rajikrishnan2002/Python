class time:
    def __init__(self,hour,minute,seconds):
        self.__h=hour
        self.__m=minute
        self.__s=seconds
    def __add__(self,a):
        hour=self.__h+a.__h
        minute=self.__m+a.__m
        second=self.__s+a.__s
        print("the sum of 2 time is: ",hour,minute,second)
a1=time(10,3,3)
a2=time(12,5,3)
print(a1+a2)
