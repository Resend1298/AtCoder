# TODO: review

def main():
	t = int(input())
	for _ in range(t):
		k = int(input())
		for i in range(1, 101):
			if "00" in str(k * i):
				print(k * i)
				break


if __name__ == "__main__":
	main()
