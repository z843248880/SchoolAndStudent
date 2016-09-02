#!/usr/bin/env python
#coding:utf-8


#!/usr/bin/env python
#coding:utf-8

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.course = []
        self.students = []
        self.staffs = []
        self.class1 = []
    def addclass1(self,obj):
        self.class1.append(obj)
        
    def searchClass1(self):
        for i in self.class1:
            print(i.name,' ',i.period,' ',i.total_person)
    
    def addCourse(self,obj):
        self.course.append(obj)
   
    def searchCourse(self):
        for i in self.course:
            print(i.name)
    def stu_enroll(self,obj):
        self.students.append(obj)
        print('%s，注册完成，您选的课程是       %s   ，您需要缴纳 %s的学费，接下来进入选课系统。' % (obj.name,obj.cour_obj.name,obj.cour_obj.price))
        for i in self.class1:
            if i.course_obj.name == obj.cour_obj.name:
                print(i.name,' ',i.period,' ',i.total_person)
        class1 = input('请输入您要选择的班级：')
        obj.class1 = class1
        print('班级选择成功，以下是您的个人信息。')
        print('''
    姓名：%s
    性别:%s
    学号：%s
    课程名：%s
    班级名：%s
            ''' % (obj.name,obj.sex,obj.stu_id,obj.cour_obj.name,obj.class1))
        
    def hire_teacher(self,obj):
        self.staffs.append(obj)
        

class BAndC(object):
    def __init__(self,name,period):
        self.name = name
        self.period = period
    
class Course(BAndC):
    def __init__(self,name,period,price):
        super(Course,self).__init__(name, period)
        self.price = price

class Class1(BAndC):
    def __init__(self,name,period,total_person,course_obj):
        super(Class1,self).__init__(name, period)
        self.total_person = total_person
        self.course_obj = course_obj

class SchoolMember(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,sex,salary,cour_obj):
        super(Teacher,self).__init__(name, sex)
        self.salary = salary
        self.cour_obj = cour_obj
    def tell(self):
        print(self.name,self.sex,self.salary,self.cour_obj)
    def search_class(self):
        pass

class Student(SchoolMember):
    def __init__(self,name,sex,stu_id,cour_obj,class1=None,grade=60):
        super(Student,self).__init__(name, sex)
        self.stu_id = stu_id
        self.cour_obj = cour_obj
        self.class1 = class1
        self.grade = grade
    def tell(self):
        print(self.name,self.sex,self.stu_id,self.cour_obj,self.class1,self.grade)
    
        
sb = School('中日友好大学','北京')
sh = School('韩国大学','上海')

clinux = Course('linux','六个月','5500')
cpython = Course('python','八个月','9900')
cgo = Course('go','九个月','12000')

class1 = Class1('python一班','八个月','33',cpython)
class2 = Class1('python二班','八个月','23',cpython)
class3 = Class1('python三班','八个月','13',cpython)
class4 = Class1('linux一班','六个月','33',clinux)
class5 = Class1('linux二班','六个月','13',clinux)
class6 = Class1('linux三班','六个月','18',clinux)
class7 = Class1('go一班','九个月','22',cgo)
class8 = Class1('go二班','九个月','33',cgo)
class9 = Class1('go三班','九个月','44',cgo)

st1 = Student('呼呼','男',10001,clinux)
st2 = Student('啦啦','女',10002,cpython)

t1  = Teacher('词','男','3333',clinux)
t2  = Teacher('单','男','5555',cpython)
t3  = Teacher('章','男','7777',cgo)

sb.hire_teacher(t1)
sb.hire_teacher(t2)
sh.hire_teacher(t3)


sb.addCourse(clinux)
sb.addCourse(cpython)
sh.addCourse(cgo)

sb.addclass1(class1)
sb.addclass1(class2)
sb.addclass1(class3)
sb.addclass1(class4)
sb.addclass1(class5)
sb.addclass1(class6)
sh.addclass1(class7)
sh.addclass1(class8)
sh.addclass1(class9)


sb.stu_enroll(st1)




    





































# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def animal_talk(obj):
#         obj.talk()
# class cat(Animal):
#     def talk(self):
#         print(self.name)
#         
# class dog(Animal):
#     def talk(self):
#         print(self.name)
#         
# c1 = cat('c')
# d1 = dog('d')
# 
# Animal.animal_talk(c1)
# Animal.animal_talk(d1)


























# class A:
#     pass
# #     def __init__(self):
# #         print('A')
# class B(A):
#     pass
# #     def __init__(self):
# #         print('B')
# 
# class C(A):
#     pass
# #     def __init__(self):
# #         print('C')
# 
# class D(B,C):
#     pass
# #     def __init__(self):
# #         print('D')
# 
# d1 = D()
