-- SQL - More queries
-- list all genres not linked to the show Dexter
SELECT tv_genres.name FROM 
    tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_show_genres.genre_id NOT IN 
    (SELECT tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter')
    GROUP BY tv_genres.name    
    ORDER BY tv_genres.name;
