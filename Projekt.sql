CREATE TABLE public.Tweet
(
    Tweet_ID integer NOT NULL,
	handle text COLLATE pg_catalog."default",
    Inhalt text COLLATE pg_catalog."default",
	ist_retweet BOOLEAN,
	ursprünglicher_Autor text COLLATE pg_catalog."default",
	Datum DATE NOT NULL,
	Antwort_auf text COLLATE pg_catalog."default",
	ist_Zitat BOOLEAN,
	Anzahl_Retweets INTEGER NOT NULL,
	Anzahl_Likes INTEGER NOT NULL,	
	
	CONSTRAINT tpk PRIMARY KEY (Tweet_ID)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE PUBLIC.Hashtag
(
    Inhalt text COLLATE pg_catalog."default",	
	Anzahl_Vorkommen INTEGER,
	Benutzungszeitpunkte DATE ARRAY[200],
    tritt_auf_mit text ARRAY[10],
	Tweet_ID INTEGER NOT NULL,
    
	CONSTRAINT hpk PRIMARY KEY (Inhalt)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;