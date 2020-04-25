#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def isPalindrome(s):
	filter_char = filter(lambda c: c.isalnum(), s)
	lower_filter_char = map(lambda x:x.lower(), filter_char)
	filter_list = list(lower_filter_char)
	reversed_list = filter_list[::-1]
	return filter_list == reversed_list

if __name__ == "__main__":
  import sys
  print(isPalindrome(sys.argv[-1]))