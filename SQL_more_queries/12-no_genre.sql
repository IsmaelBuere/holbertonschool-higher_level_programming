-- database dump from hbtn_0d_tvshows to your MySQL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;