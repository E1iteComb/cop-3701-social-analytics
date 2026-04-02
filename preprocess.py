import csv
import os
import random
from datetime import datetime, timedelta

random.seed(42)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

NUM_USERS = 100
NUM_TWEETS = 150
NUM_HASHTAGS = 100

locations = [
    "Lakeland, FL",
    "Miami, FL",
    "Orlando, FL",
    "Tampa, FL",
    "Jacksonville, FL",
    "Titusville, FL",
    "Winter Haven, FL",
    "Boca Raton, FL",
    "Tallahassee, FL",
    ""
]

tweet_phrases = [
    "Loving the new semester at Florida Poly.",
    "Working on my database project tonight.",
    "This update looks much better now.",
    "Trying to clean my dataset correctly.",
    "The analytics dashboard is finally working.",
    "Still debugging a few issues in my script.",
    "Finished another part of my course project.",
    "This query gave me the result I needed.",
    "Working through normalization step by step.",
    "Testing some sample data for the database.",
    "The schema design is starting to make sense.",
    "Loading data into the tables now.",
    "Reviewing the ER diagram one more time.",
    "This sentiment score looks reasonable.",
    "Building out the project structure in GitHub."
]

hashtag_bases = [
    "college", "stem", "database", "sql", "python", "analytics", "trend", "sentiment",
    "bug", "update", "school", "project", "coding", "data", "tech", "student",
    "design", "schema", "query", "report", "load", "csv", "github", "oracle", "cloud"
]

def random_timestamp(start_date=datetime(2026, 1, 1, 8, 0, 0), max_days=90):
    delta = timedelta(
        days=random.randint(0, max_days),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    return (start_date + delta).strftime("%Y-%m-%d %H:%M:%S")

# -------------------------
# APP_USER
# -------------------------
users = []
for i in range(1, NUM_USERS + 1):
    user_id = i
    username = f"user_{i}"
    email = f"user_{i}@example.com"
    display_name = f"User {i}"
    location = random.choice(locations)
    created_at = random_timestamp()
    users.append([user_id, username, email, display_name, location, created_at])

with open(os.path.join(DATA_DIR, "app_user.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "username", "email", "display_name", "location", "created_at"])
    writer.writerows(users)

# -------------------------
# HASHTAG
# -------------------------
hashtags = []
used_tags = set()
hashtag_id = 1

while len(hashtags) < NUM_HASHTAGS:
    base = random.choice(hashtag_bases)
    tag_text = f"{base}{hashtag_id}"
    if tag_text not in used_tags:
        used_tags.add(tag_text)
        first_seen_at = random_timestamp()
        hashtags.append([hashtag_id, tag_text, first_seen_at])
        hashtag_id += 1

with open(os.path.join(DATA_DIR, "hashtag.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["hashtag_id", "tag_text", "first_seen_at"])
    writer.writerows(hashtags)

# -------------------------
# TWEET
# -------------------------
tweets = []
tweet_ids = []

for i in range(NUM_TWEETS):
    tweet_id = 1001 + i
    tweet_ids.append(tweet_id)
    user_id = random.randint(1, NUM_USERS)
    tweet_text = random.choice(tweet_phrases)
    created_at = random_timestamp()
    lang = "en"

    reply_to_tweet_id = ""
    if i >= 10 and random.random() < 0.20:
        reply_to_tweet_id = random.choice(tweet_ids[:-1])

    tweets.append([tweet_id, user_id, tweet_text, created_at, lang, reply_to_tweet_id])

with open(os.path.join(DATA_DIR, "tweet.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["tweet_id", "user_id", "tweet_text", "created_at", "lang", "reply_to_tweet_id"])
    writer.writerows(tweets)

# -------------------------
# SENTIMENT_SCORE
# -------------------------
sentiment_scores = []
for tweet in tweets:
    tweet_id = tweet[0]
    score = round(random.uniform(-1.00, 1.00), 2)
    model_version = "v1"
    computed_at = random_timestamp()
    sentiment_scores.append([tweet_id, score, model_version, computed_at])

with open(os.path.join(DATA_DIR, "sentiment_score.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["tweet_id", "score", "model_version", "computed_at"])
    writer.writerows(sentiment_scores)

# -------------------------
# TWEET_HASHTAG
# -------------------------
tweet_hashtag_rows = []
used_pairs = set()

for tweet in tweets:
    tweet_id = tweet[0]
    num_tags = random.randint(1, 3)
    chosen_hashtags = random.sample(range(1, NUM_HASHTAGS + 1), num_tags)

    for hashtag_id in chosen_hashtags:
        pair = (tweet_id, hashtag_id)
        if pair not in used_pairs:
            used_pairs.add(pair)
            tagged_at = random_timestamp()
            tweet_hashtag_rows.append([tweet_id, hashtag_id, tagged_at])

with open(os.path.join(DATA_DIR, "tweet_hashtag.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["tweet_id", "hashtag_id", "tagged_at"])
    writer.writerows(tweet_hashtag_rows)

print("CSV files generated successfully in the data folder.")
print("Generated files:")
print("- data/app_user.csv")
print("- data/tweet.csv")
print("- data/hashtag.csv")
print("- data/sentiment_score.csv")
print("- data/tweet_hashtag.csv")
