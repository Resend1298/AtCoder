def main():
	q = int(input())

	name_to_id = {}
	next_id = 1

	for _ in range(q):
		s = input()

		if s in name_to_id:
			print(name_to_id[s])
		else:
			name_to_id[s] = next_id
			print(next_id)
			next_id += 1


if __name__ == "__main__":
	main()
