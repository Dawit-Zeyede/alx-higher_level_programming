-- Import data base dump of hbtn_0d_tvshows and lists all shows contained in the  'hbtn_0d_tvshows'
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
