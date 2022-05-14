class Students():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s "%(name,city))
    def speak(self):
        print("我在慢慢学Python")
stu1=Students("mary","上海")
stu1.speak()