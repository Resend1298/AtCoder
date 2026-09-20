# TODO: review

def main():
	n = int(input())
	s = input()
	t = input()

	for i in range(n):
		if s[i] != t[i] and t[i] != '*':
			print("No")
			break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
