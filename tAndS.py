#!/usr/bin/env python
#coding:utf-8

import re,pickle,sys
import School

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
            if int(stu_num_input) == int(i.stu_id):
                stu_grade_input = input('请输入修改后分数：')
                i.grade = int(stu_grade_input)
                print('修改完成，如下：')
                print('''
姓名：%s,性别：%s,学号：%s,课程：%s,班级：%s,分数：%s'''
                     % (i.name,i.sex,i.stu_id,[x.name for x in i.cour_obj],i.class1,i.grade))

class Student(SchoolMember):
    def __init__(self,name,sex,stu_id,cour_obj,class1=None,grade=60):
        super(Student,self).__init__(name, sex)
        self.stu_id = stu_id
        self.cour_obj = cour_obj
        self.class1 = class1
        self.grade = grade
    def tell(self):
        print(self.name,self.sex,self.stu_id,[x for x in self.cour_obj],self.class1,self.grade)

def ct(obj_name):
    obj = obj_name
    ming = input('请输入您的姓名：')
    sex = input('请输入您的性别：')
    gongzi = input('请输入您的工资：')
    kecheng = input('请输入您的课程')
    obj = Teacher(ming,sex,gongzi,kecheng)
    with open(obj_name,'wb') as tf:
        pickle.dump(obj,tf)
def rt(obj_name):
    with open(obj_name,'rb') as tf:
        obj_name = pickle.load(tf)
    return obj_name
t1 = rt('t1')
t2 = rt('t2')
t3 = rt('t3')


def cc(obj_name):
    obj = obj_name
    ming = input('请输入您的课程名：')
    period = input('请输入课程周期：')
    price = input('请输入课程价格：')
    obj = Course(ming,period,price)
    with open(obj_name,'wb') as tf:
        pickle.dump(obj,tf)
def rc(obj_name):
    with open(obj_name,'rb') as tf:
        obj_name = pickle.load(tf)
    return obj_name

clinux = rc('clinux')
cpython = rc('cpython')
cgo = rc('cgo')


def cclass(obj_name):
    obj = obj_name
    list_input = input('请输入按此格式输入：班级名，班级周期，班级人数，班级的课程')
    
#     ming = input('请输入您的班级名：')
#     period = input('请输入班级周期：')
#     total_person = input('请输入班级人数：')
#     course_name = input('请输入班级的课程：')
    ming = list_input.split(',')[0]
    period = list_input.split(',')[1]
    total_person = list_input.split(',')[2]
    course_name = list_input.split(',')[3]
    if course_name == 'clinux':
        obj = Class1(ming,period,total_person,clinux)
    elif course_name == 'cpython':
        obj = Class1(ming,period,total_person,cpython)
    elif course_name == 'cgo':
        obj = Class1(ming,period,total_person,cgo)
    else:
        print('没有这个课程，再见')
        sys.exit()
    with open(obj_name,'wb') as tf:
        pickle.dump(obj,tf)
def rclass(obj_name):
    with open(obj_name,'rb') as tf:
        obj_name = pickle.load(tf)
    return obj_name
# cclass('python1')
python1 = rclass('python1')
# cclass('python2')
python2 = rclass('python2')
# cclass('python3')
python3 = rclass('python3')
# cclass('linux1')
linux1 = rclass('linux1')
# cclass('linux2')
linux2 = rclass('linux2')
# cclass('linux3')
linux3 = rclass('linux3')
# cclass('go1')
go1 = rclass('go1')
# cclass('go2')
go2 = rclass('go2')
# cclass('go3')
go3 = rclass('go3')


def cs(obj_name):
    obj = obj_name
    cor_list = ['[clinux]','[cpython]','[cgo]','[clinux,cpython]','[clinux,cgo]','[cpython,cgo]','[clinux,cpython,cgo]']
    print('(包含的课程如下，直接复制粘贴即可)。')
    for i in cor_list:
        print(i)
            
    list_input = input('请输入按此格式输入：姓名，性别，学号，[要选择的课程]：')
    ming = list_input.split(';')[0]
    sex = list_input.split(';')[1]
    stu_nu = list_input.split(';')[2]
    course_list = list_input.split(';')[3]
    if course_list == '[clinux]':
        obj = Student(ming,sex,stu_nu,[clinux])
    elif course_list == '[cpython]':
        obj = Student(ming,sex,stu_nu,[cpython])
    elif course_list == '[cgo]':
        obj = Student(ming,sex,stu_nu,[cgo])
    elif course_list == '[clinux,cpython]':
        obj = Student(ming,sex,stu_nu,[clinux,cpython])
    elif course_list == '[clinux,cgo]':
        obj = Student(ming,sex,stu_nu,[clinux,cgo])
    elif course_list == '[cpython,cgo]':
        obj = Student(ming,sex,stu_nu,[cpython,cgo])
    elif course_list == '[clinux,cpython,cgo]':
        obj = Student(ming,sex,stu_nu,[clinux,cpython,cgo])
    else:
        print('您输入的课程不存在，再见。')
        sys.exit()
    with open(obj_name,'wb') as ft:
        pickle.dump(obj,ft)
def rs(obj_name):
    with open(obj_name,'rb') as ft:
        obj_name = pickle.load(ft)
    return obj_name
# cs('st1')
st1 = rs('st1')
# cs('st2')
st2 = rs('st2')

list_class1_obj = [python1,python2,python3,linux1,linux2,linux3,go1,go2,go3]
      
sb = School.School('中日友好大学','北京')
sh = School.School('韩国大学','上海')

sb.hire_teacher(t1,linux1,linux2,linux3)
sb.hire_teacher(t2,python1,python2,python3)
sh.hire_teacher(t3,go1,go2,go3)


sb.addCourse(clinux)
sb.addCourse(cpython)
sh.addCourse(cgo)

sb.addclass1(python1)
sb.addclass1(python2)
# print('--------start')
# print(python1.course_obj)
# print('--------stop')
sb.addclass1(python3)
sb.addclass1(linux1)
sb.addclass1(linux2)
sb.addclass1(linux3)
sh.addclass1(go1)
sh.addclass1(go2)
sh.addclass1(go3)



list_stu_obj = [st1,st2]

sb.stu_enroll(st1)
sb.stu_enroll(st2)

t1.choice_class()
t2.change_grade()



# with open('t1','rb') as tf:
#     t1 = pickle.load(tf)

# t1  = Teacher('词','男','3333',clinux)
# t2  = Teacher('单','男','5555',cpython)
# t3  = Teacher('章','男','7777',cgo)
# clinux = Course('linux','六个月','5500')
# cpython SchooMembere('python','八个月','9900')
# cgo = CSchooMembergo','九个月','12000')




# python1('python1班','八个月','33',cpython)
# python2 = Class1('python2班','八个月','23',cpython)
# python3 = Class1('python3班','八个月','13',cpython)
# linux1 = Class1('linux1班','六个月','33',clinux)
# linux2 = Class1('linux2班','六个月','13',clinux)
# linux3 = Class1('linux3班','六个月','18',clinux)
# go1 = Class1('go1班','九个月','22',cgo)
# go2 = Class1('go2班','九个月','33',cgo)
# go3 = Class1('go3班','九个月','44',cgo)


# st1 = Student('呼呼','男',10001,[clinux,cpython])
# st2 = Student('啦啦','女',10002,[cpython])

    