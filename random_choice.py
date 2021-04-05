import random

wordlist_path = './wordlist.txt'

with open(wordlist_path, 'r') as f:
	words = f.read()
words = words.split('\n')


def choose_a_word():
	return words[random.randrange(0, len(words))]

if __name__ == '__main__':
	print(choose_a_word())