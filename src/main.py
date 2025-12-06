from generator import generate_icebreakers_for_pair
from filter import filter_icebreakers
import os
import sqlite3
from db_utils import get_profile_by_id

DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'profiles.db')

def get_icebreakers_for_match(user_a_id: int, user_b_id: int):
    user_a = get_profile_by_id(user_a_id)
    user_b = get_profile_by_id(user_b_id)

    # A → B
    raw_a = generate_icebreakers_for_pair(sender=user_a, receiver=user_b)
    safe_a = filter_icebreakers(raw_a)

    # B → A
    raw_b = generate_icebreakers_for_pair(sender=user_b, receiver=user_a)
    safe_b = filter_icebreakers(raw_b)
    return {
        "user_a": {
            "id": user_a["id"],
            "name": user_a["name"],
            "icebreakers_to_send": safe_a,   # show this to A
        },
        "user_b": {
            "id": user_b["id"],
            "name": user_b["name"],
            "icebreakers_to_send": safe_b,   # show this to B
        },
    }

if __name__ == "__main__":
    result = get_icebreakers_for_match(1, 2)
    print(result)
