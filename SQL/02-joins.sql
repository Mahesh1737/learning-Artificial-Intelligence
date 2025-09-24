use deg;

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert values
INSERT INTO student (student_id, name) VALUES
(101, 'adam'),
(102, 'bob'),
(103, 'casey');

CREATE TABLE course (
    student_id INT,
    course VARCHAR(50),
    PRIMARY KEY (student_id, course)
);

-- Insert values
INSERT INTO course (student_id, course) VALUES
(102, 'english'),
(105, 'math'),
(103, 'science'),
(107, 'computer science');

