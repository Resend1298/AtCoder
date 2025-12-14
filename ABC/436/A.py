# TODO: review

def main():
	n = int(input())
	s = input()

	o_count = n - len(s)
	print('o' * o_count + s)


if __name__ == "__main__":
	main()
