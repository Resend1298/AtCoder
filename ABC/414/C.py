# TODO: review

# Python3 Program for Checking double
# base Palindrome.

# Function generates even and 
# odd palindromes 
def makePalindrome(n, odd):
	res = n;
	if (odd):
		n = int(n / 10);
	while (n > 0):
		res = 10 * res + n % 10;
		n = int(n / 10);
	return res;


# Check if a number is palindrome
# in base k 
def isPalindrome(n, base):
	reversed = 0;
	temp = n;
	while (temp > 0):
		reversed = reversed * base + temp % base;
		temp = int(temp / base);

	return reversed == n;


# function to print sum of Palindromes
def sumPalindrome(n, k):
	sum = 0;
	i = 1;

	p = makePalindrome(i, True);

	# loop for odd generation of
	# odd palindromes
	while (p < n):
		if (isPalindrome(p, k)):
			sum += p;
		i += 1;

		p = makePalindrome(i, True);

	i = 1;

	# loop for generation of
	# even palindromes
	p = makePalindrome(i, False);
	while (p < n):
		if (isPalindrome(p, k)):
			sum += p;
		i += 1;
		p = makePalindrome(i, False);

	# result of all palindromes in
	# both bases.
	print(sum)


# Driver code
a = int(input())
n = int(input())
sumPalindrome(n + 1, a)

# This code is contributed by mits
