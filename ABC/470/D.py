def main():
	n, q = [int(i) for i in input().split()]
	p = [int(i) for i in input().split()]

	next_ = [0] * (n + 1)
	prev = [0] * (n + 1)
	rev = False

	for i in range(n):
		next_[i + 1] = p[i]
		prev[p[i]] = i + 1

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x, y:
				if not rev:
					prev[next_[x]], prev[next_[y]] = prev[next_[y]], prev[next_[x]]
					next_[x], next_[y] = next_[y], next_[x]
				else:
					next_[prev[x]], next_[prev[y]] = next_[prev[y]], next_[prev[x]]
					prev[x], prev[y] = prev[y], prev[x]
			case 2,:
				rev = not rev

	if not rev:
		print(*next_[1:])
	else:
		print(*prev[1:])


if __name__ == "__main__":
	main()
