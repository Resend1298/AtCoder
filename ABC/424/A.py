# TODO: review

def main():
	abc = [int(i) for i in input().split()]

	abc.sort()

	if abc[0] == abc[1] or abc[1] == abc[2]:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
