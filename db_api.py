# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Fri Nov  1 22:24:24 2024
in Tims II Lab

@author: Stark
"""


import psycopg2 as sql
from comands import users_param

class HomeMephiDB:  
    
    def __init__(self, database,
                       user = 'postgres',
                       password = '12345',
                       host = "localhost",
                       port = '5432'):
        
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
    
        
    
    def __enter__(self):
        self.conn = sql.connect(database = self.database,
                                user = self.user,
                                password = self.password,
                                host = self.host,
                                port = self.port)
        self.cur = self.conn.cursor()
        return self
    
    def __exit__(self, ex_type, *args):
        self.cur.close()
        self.conn.close()
        if ex_type is not None:
            pass#raise Exception("Error has been occured")
        
    
    def _create_(self):
        
        from comands import init
        
        self.cur.execute(init)
    
    def execute(self, command, tag = "one"):
        self.cur.execute(command)
        if tag == "all":return self.cur.fetchall()
        elif tag == "one": return self.cur.fetchone()
    
    def commit(self):
        self.conn.commit()
    
    
    def get(self, table, column = '*', key=None):
        if type(column) is not list:
            column = [column]
            comb = True
        
        if key is None:
            key = ''
        else:
            key = f" WHERE {key['name']} = {key['val']}"
        ans = self.execute(f"SELECT ({', '.join(column)}) FROM {table}{key}", "all")
        if comb:
            ans = list(map(lambda x:x[0], ans))
        return ans
    
    def add_User(self, ID, name, bd, pw = None, em = None, ph = None, ii = None, kaf = "22"):
        
        #no check because we dont add only user its only student or teacher
        
        sn = name["second"]#f
        fn = name["first"] #i
        ln = name["last"]  #o
        i = 0
        head = f'{sn[0]}{fn[0]}{ln[0]}'.lower()
        
        #uniquify login
        flag = ()
        while flag is not None:
            i+=1
            l = f'{head}{i:03}'
            flag = self.execute(f"SELECT login FROM Users WHERE login = '{l}'")
        
        if pw is None: pw = 12345
        if em is None: em = ID
        if ph is None: ph = ID
        if ii is None: ii = ID
            
        #(login, password, second_name, first_name, last_name, birth_date, email, phone, photo_id)
        
        return self.execute(f"INSERT INTO Users {users_param} VALUES ({ID}, '{l}', '{pw}', '{sn}', '{fn}', '{ln}', '{bd}', '{em}', {ph}, {ii}) RETURNING id")[0]
        
    
    def add_Student(self, ID, name, bd, pw = None, em = None, ph = None, ii = None, kaf = "22"):
        exist = self.get(table="Students",
                         column="id",
                         key={'name':"user_id",'val':ID})
        
        if exist: return ID
        
        UID = self.add_User(ID, name, bd, pw, em, ph, ii)
        self.execute(f"INSERT INTO Students (user_id) VALUES ({UID}) RETURNING id")
    
    def add_Group(self, ID, name, head_id = 'NULL', curr = ""):
        kaf = name[-3::2]
        self.execute(f"INSERT INTO StudyGroups (id, group_name, head_id, curriculum, kaf) VALUES ({ID}, '{name}', {head_id}, '{curr}', '{kaf}') RETURNING id")
    
    def add_Student_to_Group(self, s_id, g_id):
        
        self.execute(f"INSERT INTO GroupStudents (student_id, group_id) VALUES ({s_id}, {g_id}) RETURNING student_id")
    
    
    
    def add_Teacher(self, ID, name, bd, pw = None, em = None, ph = None, ii = None, kaf = "22"):
        exist = self.get(table="Teachers",
                         column="id",
                         key={'name':"user_id",'val':ID})
        
        if exist: return ID
        
        UID = self.add_User(ID, name, bd, pw, em, ph, ii)
        self.execute(f"INSERT INTO Teachers (user_id, department) VALUES ({UID}, {kaf}) RETURNING id")
