import sys
import time
def print_lyrics():
    lyrics = [
        ("Forget about where we are and let go", 0.13),
        ("We're so close If you don't know ",0.13),
        ("where to start",0.19),
        ("Just hold on and don't run",0.13),
        ("It's up to you, and it's up to me",0.13),
        ("No one could say what we get to be", 0.10),
        ("And why don't we rewrite the stars?", 0.13),
        ("Changin' the world to be ours......", 0.13),
        ("We're looking back, we messed around..", 0.13),
        ("But that was then and this is now..", 0.08),
        ("All we need is enough love to hold us......", 0.15),
        ("WHERE WE ARE...", 0.06),
    ]
    delay = [0.0001, 0.0001, 0.0001, 0.0001,0.0001, 0.0001,0.0001, 0.0001,0.0001, 0.0001,0.0001,]
    print("\n==Rewrite the star x where we are==")
    time.sleep(0.01)
    for i, (line, delay) in enumerate(lyrics):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # newline after each line
if __name__ == "__main__":
    print_lyrics()