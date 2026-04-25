from collections import Counter


def main():
	n = int(input())
	s = input()

	ab_count = 0
	current = 0
	pre = Counter({0: 1})
	for i in s:
		if i == 'A':
			current += 1
		elif i == 'B':
			current -= 1
		ab_count += pre[current]
		pre[current] += 1

	bc_count = 0
	current = 0
	pre = Counter({0: 1})
	for i in s:
		if i == 'B':
			current += 1
		elif i == 'C':
			current -= 1
		bc_count += pre[current]
		pre[current] += 1

	ac_count = 0
	current = 0
	pre = Counter({0: 1})
	for i in s:
		if i == 'A':
			current += 1
		elif i == 'C':
			current -= 1
		ac_count += pre[current]
		pre[current] += 1

	abc_count = 0
	current = [0, 0]
	pre = Counter({(0, 0): 1})
	for i in s:
		if i == 'A':
			current[0] += 1
		elif i == 'B':
			current[0] -= 1
			current[1] += 1
		elif i == 'C':
			current[1] -= 1
		abc_count += pre[tuple(current)]
		pre[tuple(current)] += 1

	print(n * (n + 1) // 2 - ab_count - bc_count - ac_count + abc_count * 2)


if __name__ == "__main__":
	main()
