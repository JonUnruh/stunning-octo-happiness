COPY tweet(tweet_id, handle text, inhalt text, ist_retweet,"ursprünglicher_autor", datum, antwort_auf, ist_zitat, anzahl_retweets, anzahl_likes) 
FROM 'C:\Program Files\PostgreSQL\9.6\data\amelec-filtered.csv'
WITH DELIMITER ';' CSV HEADER;