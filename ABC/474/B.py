# TODO: review

def main():
	n = int(input())
	p = [int(i) for i in input().split()]

	for i in range(n):
		if i // 10 * 10 <= p[i] - 1 <= (i // 10 + 1) * 10 - 1:
			continue
		else:
			print("No")
			break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
