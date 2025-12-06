# 💬 Icebreaker AI

Icebreaker AI is an intelligent conversation starter generator that creates **personalized, context-aware, and safe opening messages** between two matched users — similar to features seen in modern dating apps.

Instead of generic messages like *“Hey”* or *“What’s up?”*, Icebreaker AI analyzes user profiles and generates meaningful, friendly, and relevant messages using the Gemini API.

---

## 🚀 What This Project Does

- Reads two user profiles from a SQLite database  
- Uses Google's Gemini model to generate personalized icebreakers  
- Generates messages **from User A → User B** and **from User B → User A**  
- Filters unsafe or inappropriate messages including:  
  - Phone numbers or social media requests  
  - Explicit or offensive content  
  - Overly personal or intrusive questions  

---



## 🧠 Example Output
json
{
  "user_a": {
    "name": "Aarav",
    "icebreakers_to_send": [
      "Hey Priya! You're into anime — any beginner recommendations?",
      "We both love coffee. What’s your usual order?",
      "CS + cafés is a lifestyle — right?"
    ]
  },
  "user_b": {
    "name": "Priya",
    "icebreakers_to_send": [
      "Hey Aarav! Hackathons sound fun — done any recently?",
      "Coimbatore café scene any good?",
      "We might have similar music taste — got playlist suggestions?"
    ]
  }

}
'''


⚙️ Setup & Running the Project
1️⃣ Clone the repository
git clone https://github.com/<your-username>/icebreaker-ai.git
cd icebreaker-ai

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create the .env file

Create a file named .env in the root directory:

GOOGLE_API_KEY=your_gemini_api_key_here


⚠️ .env is already ignored in .gitignore — do NOT commit your API key.

4️⃣ Generate sample users
python db/seed_profiles.py

5️⃣ Run the project
python src/main.py

🔒 Safety Features

Icebreaker AI includes a safety layer to ensure generated messages follow platform-safe rules by removing:

Requests for personal contact info (Instagram, WhatsApp, phone numbers)

Harassment, toxicity, or inappropriate tone

Intrusive personal questions

The final output is friendly, respectful, fun, and comfortable to receive.

🛠 Built With

🐍 Python

🤖 Google Gemini API

🗄 SQLite

🔐 Python dotenv

