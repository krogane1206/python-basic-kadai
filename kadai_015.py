#名前(name)と年齢(age)の属性を持つHumanクラスを作成
#nameとageを標準出力する(print)するメソッド(printinfo)を追加してください

class Human():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print(f"名前： {self.name}")
        print(f"年齢: {self.age}")

person1 = Human(name="太郎", age = 25)
person1.printinfo()

person2 = Human(name="花子", age = 30)
person2.printinfo()