# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(s1):
	chars = s1.split()
	anchor = write = 0
	for read, c in enumerate(chars):
			if read + 1 == len(chars) or chars[read + 1] != c:
				chars[write] = chars[anchor]
				write += 1
				if read > anchor:
					for digit in str(read - anchor + 1):
						chars[write] = digit
						write += 1
				anchor = read + 1
	return write


if __name__ == "__main__":
  import sys
  print(string_compression(sys.argv[-1]))