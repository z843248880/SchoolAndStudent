#!/usr/bin/env python
#coding:utf-8

import re,pickle
import School




class SchoolMember(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def tell(self):
        pass
    
class Student(SchoolMember):
    def __init__(self,name,sex,stu_id,cour_obj,class1=None,grade=60):
        super(Student,self).__init__(name, sex)
        self.stu_id = stu_id
        self.cour_obj = cour_obj
        self.class1 = class1
        self.grade = grade
    def tell(self):
        print(self.name,self.sex,self.stu_id,[x for x in self.cour_obj],self.class1,self.grade)


class Teacher(SchoolMember):
    def __init__(self,name,sex,salary,cour_obj):
        super(Teacher,self).__init__(name, sex)
        self.salary = salary
        self.cour_obj = cour_obj
    def tell(self):
        print(self.name,self.sex,self.salary,self.cour_obj)
    def choice_class(self):
        dict_tea = School.School.staffs
        for i in dict_tea[self.name]:
            print(i)
        choice_class = input('请输入您要进入的班级：')
        class_name_num = re.search(r'(\w+)(\d+)', choice_class).group(1) + re.search(r'(\w+)(\d+)', choice_class).group(2)
        for i in list_class1_obj:
            list_class1_obj_name = re.search(r'(\w+)(\d+)', i.name).group(1) + re.search(r'(\w+)(\d+)', i.name).group(2)
            if class_name_num == list_class1_obj_name:
                print('''
                                                                                    现在进入%s,
                                                                                    学习周期是%s,
                                                                                    总人数是%s''' 
                    % (i.name,i.period,i.total_person))
        print('以下是该班学生成员信息：',end='')        
        for i in list_stu_obj:
            for j in i.class1:
                if j == choice_class:
                    print('''
姓名：%s,性别：%s,学号：%s,课程：%s,班级：%s,分数：%s'''
                     % (i.name,i.sex,i.stu_id,[x.name for x in i.cour_obj],i.class1,i.grade),end='')
    def change_grade(self):
        stu_num_input = input('请输入想要修改分数的学号：')
        for i in list_stu_obj:
            if int(stu_num_input) == i.stu_id:
                stu_grade_input = input('请输入修改后分数：')
                i.grade = int(stu_grade_input)
                print('修改完成，如下：')
                print('''
姓名：%s,性别：%s,学号：%s,课程：%s,班级：%s,分数：%s'''
                     % (i.name,i.sex,i.stu_id,[x.name for x in i.cour_obj],i.class1,i.grade))
                
def ct(obj_name):
    obj = obj_name
    ming = input('请输入您的姓名：')
    sex = input('请输入您的性别：')
    gongzi = input('请输入您的工资：')
    kecheng = input('请输入您的课程')
    obj = SchoolMember(ming,sex,gongzi,kecheng)
    with open(obj_name,'wb') as tf:
        pickle.dump(obj,tf)
def rt(obj_name):
    with open(obj_name,'rb') as tf:
        obj_name = pickle.load(tf)
    return obj_name
# ct('t1')
t1 = rt('t1')
# ct('t2')
t2 = rt('t2')
# ct('t3')
t3 = rt('t3')