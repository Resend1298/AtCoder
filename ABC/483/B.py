# TODO: review

def main():
	n, q = [int(i) for i in input().split()]
	k = [int(i) for i in input().split()]

	cards = [i for i in range(1, n + 1)]

	for i in k:
		cards[:i] = cards[i - 1::-1]
		for j in range(i):
			cards[j] = -cards[j]

	for i in cards:
		print(i)


if __name__ == "__main__":
	main()
