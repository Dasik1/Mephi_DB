# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Nov 30 13:06:16 2024
in Tims II Lab

@author: Stark
"""






from db_api import HomeMephiDB


from faker import Faker
from datetime import date as d
from datetime import time as t
f_gen = Faker("ru_RU")

from random import random as r
from random import randint as rint
from time import time as now
from time import sleep as zzz


types = [
    "Базы данных и экспертные системы"
    ]


with HomeMephiDB(database="HomeMephi") as db:
    
    s_ids = db.get(table="Students",column="user_id")
    t_ids = db.get(table="Teachers",column="user_id")
    
    
    g_id = db.add_OtherGroup("Студенты", "Информация", f_gen.date_between(d(2015,1,1), d(2020,1,1)))
    for s_id in s_ids:
        db.add_ToOtherGroup(s_id, g_id)
    
    g_id = db.add_OtherGroup("Преподаватели", "Информация", f_gen.date_between(d(2015,1,1), d(2020,1,1)))
    for t_id in t_ids:
        db.add_ToOtherGroup(t_id, g_id)
    
    g_id = db.add_OtherGroup("Базы данных и экспертные системы", "Лекции", f_gen.date_between(d(2015,1,1), d(2020,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'54'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
            
    g_id = db.add_OtherGroup("Базы данных и экспертные системы", "Семинары", f_gen.date_between(d(2015,1,1), d(2020,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'54'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
    
    
    
    g_id = db.add_OtherGroup("Безопасность информационных и аналитических систем", "Информация", f_gen.date_between(d(2015,1,1), d(2020,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'73'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
    
    
    
    g_id = db.add_OtherGroup("Информатика", "Лекции", f_gen.date_between(d(2018,1,1), d(2023,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'72'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
            
            
    
    
    g_id = db.add_OtherGroup("История христианской мысли", "Факультатив", f_gen.date_between(d(2020,1,1), d(2023,1,1)))
    for s_id in s_ids:
        if r()<0.02:
            db.add_ToOtherGroup(s_id, g_id)
            
            
    
    g_id = db.add_OtherGroup("Линейная алгебра", "Факультатив", f_gen.date_between(d(2020,1,1), d(2020,1,1)))
    for s_id in s_ids:
        if r()<0.01:
            db.add_ToOtherGroup(s_id, g_id)
            
    
    g_id = db.add_OtherGroup("Линейная алгебра", "Лекции", f_gen.date_between(d(2018,1,1), d(2020,1,1)))
    sub_id = db.get(table="Subjects", column="id", key={'name':'name', 'val':"'Линейная алгебра'"})[0]
    for s_gr in db.get(table="StudyingSubject", column="group_id", key={'name':'subject_id', 'val':sub_id}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
            
    
    g_id = db.add_OtherGroup("Линейная алгебра", "Семинары", f_gen.date_between(d(2018,1,1), d(2020,1,1)))
    sub_id = db.get(table="Subjects", column="id", key={'name':'name', 'val':"'Линейная алгебра'"})[0]
    for s_gr in db.get(table="StudyingSubject", column="group_id", key={'name':'subject_id', 'val':sub_id}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            db.add_ToOtherGroup(s_id, g_id)
    
    
    g_id = db.add_OtherGroup("Машинное обучение", "Факультатив", f_gen.date_between(d(2020,1,1), d(2020,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'54'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            if r()<0.75:
                db.add_ToOtherGroup(s_id, g_id)
    
    g_id = db.add_OtherGroup("Машинное обучение", "Факультатив", f_gen.date_between(d(2021,1,1), d(2021,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'54'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            if r()<0.75:
                db.add_ToOtherGroup(s_id, g_id)
                     
                
    g_id = db.add_OtherGroup("Основы гуманитарного знания", "Факультатив", f_gen.date_between(d(2020,1,1), d(2023,1,1)))
    for s_id in s_ids:
        if r()<0.02:
            db.add_ToOtherGroup(s_id, g_id)
    
    
    g_id = db.add_OtherGroup("Электронные платежные системы", "Факультатив", f_gen.date_between(d(2021,1,1), d(2021,1,1)))
    for s_gr in db.get(table="StudyGroups", column="id", key={'name':'kaf', 'val':"'71'"}):
        for s_id in db.get(table="GroupStudents", column="student_id", key={'name':'group_id', 'val':s_gr}):
            if r()<0.75:
                db.add_ToOtherGroup(s_id, g_id)
    
    db.commit()