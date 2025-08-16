from collections import deque


def main():
	n, m, l = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	current_sum = sum(a[:l])
	slot = deque([(current_sum // m + 1) * m - current_sum])
	result = 0

	for i in range(l, n):
		current_sum += a[i]
		current_sum -= a[i - l]
		new = (current_sum // m + 1) * m - current_sum

		if len(slot) < l and new >= slot[-1]:
			slot.append(new)
			continue

		tmp = slot.popleft()
		if tmp % m != 0:
			result += tmp
			for j in range(len(slot)):
				slot[j] -= tmp
				if slot[j] < 0:
					slot[j] = m + slot[j]
		slot.append(new)

	while slot:
		tmp = slot.popleft()
		if tmp % m != 0:
			result += tmp
			for i in range(len(slot)):
				slot[i] -= tmp
				if slot[i] < 0:
					slot[i] = m + slot[i]

	print(result)


if __name__ == "__main__":
	main()
