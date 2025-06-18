def main():
	n, h, m = [int(i) for i in input().split()]
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	current_status = {h: m}

	for i in range(n):
		new_status = {}

		for j, k in current_status.items():
			if j >= ab[i][0]:
				if j - ab[i][0] in new_status:
					new_status[j - ab[i][0]] = max(new_status[j - ab[i][0]], k)
				else:
					new_status[j - ab[i][0]] = k
			if k >= ab[i][1]:
				if j in new_status:
					new_status[j] = max(new_status[j], k - ab[i][1])
				else:
					new_status[j] = k - ab[i][1]

		if new_status:
			current_status = new_status
		else:
			print(i)
			exit()

	print(n)


if __name__ == "__main__":
	main()
