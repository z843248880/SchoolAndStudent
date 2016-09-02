#!/usr/bin/env python
#coding:utf-8

class School(object):
    staffs = {}
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.course = []
        self.students = []       
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
        class_list = []
        count = 0
        course_name = ''
        for i in obj.cour_obj:
            print('%s，注册完成，您选的课程是       %s   ，您需要缴纳 %s的学费，接下来进入选课系统。' % (obj.name,i.name,i.price))
        for j in self.class1:
            for k in obj.cour_obj:                 
                if j.course_obj.name == k.name:
                    if course_name == j.course_obj.name[0:1]:
                        print(j.name,' ',j.period,' ',j.total_person)
                    else:
                        print(j.name,' ',j.period,' ',j.total_person)
                        course_name = j.course_obj.name[0:1]
                        count += 1
        a = 0
        while a < count:
            class_input = input('请输入您要选择的班级：')
            class_list.append(class_input)    
            a += 1
        obj.class1 = class_list
        print('班级选择成功，以下是您的个人信息。')
        print('''
    姓名：%s
    性别:%s
    学号：%s
    课程名：%s
    班级名：%s
            ''' % (obj.name,obj.sex,obj.stu_id,[x.name for x in obj.cour_obj],obj.class1))
        
    def hire_teacher(self,obj,*obj1):
        afk = []
        for i in obj1:
            afk.append(i.name)
        self.staffs[obj.name] = afk
        
