# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:30:30 2024

@author: excal
"""
#Humanクラスに、以下条件の出力を行うcheck_adultメソッドを追加して記載する
#1, ageが20以上の場合、大人であること
#2, そうでない場合に大人でないこと

#クラスHumanを定義
class Human:
    #__init__メソッドは、新しいHumanオブジェクトの作成に当たり、呼び出される。
    # age と　name を受け取り、、それぞれの属性に値を設定する
    def __init__(self, name, age):
        self.name = name
        self.age = age

#check_adultメソッドの作成
#check_adultメソッドは,ageが２０以上の場合に「大人である」
#check_adultメソッドは,ageがそれ以外の場合に「大人でない」

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です")
        else:
            print(f"{self.name}は大人ではありません")

# Humanクラスのインスタンスを作成　と　リストへの追加
#　person1,person2,person3　の　３つのHumanクラスのインスタンスを作成。
#　それぞれに、名前と年齢を設定する
person1 = Human("侍太郎", 25)
person2 = Human("侍貴子", 18)
person3 = Human("侍敏弘", 30)

# リストに追加
human = [person1, person2, person3]

# リストの要素数分だけcheck_adultメソッドを呼び出す
# forループを使って、リスト内の各Humanオブジェクトに対してcheck_adultメソッドを呼び出す
for person in human:
    person.check_adult()
