class Time():
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def show_time(self):
        print("%d:%d:%d")