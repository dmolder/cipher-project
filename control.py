"""
Main file, import necessary ciphers as needed
"""
import sys
from caesar import caesar_cipher
from shuffle import shuffle

CIPHER = str(input("Enter cipher:"))
print("")
def analyze(intake: str):
    """
    Initial analysis on start-up. Frequency analysis (or others)
    to determine most likely cipher used.

    The function accepts following parameters:
    1. STRING intake
    """
    if len(intake) < 100:
        print("Analysis inconclusive - sample too small")


analyze(CIPHER)
while True:
    try:
        print(f"Current cipher: {CIPHER}")
        MODE = int(input("""
Please select a tool, or Ctrl+Z, then Return to exit:
1 - Caesar cipher
2 - Shuffle
"""))
    except EOFError:
        exit()
    if MODE == 1:
        SHIFT = int(input("Key Amount?"))
        print(f"Output string: {caesar_cipher(CIPHER,SHIFT)}")
        print("")
        REPLACE = str(input("Replace cipher(Y/N)?\n"))
        if (REPLACE == 'Y') or (REPLACE == 'y'):
            CIPHER = caesar_cipher(CIPHER,SHIFT)
        continue
    elif MODE == 2:
        SHIFT = int(input("Shuffle size?"))
        print(f"Output string: {shuffle(CIPHER,SHIFT)}")
        print("")
        REPLACE = str(input("Replace cipher(Y/N)?\n"))
        if (REPLACE == 'Y') or (REPLACE == 'y'):
            CIPHER = shuffle(CIPHER,SHIFT)
        continue
    else:
        exit()
