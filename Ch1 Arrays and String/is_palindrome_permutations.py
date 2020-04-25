# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
import collections


def is_palindrome_permutations(s):
	counter = collections.Counter(s.lower().replace(' ',''))
	print(counter.items())
	odd_counts = [cha for cha, count in counter.items() if count % 2 == 1]
	print(odd_counts)
	return len(odd_counts) <= 1

if __name__ == "__main__":
  import sys
  print(is_palindrome_permutations(sys.argv[-1]))