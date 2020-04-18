# -*- coding:utf-8 -*-
# author:mingregister
# date：2020-04-11,22:24 

from abc import ABCMeta, abstractclassmethod

# Product
class Player():
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" %(self.face, self.body, self.arm, self.leg)

# Builder
class PlayerBuilder(metaclass=ABCMeta):
    @abstractclassmethod
    def build_face(self):
        pass

    @abstractclassmethod
    def build_body(self):
        pass

    @abstractclassmethod
    def build_arm(self):
        pass

    @abstractclassmethod
    def build_leg(self):
        pass

# ConcreteBuilder
class SexyGrilBuiler(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    # ConcreteBuilder的每一个方法理论上
    # 都应该要建造出产品的一某一部分？
    def build_face(self):
        self.player.face = "beautiful face"

    def build_body(self):
        self.player.body = "beautiful body"

    def build_arm(self):
        self.player.arm = "beautiful arm"

    def build_leg(self):
        self.player.leg = "beautiful leg"


# ConcreteBuilder
class MonsterBuiler(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "argly face"

    def build_body(self):
        self.player.body = "argly body"

    def build_arm(self):
        self.player.arm = "argly arm"

    def build_leg(self):
        self.player.leg = "argly leg"

# Director
class PlayerDirector():   # 用于控制组装顺序 
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player

# client 
# builder = SexyGrilBuiler()
builder = MonsterBuiler()
director = PlayerDirector()
p = director.build_player(builder)
print(p)