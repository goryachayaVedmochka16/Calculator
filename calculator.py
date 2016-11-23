import os

def calcul(expr):
	if sum([1 for char in expr if char not in "1234567890.+-/*()jJ"]) == 0: # jJ for comlex number (y+xj); y, x of R
		try: print eval(expr)
		except Exception: print 'enter a correct math expression'
	else: print 'enter only a valid calculable expression'

while True:
	print 'Enter an exression to calculate'
	calcul(raw_input())
	os.system('pause')
	os.system('cls')
	# break