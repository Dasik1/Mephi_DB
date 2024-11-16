select student_id from Studygroups S
Join GroupStudents G ON S.id = G.group_id
Join Users U on G.student_id = U.id
where S.id = 