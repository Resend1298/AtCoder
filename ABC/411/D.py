def main():
	n, q = [int(i) for i in input().split()]
	query = [input().split() for _ in range(q)][::-1]

	result = []
	searching_3 = True

	for i in query:
		if searching_3:
			if i[0] == '3':
				current_pc = i[1]
				searching_3 = False
		else:
			# noinspection PyUnboundLocalVariable
			if i[0] == '2' and i[1] == current_pc:
				result.append(i[2])
			elif i[0] == '1' and i[1] == current_pc:
				searching_3 = True

	print(''.join(result[::-1]))


if __name__ == "__main__":
	main()
