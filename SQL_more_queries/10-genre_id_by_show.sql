--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT ts.title, tg.genre_id FROM tv_shows ts, tv_show_genres tg
WHERE ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
