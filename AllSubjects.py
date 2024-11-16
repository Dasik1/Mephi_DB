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
del login, password


from faker import Faker
from datetime import date as d
f_gen = Faker()

from random import random as r, randint as ri
from time import sleep as zzz




with HomeMephiDB(database="HomeMephi") as db:
    
    group_ids = db.get(table="StudyGroups", column = 'id')
    group_parced_ids = db.get_learning_groups()
    print(group_parced_ids)
    for g_id in group_ids:
        if g_id in group_parced_ids:
            print(g_id)
            continue
        
        lessons = hmp.parse_Shedule(hmp.ping_Shedule(g_id))
        
        for lesson in lessons:
            for teacher in lesson["teachers"]:
                #lesson:{'name':, 'weekday':, 'start_time':, 'location':,'teachers':<iter>, 'group':}
                
                
                
                #get kaf
                kaf, t_id = db.get_Teacher(teacher)
                if t_id is None:continue
                l_id = db.add_Subject(lesson["name"], kaf)
                
                db.add_TeachingSubject(t_id, l_id)
                db.add_StudyingSubject(g_id, l_id)
                
                a_id = db.add_Audience(lesson["location"])
                
                #now we are ready for shedule
                db.add_Shedule(l_id, t_id, g_id, a_id, lesson["weekday"],lesson["start_time"])
                
                
                
                #get marks -->>
                #get students
                students = db.get_Students_from_Group(g_id)
                
                for s_id in students:
                    grade = ri(60, 100)
                    m_id = db.add_Mark(l_id, grade)
                    
                    date = f_gen.date_between(d(2024,12,20), d(2025,2,1))
                    db.add_Student_Mark(s_id[0], m_id, t_id, date)#third leg

        
        

        
        
        
        #commit per group
        db.commit()
        zzz(2*r())
        
    pass





hmp.logout()