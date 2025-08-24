def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	current_sum = 0
	for i in range(n):
		current_sum += min(a[i], b[i])

	for _ in range(q):
		c, x, v = input().split()
		x, v = int(x) - 1, int(v)

		match c:
			case 'A':
				current_sum -= min(a[x], b[x])
				a[x] = v
				current_sum += min(a[x], b[x])
				print(current_sum)
			case 'B':
				current_sum -= min(a[x], b[x])
				b[x] = v
				current_sum += min(a[x], b[x])
				print(current_sum)


if __name__ == "__main__":
	main()
