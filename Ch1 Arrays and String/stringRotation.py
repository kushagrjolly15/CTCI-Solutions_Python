##Innovative solution
def stringRotation(s1, s2):
	if len(s2) != len(s1):
		return False
	s1 =  s1 + s1
	if s2 in s1:
		return True
	else:
		return False
	
if __name__ == '__main__':
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(stringRotation(s1,s2))