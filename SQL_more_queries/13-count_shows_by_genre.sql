-- database dump from hbtn_0d_tvshows
SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_show_genres.genre_id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;