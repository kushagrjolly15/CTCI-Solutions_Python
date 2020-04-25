# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.def URLify(s):
	s = s.strip()
	s = s.replace(' ','%20')
	return s

if __name__ == "__main__":
  import sys
  print(URLify(sys.argv[-1]))