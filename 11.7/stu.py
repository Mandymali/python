#!/usr/bin/python
# -*- coding: UTF-8 -*-



class Student:

    stu_count = 0
    stu_count_wl163 = 0
    stu_count_wl161 = 0

    def __init__(self,stu_no,name,stu_class,male):
        self.stu_no = stu_no
        self.name = name
        self.stu_class = stu_class
        self.male = male
        Student.stu_count += 1
        if self.stu_class == "wl163":
            Student.stu_count_wl163 += 1
        elif self.stu_class == "wl161":
            student.stu_count_wl161 += 1


    def displayStuInfo(self):
        print "student number:",self.stu_no

    def displayCount(self):
        print "Count:",Student.stu_count
