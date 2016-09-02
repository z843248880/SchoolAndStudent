#!/usr/bin/env python
#coding:utf-8

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def eat(self):
        print('%s is eting.' % self.name)
    
    def sleep(self):
        print('%s is age.' % self.age)
        
class Man(People):
    def __init__(self,name,age,money):
        People.__init__(self, name, age)
        super(Man,self).__init__(name, age)
        self.money = money
    def man(self):
        print('this is man,%s' % self.name)
        
    def sleep(self):
        print('chong xie sleep')
    
    def eat(self):
        People.eat(self)
        print('chongxie eat.')
class Woman(People):
    def woman(self):
        print('this is woman,%s' % self.age)

m1 = Man('ci',25)
m1.eat()
m1.sleep()
m1.man()
print('---------------------------------')
w1 = Woman('wwww',33)
w1.eat()
w1.sleep()
w1.woman()
        
    