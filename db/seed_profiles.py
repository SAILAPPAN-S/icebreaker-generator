import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'profiles.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS user_profiles(
                id INTEGER PRIMARY KEY autoincrement,
                name TEXT NOT NULL,
        age INTEGER,
        location TEXT,
        interests TEXT,   -- comma-separated
        bio TEXT
        );
                """)
    
    conn.commit()
    conn.close()

def seed_profiles():
    profiles = [
        ("Aarav", 21, "Bangalore", "coding,coffee,k-dramas", 
         "CS student who lives in cafés, loves debugging and binge-watching K-dramas."),
        ("Priya", 20, "Chennai", "books,anime,travel",
         "Introvert with a loud Spotify playlist and a long anime watchlist."),
        ("Rahul", 22, "Mumbai", "cricket,memes,startups",
         "Future founder, current assignment warrior. Loves late-night chai and startup podcasts."),
        ("Ananya", 19, "Delhi", "k-pop,k-dramas,sketching",
         "K-drama addict who cries over fictional characters and doodles in the margins of notes."),
        ("Vikram", 23, "Hyderabad", "gaming,fitness,tech",
         "Plays Valorant, lifts weights, and breaks production code (sometimes)."),
        ("Sanya", 21, "Pune", "coffee,reading,solo-travel",
         "Reads in cafés, plans solo trips she may or may not take."),
        ("Karthik", 20, "Coimbatore", "coding,hackathons,AI",
         "Sleeps in class, wakes up for hackathons. Loves building random AI projects."),
        ("Meera", 22, "Kochi", "music,photography,webtoons",
         "Lives on playlists and sunset photos. Webtoons > sleep."),
        ("Aditya", 24, "Noida", "stock-market,podcasts,football",
         "Day trader in theory, broke student in reality."),
        ("Ishita", 21, "Jaipur", "baking,rom-coms,spotify",
         "Bakes when stressed, feeds friends, forgets her own assignments."),
        ("Rohan", 19, "Tenkasi", "anime,tech-youtube,coffee",
         "Anime enjoyer and tech YouTube worm, survives on cold coffee."),
        ("Divya", 20, "Nagpur", "journaling,yoga,dramas",
         "Keeps a journal for everything, including how lectures made her sleepy."),
        ("Sahil", 22, "Goa", "beaches,photography,startups",
         "Beach walks, camera in hand, startup ideas in notes app."),
        ("Nisha", 23, "Ahmedabad", "design,figma,uiux",
         "Pixel perfectionist who adjusts padding in her sleep."),
        ("Arjun", 21, "Mysore", "reading,manga,tea",
         "Tea > coffee, manga > textbooks. Still somehow passes exams.")
    ]

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executemany("""
        INSERT INTO user_profiles (name, age, location, interests, bio)
        VALUES (?, ?, ?, ?, ?)
    """, profiles)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    seed_profiles()