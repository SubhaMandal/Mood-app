# Mood-Based Workout or Activity Recommender - Console App

import random



def greet_user():
    print("Welcome to FitMood Buddy!")
    name = input("What's your name? ")
    print(f"Hi {name}! Let's find the perfect activity for your current mood.")
    return name


def get_user_mood():
    print("\nHow are you feeling right now?")
    print("1. Happy")
    print("2. Sad")
    print("3. Tired")
    print("4. Stressed")
    print("5. Bored")
    mood_input = input("Enter the number or name of your mood: ").lower()
    return mood_input


def recommend_activity(mood):
    activities = {
        "1": ["Go for a jog in the park", "Dance to your favorite song", "Invite friends for a group workout"],
        "happy": ["Go for a jog in the park", "Dance to your favorite song", "Invite friends for a group workout"],
        "2": ["Do some light yoga", "Take a walk while listening to music", "Try deep breathing exercises"],
        "sad": ["Do some light yoga", "Take a walk while listening to music", "Try deep breathing exercises"],
        "3": ["Try a 5-minute stretch", "Take a short walk", "Do light breathing exercises"],
        "tired": ["Try a 5-minute stretch", "Take a short walk", "Do light breathing exercises"],
        "4": ["Meditate for 10 minutes", "Try progressive muscle relaxation", "Do some slow-paced yoga"],
        "stressed": ["Meditate for 10 minutes", "Try progressive muscle relaxation", "Do some slow-paced yoga"],
        "5": ["Try a new dance workout on YouTube", "Do a fun HIIT challenge", "Go cycling or play an outdoor game"],
        "bored": ["Try a new dance workout on YouTube", "Do a fun HIIT challenge", "Go cycling or play an outdoor game"]
    }

    if mood in activities:
        suggestion = random.choice(activities[mood])
        print(f"\nBased on your mood, here's a suggestion: {suggestion}")
    else:
        print("\nSorry, I didn't recognize that mood. Please try again.")


def motivational_boost():
    quotes = [
        "You don't have to be extreme, just consistent.",
        "Every step forward is a step toward feeling better.",
        "Take care of your body—it's the only place you have to live.",
        "Your mind will quit 100 times before your body does. Push through."
    ]
    print("\nMotivation Boost:")
    print(random.choice(quotes))


def ask_to_continue():
    choice = input("\nWould you like another recommendation? (yes/no): ").lower()
    return choice == "yes"

# Main function

def run_fitmood_buddy():
    name = greet_user()
    while True:
        mood = get_user_mood()
        recommend_activity(mood)
        motivational_boost()
        if not ask_to_continue():
            print(f"\nThanks for using FitMood Buddy, {name}! Stay active and take care!")
            break

if __name__ == "__main__":
    run_fitmood_buddy()
