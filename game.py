import random
import time

def 🧠_Mystery_Mind_Reader_3000():
    print("""
    🔮✨ MYSTERY MIND READER 3000 ✨🔮
    Can you outsmart the psychic computer?
    I'll read your mind... through numbers!
    Guess my secret number (1-100) to win cosmic bragging rights!
    """)
    
    secret = random.randint(1, 100)
    attempts = 0
    difficulty = input("Choose your fate:\n1. Novice (10 tries)\n2. Adept (7 tries)\n3. Psychic (5 tries)\n> ")
    max_attempts = {"1":10, "2":7, "3":5}.get(difficulty, 7)
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n⚡ Attempt {attempts+1}/{max_attempts}\nYour guess: "))
            attempts += 1
            
            if guess == secret:
                print(f"\n🌌 WHOA! You broke the matrix in {attempts} tries!")
                print("The cosmic forces bow to your numerical intuition!")
                return
                
            diff = abs(secret - guess)
            if diff <= 5:
                print("🔥 Burning hot! Almost there!")
            elif diff <= 15:
                print("💨 Warm... getting closer!")
            elif guess < secret:
                print(f"⬆️ Higher! {random.choice(['Is that your final answer?','Trust your instincts!'])}")
            else:
                print(f"⬇️ Lower! {random.choice(['The numbers deceive you...','Focus your third eye!'])}")
                
        except ValueError:
            print("⚠️ The crystal ball only understands numbers!")
    
    print(f"\n💀 GAME OVER! The secret was {secret}")
    print("The computer absorbs your mental energy... better luck next time!")

🧠_Mystery_Mind_Reader_3000()
