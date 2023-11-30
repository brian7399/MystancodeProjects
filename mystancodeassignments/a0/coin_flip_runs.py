"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	print("Let's flip a coin!")
	run = int(input("Number of runs: "))
	dice = " "
	dice += str(coin())
	count = 0

	while count < run:
		current_coin = coin()
		dice += current_coin
		if current_coin != dice[-2]:
			count += 1
	current_coin = coin()
	dice += current_coin
	if current_coin == dice[-2]:
		pass
	print(dice)


def coin():
	roll = r.randrange(1, 3)
	if roll == 1:
		return "T"
	else:
		return "H"

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
