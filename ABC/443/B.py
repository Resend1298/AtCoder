# TODO: review

def main():
	n, k = [int(i) for i in input().split()]

	current_sum = 0
	for i in range(10 ** 100):
		current_sum += n + i
		if current_sum >= k:
			print(i)
			exit()


if __name__ == "__main__":
	main()
