# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Fri Nov  1 23:07:47 2024
in Tims II Lab

@author: Stark
"""

from db_api import HomeMephiDB
from parser import HomeMephiParser

hmp = HomeMephiParser()
from secret import login, password
hmp.login(login, password)

from faker import Faker
from datetime import date as d
f_gen = Faker()

from random import random as ri

from time import sleep as zzz

from comands import ALPHABET





with HomeMephiDB(database="HomeMephi") as db:
    
    #students and groups
    '''group_ids = hmp.parse_Groups(hmp.ping_Groups())
    for i in group_ids.keys():
        print(group_ids[i],i)
        db.add_Group(group_ids[i], i)
        
        students = hmp.parse_Users_per_Group(hmp.ping_Users_per_Group(group_ids[i]))
        
        for st_id in students.keys():
            date = 2000+int(i[1:3])
            if i[0] == "А":date -= 18+4+3+1
            elif i[0] == "М":date -= 18+4+1
            else: date -= 18+1
            bd = f_gen.date_between(d(date,1,1), d(date+2,1,1))
            #print(st_id, students[st_id])
            db.add_Student(st_id, students[st_id], bd)
            db.add_Student_to_Group(st_id, group_ids[i])
        zzz(1.2+ri())
        #break
    #im tired to rollback every time it drops so
    db.commit()'''
    for letter in ALPHABET:
        teachers = hmp.parse_Teachers(hmp.ping_Teachers(letter))
        
        for schedule_id in teachers.keys():
            
            t_id, page = hmp.ping_Teacher(schedule_id)
            kaf, work_from = hmp.parse_Teacher(page)
            bd = f_gen.date_between(d(work_from-55,1,1), d(work_from-25,1,1))
            
            #print(t_id, teachers[schedule_id],kaf, work_from)
            db.add_Teacher(t_id, teachers[schedule_id], bd)
            zzz(1+ri())
    db.commit()
    
    
    
    
            


hmp.logout()