SELECT * FROM movies.movies_basic;
SELECT DISTINCT Genre,title AS 'TITLE' from movies_basic ;
SELECT genre,title,critics_rating from movies_basic ORDER BY critics_rating DESC; 
SELECT title, release_year AS "In_cinemas" from movies_basic where release_year > 1905 AND release_year < 1990 ;
SElECT title,ID from movies_basic where id <20 AND id <>40 limit 10,20909099;
SELECT Genre,studio from movies_basic where studio LIke 'BIX' ; 

-- underscore matches only 1 charesteristics;
SELECT title,Genre,studio,release_year from movies_basic where release_year LIke '192_' ;

--begin with studio  'STUDIO%' ;
SELECT * FROM movies_basic where genre LIKE 'STUDIO%'; 

--having substring "STUDIO";
SELECT * FROM movies_basic where genre LIKE '%STUDIO%'; 

SELECT * FROM movies_basic WHERE LENGTH(title) > 20 AND critics_rating <4; 
SELECT title, IF (critics_rating > 5,"GOOD","BAD") AS "Score"  FROM movies_basic;

SELECT title,
CASE 
    WHEN critics_rating <3 THEN 'Bad'
	WHEN  critics_rating > 5 THEN 'Good'
    ELSE 'Intermediate'
END AS 'score'
FROM movies_basic;

SELECT title AS 'Title:',
CASE 
     WHEN release_year < 2000 THEN "20th Century"
     WHEN release_year < 2100 THEN '21th Century'
     ELSE "22nd Century"
END AS 'Released', 
directors AS 'DiRECTOR',
CASE 
     WHEN critics_rating <= 5 THEN 'BAD'
     WHEN critics_rating <= 5.1 AND critics_rating <= 7 THEN 'Decent'
     WHEN critics_rating <= 7.1 AND critics_rating <= 8.9 THEN 'Good'
	ELSE 'Amazing'
END AS 'Review'
FROM movies_basic ORDER BY title DESC;


---JOIN



