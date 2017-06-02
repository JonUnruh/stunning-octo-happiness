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

CREATE TABLE public.hashtag
(
    hashtagid integer NOT NULL,
    inhalt text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT hpk PRIMARY KEY (hashtagid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.hashtag
    OWNER to postgres;

CREATE TABLE public.vorkommen_in
(
    tweet_id integer NOT NULL,
    vorkommen date NOT NULL,
    hashtagid integer NOT NULL,
    CONSTRAINT vorkommen_in_pkey PRIMARY KEY (hashtagid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.vorkommen_in
    OWNER to postgres;