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


def bubble_sort(values):
	for end in range(len(values) - 1, 0, -1):
		swapped = False
		for i in range(end):
			if values[i] > values[i + 1]:
				values[i], values[i + 1] = values[i + 1], values[i]
				swapped = True
		if not swapped:
			break


def main():
	values = numbers("Целые числа через пробел: ")
	bubble_sort(values)
	print("Результат:")
	print(*values)


def repeat():
	while run(main):
		if input("Enter — повторить, 0 — выйти: ").strip() == "0":
			return


if __name__ == "__main__":
	run(repeat)
