# COP 3701 Project: Social Analytics Database

## How To Use
Step 1: Use the “create_db.sql” to create the database
Step 2: Use the dataload.sql to populate the database with toy data
Step 3: Change app.py and add your database credentials
Step 4: run the app.py using the command below
Python -m streamlit run app.py



## Application Domain
This project builds a social analytics database focused on short-form posts. The system stores tweet content and metadata, tracks hashtag usage over time, and supports analytics like trending hashtags.

## High-Level Goals
1. Store tweets, authors, and sentiment scores in a relational database.
2. Support hashtag trend ranking 
3. Provide automated sentiment aggregation procedures:
4. Enable analytics like the following:
   - “Top 10 hashtags today”
   - “Sentiment trend for #topic over time”
   - “Most positive/negative hashtags this week”

## Project Scope
- Tables for: Users/Authors, Tweets, Hashtags, Trend tables.
- Automated procedures like updating the hashtag trend and computing hashtag sentiment.
- Constraints and data integrity.
- Sample dataset imports.


## Intended Users
- Data analysts
- Marketing teams
- Instructors

## Data Sources
Possible sources include:
1. Public social media datasets from Kaggle containing tweets + hashtags.
2. Public academic datasets on tweet text + metadata.

---

## Database Application

This project builds a social analytics database for tweets, hashtags, and sentiment scores. The system stores tweet content and metadata, tracks hashtag usage frequency, and supports hashtag trend ranking.

### Unique / Challenging Aspects
- Many-to-many relationship between Tweets and Hashtags implemented using an associative entity.
- One-to-one relationship between Tweet and SentimentScore.
- Automated sentiment aggregation and trend ranking.
- Proper enforcement of primary and foreign key constraints.


## Useful Files

- Final ER design: [database_er.md](database_er.md)
- Database schema script: [create_db.sql](create_db.sql)
- Data preprocessing script: [preprocess.py](preprocess.py)
- Data loading script: [dataload.py](dataload.sql)
- CSV data files: [data/](data/)
