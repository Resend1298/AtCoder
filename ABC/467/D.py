def solve():
	px, py, qx, qy, rx, ry, sx, sy = [int(i) for i in input().split()]

	if (qx - px) * (sy - ry) == (sx - rx) * (qy - py) and (
			(qx - px) * (rx ** 2 + ry ** 2 - sx ** 2 - sy ** 2) != (sx - rx) * (px ** 2 + py ** 2 - qx ** 2 - qy ** 2)
			or
			(qy - py) * (rx ** 2 + ry ** 2 - sx ** 2 - sy ** 2) != (sy - ry) * (px ** 2 + py ** 2 - qx ** 2 - qy ** 2)
	):
		print("No")
	else:
		print("Yes")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
