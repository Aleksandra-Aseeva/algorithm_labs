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


def insertion_sort(values):
	for i in range(1, len(values)):
		current = values[i]
		position = i
		while position > 0 and values[position - 1] > current:
			values[position] = values[position - 1]
			position -= 1
		values[position] = current


def main():
	values = numbers("Целые числа через пробел: ")
	insertion_sort(values)
	print("Результат:")
	print(*values)


def repeat():
	while run(main):
		if input("Enter — повторить, 0 — выйти: ").strip() == "0":
			return


if __name__ == "__main__":
	run(repeat)
