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



with HomeMephiDB(database="HomeMephi") as db:
    
    
    
    
    
    
    #serteficates
    #for everyone
    s_ids = db.get(table="Students",column="user_id")
    t_ids = db.get(table="Teachers",column="user_id")
    
    for s_id in s_ids:
        db.add_Serteficate_Request(s_id, data, date, rez)




