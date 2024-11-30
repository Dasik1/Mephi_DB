/*
HomeMephi database init

authors: Stark, D1rall
*/

---academic perfomance---
CREATE TABLE IF NOT EXISTS Users ( --parser DONE
    id SERIAL PRIMARY KEY,
    login CHAR(6) NOT NULL UNIQUE,
    password VARCHAR(100),

    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    email VARCHAR(100) UNIQUE,
    phone BIGINT UNIQUE,
    photo_id int UNIQUE
);

CREATE TABLE IF NOT EXISTS Students ( --parser DONE
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS StudyGroups ( --parser DONE
    id INTEGER PRIMARY KEY,
    group_name VARCHAR(7) NOT NULL,
    head_id INT,
    FOREIGN KEY (head_id) REFERENCES Students (user_id) ON DELETE SET NULL,
    curriculum VARCHAR(100),
    kaf VARCHAR(2) NOT NULL
);

---to enter 3d normal form
CREATE TABLE IF NOT EXISTS GroupStudents( --parser DONE
    student_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students (user_id) ON DELETE CASCADE,
    group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES StudyGroups (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Teachers ( --parser DONE
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE,
    department INTEGER NOT NULL,
    work_from DATE
);

CREATE TABLE IF NOT EXISTS Subjects ( --parser DONE
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    department INTEGER NOT NULL,
    total_hours INTEGER
	
);

CREATE TABLE IF NOT EXISTS Marks ( --parser DONE
    id SERIAL PRIMARY KEY,
    subject_id INT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES Subjects (id) ON DELETE CASCADE,
    grade_type MARK_TYPE,
    grade_val SMALLINT NOT NULL,
    grade_ECTS MARK_ECTS
);

CREATE TABLE IF NOT EXISTS StudentMarks ( --parser DONE
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students (user_id) ON DELETE CASCADE,
    mark_id INT NOT NULL,
    FOREIGN KEY (mark_id) REFERENCES Marks (id) ON DELETE RESTRICT,
    teacher_id INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (user_id) ON DELETE CASCADE,
    mark_date DATE NOT NULL
);


---from other---

CREATE TABLE IF NOT EXISTS Audiences ( --parser DONE
    id SERIAL PRIMARY KEY,

	name VARCHAR(10) NOT NULL UNIQUE,
	
    building BUILDING_TYPE,
    floor SMALLINT,
    numder SMALLINT,

    capacity INTEGER
    ---equipment in PRO version)---
);

---shedule---
CREATE TABLE IF NOT EXISTS TeachingSubject ( --parser DONE
    id SERIAL PRIMARY KEY,
    teacher_id INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (user_id) ON DELETE CASCADE,
    subject_id INT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES Subjects (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS StudyingSubject ( --parser DONE
    id SERIAL PRIMARY KEY,
	group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES StudyGroups (id) ON DELETE CASCADE,
	subject_id INT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES Subjects (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Shedule ( --parser DONE
    id SERIAL PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES Subjects (id) ON DELETE CASCADE,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (user_id) ON DELETE CASCADE,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES StudyGroups (id) ON DELETE CASCADE,
    audience_id INTEGER NOT NULL,
    FOREIGN KEY (audience_id) REFERENCES Audiences (id) ON DELETE CASCADE,
	week_day DAY_TYPE NOT NULL,
	time_start TIME NOT NULL
);

---other other (perfect joke)---
CREATE TABLE IF NOT EXISTS OtherGroups ( --parser DONE
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL,
    group_type VARCHAR(30) NOT NULL,
    head_id INT,
    FOREIGN KEY (head_id) REFERENCES Users (id) ON DELETE SET NULL,
    creade_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS OtherGroupMembers ( --parser DONE
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE,
    group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES OtherGroups (id) ON DELETE SET NULL 

);
/*
CREATE TABLE IF NOT EXISTS Events (
    id SERIAL PRIMARY KEY,
    event_name VARCHAR(100),
    event_begin_date  DATE NOT NULL,
    event_end_date DATE NOT NULL,
    event_begin_time TIME NOT NULL,
    event_end_time TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS GroupEvents (
    id SERIAL PRIMARY KEY,
    group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES OtherGroups (id) ON DELETE CASCADE,
    event_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events (id) ON DELETE CASCADE
);
*/

CREATE TABLE IF NOT EXISTS Psycologists ( --parser DONE
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE,
    about TEXT
);

CREATE TABLE IF NOT EXISTS PsycologistAppointment ( --parser DONE
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE,
    psycologist_id INT NOT NULL,
    FOREIGN KEY (psycologist_id) REFERENCES Psycologists (id) ON DELETE CASCADE,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS SerteficateOrders ( --parser DONE
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE,
    order_data VARCHAR(255) NOT NULL,
    order_date DATE NOT NULL,
    order_result ORDER_TYPE NOT NULL
);
