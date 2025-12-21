def main():
	h, w, n = [int(i) for i in input().split()]
	a = [{int(i) for i in input().split()} for _ in range(h)]
	b = {int(input()) for _ in range(n)}

	print(max(len(i & b) for i in a))


if __name__ == "__main__":
	main()
