def numbers(prompt):
	return [int(word) for word in input(prompt).split()]


def run(action):
	try:
		action()
	except EOFError:
		print("Ввод завершён.")
		return False
	except (ValueError, ArithmeticError, RecursionError) as error:
		print(f"Ошибка: {error}")
	return True


def selection_sort(values):
	for start in range(len(values) - 1):
		smallest = start
		for i in range(start + 1, len(values)):
			if values[i] < values[smallest]:
				smallest = i
		if smallest != start:
			values[start], values[smallest] = values[smallest], values[start]


def main():
	values = numbers("Целые числа через пробел: ")
	selection_sort(values)
	print("Результат:")
	print(*values)


def repeat():
	while run(main):
		if input("Enter — повторить, 0 — выйти: ").strip() == "0":
			return


if __name__ == "__main__":
	run(repeat)
