def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	prefix_sum = [0]
	for i in a:
		prefix_sum.append(prefix_sum[-1] + i)

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x:
				x -= 1
				a[x], a[x + 1] = a[x + 1], a[x]
				prefix_sum[x + 1] = prefix_sum[x] + a[x]
			case 2, l, r:
				l -= 1
				r -= 1
				print(prefix_sum[r + 1] - prefix_sum[l])


if __name__ == "__main__":
	main()
