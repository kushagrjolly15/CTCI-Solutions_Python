# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away


def one_away(s1, s2):
	if abs(len(s1) - len(s2)) > 1:
		return False
	elif abs(len(s1) - len(s2)) == 0:
		difference_count = 0
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				difference_count += 1
			if difference_count > 1:
				return False
		return True
	else:
		if len(s1) < len(s2):
			s1, s2 = s2, s1
		shift = 0
		for i in range(len(s2)):
			if s2[i] != s1[i + shift]:
				if shift or (s2[i] != s1[i + 1]):
					return False
				shift = 1
		return True


if __name__ == "__main__":
  import sys
  print(one_away(sys.argv[-1], sys.argv[-2]))