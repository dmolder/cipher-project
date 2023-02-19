import sys
from caesar import caesar_cypher
from shuffle import shuffle

try:
    CIPHER = sys.argv[1]
except IndexError:
    print("Missing cipher")
    exit()
    
def analyze(intake: str):
    if len(intake) < 100:
        print("Analysis inconclusive - sample too small")
        exit()

analyze(CIPHER)
print(shuffle(caesar_cypher(CIPHER,sys.argv[2]),2))
