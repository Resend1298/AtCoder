from math import ceil


def main():
	n, k, t = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = 0
	a = set(i for i in a if i <= t)
	a = sorted(a)

	if not a:
		print(ceil(t / k))
		exit()

	if a[0] != 0:
		result += ceil(a[0] / k)
		current = k * result
	else:
		current = 0

	for i in a:
		if current < i:
			result += ceil((i - current) / k)
			current += ceil((i - current) / k) * k
		current = max(current, i + k)

	if current < t:
		result += ceil((t - current) / k)

	print(result)


if __name__ == "__main__":
	main()
