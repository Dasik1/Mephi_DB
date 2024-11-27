# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Nov 16 16:47:20 2024
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


with HomeMephiDB(database="HomeMephi") as db:
    
    #serteficates
    #for everyone
    s_ids = db.get(table="Students",column="user_id")
    t_ids = db.get(table="Teachers",column="user_id")
    
    for i in range(5):
        s, f, l = f_gen.name().split(" ")
        p_id = db.add_Psycologist(-int(now()%1000000), name = {"second":s,
                                                        "first":f,
                                                        "last":l},
                                  bd = f_gen.date_between(d(1950,1,1), d(2000,1,1)))
        
        for s_id in s_ids:
            if r()<0.01:
                date = f_gen.date_between(d(2024,9,1), d(2025,1,1))
                time = t(10+rint(0, 6), 0)
                db.add_PsycologistAppointmenr(s_id, p_id, date, time)
        
        zzz(1)
    
    
    db.commit()



