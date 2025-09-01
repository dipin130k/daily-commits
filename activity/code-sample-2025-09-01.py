# Daily Code Sample
from datetime import datetime
import random

def generate_daily_insight():
    """Generate a random programming insight."""
    insights = [
        "Clean code is not written by following a set of rules, but by carefully considering readability.",
        "The best programs are written when the programmer is in a state of flow.",
        "Code is read more often than it's written.",
        "Debugging is twice as hard as writing the code in the first place."
    ]
    
    return {
        'insight': random.choice(insights),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'language': 'Python'
    }

if __name__ == "__main__":
    daily = generate_daily_insight()
    print(f"Today's insight ({daily['date']}): {daily['insight']}")
