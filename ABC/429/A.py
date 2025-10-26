# TODO: review

def main():
	n, m = [int(i) for i in input().split()]

	for i in range(1, n + 1):
		if i <= m:
			print("OK")
		else:
			print("Too Many Requests")


if __name__ == "__main__":
	main()
