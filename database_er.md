# Database ER Diagram — Social Analytics

## User Groups
- Analyst / Data Scientist
- Marketing / Brand Team
- System Administrator

---

## ER Diagram

```mermaid
erDiagram
    USER ||--o{ TWEET : posts
    TWEET ||--|| SENTIMENT_SCORE : has
    TWEET ||--o{ TWEET_HASHTAG : tagged_with
    HASHTAG ||--o{ TWEET_HASHTAG : appears_in

    USER {
      int user_id PK
      string username
      string email
      string display_name
      string location
      datetime created_at
    }

    TWEET {
      bigint tweet_id PK
      int user_id FK
      string tweet_text
      datetime created_at
      string lang
      bigint reply_to_tweet_id
    }

    HASHTAG {
      int hashtag_id PK
      string tag_text
      datetime first_seen_at
    }

    TWEET_HASHTAG {
      bigint tweet_id PK, FK
      int hashtag_id PK, FK
      datetime tagged_at
    }

    SENTIMENT_SCORE {
      bigint tweet_id PK, FK
      decimal score
      string model_version
      datetime computed_at
    }
