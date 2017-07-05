SELECT A.hashtagid AS source, B.hashtagid AS target
	FROM vorkommen_in A, vorkommen_in B
    WHERE A.tweet_id = B.tweet_id AND A.hashtagid < B.hashtagid
    ORDER BY A.hashtagid