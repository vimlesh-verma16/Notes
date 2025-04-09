Create Table movies_basic
(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
title VARCHAR(40),
genre varchar(40),
releasetear INT, 
directors VARCHAR(50),
studio VARCHAR(40),
critics_rating DECIMAL(2,1)
);

-- Use DROP TABLE if you no longer need the table.
-- Use TRUNCATE TABLE if you want to clear all data but keep the table.

ALTER TABLE movies.movies_basic RENAME COLUMN releasetear TO release_year; 

DROP TABLE movies_basic ;

-- --always use > or = for interger other wise quesry will be slow :
INSERT INTO movies_basic
(title,genre,release_year,directors,studio,critics_rating)
VALUES 
('END Game','Action','2016','Stan Lee', 'SONY Studio','9'),
('GOT','Emotional','2020','Stan Lee', 'Marvel Studio','9');

SELECT * FROM movies_basic Where directors = 'Miley Watson';

UPDATE movies_basic SET directors = 'Mike Watson' WHERE directors = 'Miley Watson';

SELECT * FROM movies_basic Where directors = 'Mike Watson';

-- NO RUN IT is preferred over delete as delete perform row by row operation 
TRUNCATE movies_basic; 


-----------Challenge: 
INSERT INTO movies_basic
(title,genre,release_year,directors,studio,critics_rating)
Values
('run for the forest','Drama','1946','rence_pera','Lionel Brownstone','0.3'),
('Luck of the Night','Drama','1951','rence_pera','Lionel Brownstone','6.8'),
('Invader Galaxy','Adventure','1953','rence_pera','Studio 60','5.5');

SELECT *  FROM movies_basic WHERE genre Like 'Sci%' AND studio LIKE 'Falstead%';
UPDATE movies_basic
SET genre = 'SF' 
WHERE genre Like 'Sci%' AND studio LIKE 'Falstead%';
SELECT *  FROM movies_basic WHERE genre Like 'SF' AND studio LIKE 'Falstead%'; 

SELECT * fROM movies_basic WHERE directors LIKE 'Garry Scott' AND studio LIke 'Lionel Brownstone';
DELETE FROM movies_basic 
WHERE directors LIKE 'Garry Scott' AND studio LIke 'Lionel Brownstone'; 



