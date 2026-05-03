from collections import Counter


def main():
	n, m, c = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a_counter = Counter(a)
	a = sorted(a_counter.items(), key=lambda x: x[0])

	x_from_a = []
	current = 0
	end_index = -1
	for i in range(len(a)):
		if i != 0:
			current -= a[i - 1][1]
		while current < c and end_index + 1 < len(a):
			end_index += 1
			current += a[end_index][1]
		if end_index == len(a) - 1:
			end_index = -1
		while current < c:
			end_index += 1
			current += a[end_index][1]
		x_from_a.append(current)

	result = 0
	for i in range(1, len(a)):
		result += (a[i][0] - a[i - 1][0]) * x_from_a[i]
	result += (m - a[-1][0] + a[0][0]) * x_from_a[0]

	print(result)


if __name__ == "__main__":
	main()
