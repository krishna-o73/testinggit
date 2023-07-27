import string

str = input()

small = string.ascii_lowercase

big = string.ascii_uppercase

res = ""

for i in str:

	if i in small:

		index = small.index(i)

		index = ((index-2)+26)%26

		res+=small[index]

	elif i in big:

		index= big.index(i)

		index = ((index-3)+26)%26

		res+=big[index]

	else:
		res+=i
print(res,end="")
