/*
HomeMephi database init

authors: Stark, D1rall
*/

---academic perfomance---
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Students CASCADE;
DROP TABLE IF EXISTS StudyGroups CASCADE;
---to enter 3d normal form
DROP TABLE IF EXISTS GroupStudents CASCADE;
DROP TABLE IF EXISTS Teachers CASCADE;
DROP TABLE IF EXISTS Subjects CASCADE;
DROP TABLE IF EXISTS TeachingSubject CASCADE;
DROP TABLE IF EXISTS StudyingSubject CASCADE;
DROP TABLE IF EXISTS Marks CASCADE;
DROP TABLE IF EXISTS StudentMarks CASCADE;
---from other---
DROP TABLE IF EXISTS Audiences CASCADE;
---shedule---
DROP TABLE IF EXISTS Lessons CASCADE;
DROP TABLE IF EXISTS TeachingLessons CASCADE;
DROP TABLE IF EXISTS StudyingLessons CASCADE;
DROP TABLE IF EXISTS Shedule CASCADE;
---other other (perfect joke)---
DROP TABLE IF EXISTS OtherGroups CASCADE;
DROP TABLE IF EXISTS OtherGroupMembers CASCADE;
DROP TABLE IF EXISTS Events CASCADE;
DROP TABLE IF EXISTS GroupEvents CASCADE;
---services---
DROP TABLE IF EXISTS Reviews CASCADE;
DROP TABLE IF EXISTS ReviewConnections CASCADE;
DROP TABLE IF EXISTS Psycologists CASCADE;
DROP TABLE IF EXISTS PsycologistAppointment CASCADE;
DROP TABLE IF EXISTS SerteficateOrders CASCADE;