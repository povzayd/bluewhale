import random
import datetime

class Challenge:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True
        return f"Challenge completed: {self.description}"

class PositivePathGame:
    def __init__(self):
        self.challenges = [
            "Take a 30-minute walk in nature.",
            "Write a positive message to a friend.",
            "Read a chapter of a book.",
            "Try a new healthy recipe.",
            "Spend 15 minutes meditating.",
            "Draw or doodle something creative.",
            "Watch a documentary on a topic you are curious about.",
            "Spend an hour learning a new skill online.",
            "Do a random act of kindness for someone.",
            "Write down three things you're grateful for."
        ]
        self.daily_challenge = None
        self.start_date = datetime.date.today()

    def get_random_challenge(self):
        if not self.daily_challenge or self.daily_challenge.completed:
            self.daily_challenge = Challenge(random.choice(self.challenges))
        return self.daily_challenge.description

    def complete_challenge(self):
        if self.daily_challenge:
            return self.daily_challenge.complete()
        else:
            return "No challenge to complete today."

def main():
    game = PositivePathGame()
    print("Welcome to Positive Path!")
    print("Each day you'll receive a positive challenge to complete.")
    print("Let's make today great!\n")

    while True:
        print(f"Today's date: {datetime.date.today()}")
        print(f"Days since start: {(datetime.date.today() - game.start_date).days}\n")

        print("1. Get today's challenge")
        print("2. Complete today's challenge")
        print("3. Exit\n")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            print(f"\nToday's challenge: {game.get_random_challenge()}\n")
        elif choice == '2':
            print(f"\n{game.complete_challenge()}\n")
        elif choice == '3':
            print("Thanks for playing Blue whale! Have a great day!\n")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    main()
