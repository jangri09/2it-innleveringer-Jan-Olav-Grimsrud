import time

print("Dette vil bli slettet.")
time.sleep(2)

# Flytt opp én linje og slett linjen
print("\033[F\033[K", end="")

print("Dette er den nye teksten.")