# TODO: review

def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	x = int(input())

	if x in a:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
