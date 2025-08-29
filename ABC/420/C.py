def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	current_sum = 0
	for i in range(n):
		current_sum += min(a[i], b[i])

	for _ in range(q):
		c, x, v = input().split()
		x = int(x) - 1
		v = int(v)

		current_sum -= min(a[x], b[x])

		match c:
			case 'A':
				a[x] = v
			case 'B':
				b[x] = v

		current_sum += min(a[x], b[x])

		print(current_sum)


if __name__ == "__main__":
	main()
