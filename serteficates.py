# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Nov 16 16:47:20 2024
in Tims II Lab

@author: Stark
"""
# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Nov 16 16:47:20 2024
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

from random import random as r



with HomeMephiDB(database="HomeMephi") as db:
    
    #serteficates
    #for everyone
    s_ids = db.get(table="Students",column="user_id")
    t_ids = db.get(table="Teachers",column="user_id")
    
    #card 
    data = "<certificate with the stamp>"
    for s_id in s_ids:
        if r()<0.3:
            date = f_gen.date_between(d(2024,9,1), d(2025,1,1))
            if date < d(2024,11,1):rez = 'Выдан'
            elif date < d(2024, 12, 1):rez = "В обработке"
            else: rez = "Принят"
            
            
            ID = db.add_Serteficate_Request(s_id, data, date)
            db.set_Serteficate_Result(ID, rez)
    
    db.commit()