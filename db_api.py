# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Fri Nov  1 22:24:24 2024
in Tims II Lab

@author: Stark
"""


import psycopg2 as sql
from comands import(
    users_param,
    Teacher_from_FIO,
    Students_from_Group
)
from datetime import date as d

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
        comb = False
        if type(column) is not list and column != '*':
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
        #как же я блять ошибался
        exist = self.get(table="Users",
                         column="id",
                         key={'name':"id",'val':ID})
        
        if exist: return ID
        
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
    
    
    
    def add_Teacher(self, ID, name, bd, pw = None, em = None, ph = None, ii = None, kaf = "22", wf=d(2024,9,1)):
        exist = self.get(table="Teachers",
                         column="id",
                         key={'name':"user_id",'val':ID})
        
        if exist: return ID
        
        UID = self.add_User(ID, name, bd, pw, em, ph, ii)
        self.execute(f"INSERT INTO Teachers (user_id, department, work_from) VALUES ({UID}, {kaf}, '{wf}') RETURNING id")
    
    
    def get_Teacher(self, name):
        """format = Fam I.O"""
        
        f, n_o = name.split('\xa0')#I hate home mephi authors
        var = self.execute(Teacher_from_FIO + f"'{f}'", "all")
        if n_o.count(".") == 1: n_o = n_o[0]+"-"
        elif n_o.count(".") == 2: n_o = n_o[0]+n_o[2]
        #else it skips the loop
        
        for i in var:
            if i[1][0]+i[2][0] == n_o:
                return i[3], i[4] #department, id
        
        #u should follow rules
        #get out of here
        
        #print([name]) <- he is gay
        
        #raise Exception("Get teacher with not valid ")
        return None, None
    
    
    
    def add_Subject(self, name, department):
        if len(name)>150:return None
        
        exist = self.get(table="Subjects",
                         column=["id", "department"],
                         key={'name':"name",'val':f"'{name}'"})
        
        if exist:
            if len(exist)>0:
                ID, kaf = 0, -1
                for i in exist:
                    nID, nkaf = eval(i[0])
                    if nkaf>=kaf and kaf == -1:
                        ID = nID
                        kaf = nkaf
                if kaf < department:
                    print(f"update {name} to {department}")
                    self.execute(f"UPDATE Subjects SET department={department} WHERE id={ID} RETURNING id")
                    return ID
                return max(ID, nID)
        else:
            return self.execute(f"INSERT INTO Subjects (name, department) VALUES ('{name}', {department}) RETURNING id")[0]
    
    
    def get_learning_groups(self):
        ans = self.execute("SELECT Group_id FROM StudyingSubject GROUP BY Group_id", "all")
        return list(map(lambda x: x[0], ans))
        
    
    
    
    def add_Audience(self, name):
        exist = self.get(table="Audiences",
                         column="id",
                         key={'name':"name",'val':f"'{name}'"})
        
        if exist: return exist[0]
        if len(name) >10:return None
        return self.execute(f"INSERT INTO Audiences (name) VALUEs ('{name}') RETURNING id")[0]
    
    def add_TeachingSubject(self, t_id, l_id):
        return self.execute(f"INSERT INTO TeachingSubject (teacher_id, subject_id) VALUES ({t_id}, {l_id}) RETURNING id")[0]
    
    def add_StudyingSubject(self, g_id, l_id):
        return self.execute(f"INSERT INTO StudyingSubject (group_id, subject_id) VALUES ({g_id}, {l_id}) RETURNING id")[0]
    
    
    def get_Students_from_Group(self, group_id):
        return self.execute(Students_from_Group + str(group_id) , "all")
    
    def add_Shedule(self, l_id, t_id, g_id, a_id, weekday, time):
        return self.execute(f"INSERT INTO Shedule (subject_id, teacher_id, group_id, audience_id, week_day, time_start) VALUES ({l_id}, {t_id}, {g_id}, {a_id}, '{weekday}', '{time}') RETURNING id")[0]
    
    
    def add_Mark(self, s_id, grade):
        return self.execute(f"INSERT INTO Marks (subject_id, grade_val) VALUES ({s_id}, {grade}) RETURNING id")[0]
    
    
    def add_Student_Mark(self, s_id, m_id, t_id, date):
        return self.execute(f"INSERT INTO StudentMarks (student_id, mark_id, teacher_id, mark_date) VALUES ({s_id}, {m_id}, {t_id}, '{date}') RETURNING id")
    
