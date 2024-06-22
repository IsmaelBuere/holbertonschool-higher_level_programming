-- database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.id = tv_genres.tv_show_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;