import csv
import oracledb

connection = oracledb.connect(
    user="YOUR_ORACLE_USERNAME",
    password="YOUR_ORACLE_PASSWORD",
    dsn="YOUR_ORACLE_DSN"
)

cursor = connection.cursor()

def load_csv(file_path, insert_sql):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cleaned_row = [None if value == "" else value for value in row]
            cursor.execute(insert_sql, cleaned_row)

load_csv(
    "data/app_user.csv",
    """
    INSERT INTO APP_USER (user_id, username, email, display_name, location, created_at)
    VALUES (:1, :2, :3, :4, :5, TO_TIMESTAMP(:6, 'YYYY-MM-DD HH24:MI:SS'))
    """
)

load_csv(
    "data/hashtag.csv",
    """
    INSERT INTO HASHTAG (hashtag_id, tag_text, first_seen_at)
    VALUES (:1, :2, TO_TIMESTAMP(:3, 'YYYY-MM-DD HH24:MI:SS'))
    """
)

load_csv(
    "data/tweet.csv",
    """
    INSERT INTO TWEET (tweet_id, user_id, tweet_text, created_at, lang, reply_to_tweet_id)
    VALUES (:1, :2, :3, TO_TIMESTAMP(:4, 'YYYY-MM-DD HH24:MI:SS'), :5, :6)
    """
)

load_csv(
    "data/sentiment_score.csv",
    """
    INSERT INTO SENTIMENT_SCORE (tweet_id, score, model_version, computed_at)
    VALUES (:1, :2, :3, TO_TIMESTAMP(:4, 'YYYY-MM-DD HH24:MI:SS'))
    """
)

load_csv(
    "data/tweet_hashtag.csv",
    """
    INSERT INTO TWEET_HASHTAG (tweet_id, hashtag_id, tagged_at)
    VALUES (:1, :2, TO_TIMESTAMP(:3, 'YYYY-MM-DD HH24:MI:SS'))
    """
)

connection.commit()
cursor.close()
connection.close()

print("All CSV files loaded successfully into Oracle.")