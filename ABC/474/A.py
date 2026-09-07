# TODO: review

def main():
	x = int(input())

	tmp = set(range(1, 4))
	tmp.remove(x)

	print(tmp.pop())


if __name__ == "__main__":
	main()
