COPY tweet(tweet_id, handle, inhalt, ist_retweet,"ursprünglicher_autor", datum, antwort_auf, ist_zitat, anzahl_retweets, anzahl_likes) 
FROM 'C:\Program Files\PostgreSQL\9.6\data\amelec-filtered.csv'
WITH DELIMITER ';' CSV HEADER;

COPY hashtag(hashtagid, inhalt) 
FROM 'C:\Program Files\PostgreSQL\9.6\data\amelec-hashtag.csv'
WITH DELIMITER ';' CSV HEADER;

CREATE temporary TABLE t (x1 integer, 
	tweet_id float NOT NULL,
    vorkommen timestamp NOT NULL,
    hashtagid float NOT NULL);

COPY t(x1, hashtagid, tweet_id, vorkommen) 
FROM 'C:\Program Files\PostgreSQL\9.6\data\amelec-vorkommen.csv'
WITH DELIMITER ';' CSV HEADER;

insert into vorkommen_in (tweet_id, vorkommen, hashtagid)
select tweet_id, vorkommen, hashtagid
from t;

drop table t;