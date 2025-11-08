# PyPy TLE, CPython AC

def solve():
	a = input()
	b = input()

	a *= 2
	print(a.find(b))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
