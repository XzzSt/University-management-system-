CREATE TABLE course_professor(
    CourseID VARCHAR(10),
    Credit INT,
    ProfUIN INT,
    PRIMARY KEY (CourseID)
);

CREATE TABLE professor(
	ProfUIN INT,
	ProfName VARCHAR(30),
	DepartmentName VARCHAR(30),
	Age INT,
	Gender VARCHAR(6),
	PRIMARY KEY (ProfUIN)
);

CREATE TABLE student(
	UIN INT,
	StuName VARCHAR(30),
	BirthYear INT,
	Gender VARCHAR(6),
	Phone FLOAT,
	Major VARCHAR(20),
	PRIMARY KEY(UIN)
);

CREATE TABLE study (
  CourseID VARCHAR(10),
  UIN int,
  Score INT DEFAULT NULL,
  PRIMARY KEY (CourseID,UIN)
);

CREATE TABLE course(
	CourseID VARCHAR(10),
	Credit INT,
	CRN INT,
	Department VARCHAR(30),
	Start_Date FLOAT,
	PRIMARY KEY(CourseID)
)
ALTER TABLE Course_Professor DROP COLUMN Credit;

SELECT student.UIN, student.StuName, course.CourseID, study.score
FROM study
JOIN course ON study.CourseID = course.CourseID
JOIN student ON study.UIN = student.UIN
WHERE study.CourseID LIKE 'BIO__%';

SELECT student.UIN, student.StuName, course.CourseID, study.score
FROM Study
JOIN course ON study.CourseID = course.CourseID
JOIN student ON study.UIN = student.UIN
WHERE study.Score < 60;

SELECT professor.Age, professor.ProfName, professor.DepartmentName, Course_Professor.CourseID
FROM Course_Professor
JOIN professor on course_professor.ProfUIN = professor.ProfUIN
WHERE professor.Age >= 50

SELECT *
FROM student
Where student.UIN = 110100
