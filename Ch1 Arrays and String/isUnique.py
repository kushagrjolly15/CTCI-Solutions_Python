#Is Unique: Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?

def isUnique(message):
	letters = {}
	for letter in message:
		if letter in letters:
			return False
		letters[letter] = True
	return True



if __name__ == "__main__":
  import sys
  print(isUnique(sys.argv[-1]))