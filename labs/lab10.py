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


def binary_search(values, target):
	left, right = 0, len(values) - 1
	while left <= right:
		middle = (left + right) // 2
		middle_value = values[middle]
		if middle_value == target:
			return middle
		if middle_value > target:
			right = middle - 1
		else:
			left = middle + 1
	return -1


def main():
	values = numbers("Целые числа по неубыванию: ")
	if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
		raise ValueError("Массив должен быть отсортирован по неубыванию.")
	target = int(input("Искомое число: "))
	print("Индекс:", binary_search(values, target))


def repeat():
	while run(main):
		if input("Enter — повторить, 0 — выйти: ").strip() == "0":
			return


if __name__ == "__main__":
	run(repeat)
