from sortedcontainers import SortedList


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	sorted_start = [False] * n
	sorted_end = [False] * n
	sorted_start[0] = True
	for i in range(1, n):
		if a[i] >= a[i - 1]:
			sorted_start[i] = True
		else:
			break
	sorted_end[-1] = True
	for i in range(n - 2, -1, -1):
		if a[i] <= a[i + 1]:
			sorted_end[i] = True
		else:
			break

	current = SortedList(a[:k])
	if sorted_end[k] and current[-1] <= a[k]:
		print("Yes")
		exit()

	for left_pop in range(n - k):
		current.remove(a[left_pop])
		current.add(a[left_pop + k])
		if sorted_start[left_pop] and (left_pop + k + 1 >= n or sorted_end[left_pop + k + 1]) and a[left_pop] <= \
				current[0] and (left_pop + k + 1 >= n or current[-1] <= a[
			left_pop + k + 1]):
			print("Yes")
			exit()

	print("No")


if __name__ == "__main__":
	main()
