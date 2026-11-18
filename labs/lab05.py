def integer(prompt, minimum=None, maximum=None):
	value = int(input(prompt))
	if minimum is not None and value < minimum:
		raise ValueError(f"Число должно быть не меньше {minimum}.")
	if maximum is not None and value > maximum:
		raise ValueError(f"Число должно быть не больше {maximum}.")
	return value


def real(text):
	value = float(text.replace(",", "."))
	if not -float("inf") < value < float("inf"):
		raise ValueError("Введите конечное число.")
	return value


def numbers(prompt, convert=real, count=None):
	values = [convert(word) for word in input(prompt).split()]
	if count is not None and len(values) != count:
		raise ValueError(f"Нужно ввести {count} чисел.")
	return values


def run(action):
	try:
		action()
	except EOFError:
		print("Ввод завершён.")
		return False
	except (ValueError, ArithmeticError, RecursionError) as error:
		print(f"Ошибка: {error}")
	return True


def menu(tasks):
	for index, (title, _) in enumerate(tasks, 1):
		print(f"{index}. {title}")
	previous = None
	while True:
		try:
			choice = input("Номер задачи (Enter — повтор, 0 — выход): ").strip()
			if choice == "" and previous is not None:
				index = previous
			else:
				index = int(choice)
			if not 0 <= index <= len(tasks):
				raise ValueError
		except EOFError:
			print("Ввод завершён.")
			return
		except ValueError:
			print(f"Введите номер задачи от 1 до {len(tasks)} или 0 для выхода.")
			continue
		if index == 0:
			return
		previous = index
		if not run(tasks[index - 1][1]):
			return


def read_array(convert=int, minimum=1):
	values = numbers("Элементы массива через пробел: ", convert)
	if len(values) < minimum:
		raise ValueError(f"Нужно хотя бы {minimum} элементов.")
	return values


def odds():
	n = integer("N > 0: ", 1)
	values = list(range(1, 2 * n, 2))
	print(*values)


def geometric():
	n = integer("N > 1: ", 2)
	value, ratio = numbers("Первый член A и знаменатель D: ", count=2)
	values = [value]
	for _ in range(n - 1):
		value *= ratio
		values.append(value)
	print(*values)


def sum_of_previous():
	n = integer("N > 2: ", 3)
	a, b = numbers("Целые A B: ", int, 2)
	values = [a, b]
	total = a + b
	for _ in range(n - 2):
		values.append(total)
		total += values[-1]
	print(*values)


def alternating_ends():
	values = read_array(real)
	left, right = 0, len(values) - 1
	result = []
	while left < right:
		result.extend((values[left], values[right]))
		left += 1
		right -= 1
	if left == right:
		result.append(values[left])
	print(*result)


def odd_then_even():
	values = read_array(real)
	print(values[0], end="")
	for index in range(2, len(values), 2):
		print("", values[index], end="")
	last_even = len(values) - 1
	if last_even % 2 == 0:
		last_even -= 1
	for index in range(last_even, 0, -2):
		print("", values[index], end="")
	print()


def segment_mean():
	values = read_array(real)
	k = integer("Номер K: ", 1, len(values))
	last = integer("Номер L: ", k, len(values))
	total = 0
	for index in range(k - 1, last):
		total += values[index]
	print(total / (last - k + 1))


def arithmetic_difference():
	values = read_array(minimum=2)
	if len(set(values)) != len(values):
		raise ValueError("Числа должны быть различными.")
	difference = values[1] - values[0]
	for i in range(2, len(values)):
		if values[i] - values[i - 1] != difference:
			print(0)
			return
	print(difference)


def even_minimum():
	values = read_array(real, minimum=2)
	smallest = values[1]
	for index in range(3, len(values), 2):
		if values[index] < smallest:
			smallest = values[index]
	print(smallest)


def last_local_maximum():
	values = read_array(real)
	for i in range(len(values) - 1, -1, -1):
		left_ok = i == 0 or values[i] > values[i - 1]
		right_ok = i == len(values) - 1 or values[i] > values[i + 1]
		if left_ok and right_ok:
			print(i + 1)
			return
	print("Локального максимума нет.")


def equal_positions():
	values = read_array(minimum=2)
	seen = {}
	pair = None
	for index, value in enumerate(values, 1):
		if value in seen:
			if pair is not None:
				raise ValueError("Допускается ровно одна пара одинаковых элементов.")
			pair = (seen[value], index)
		else:
			seen[value] = index
	if pair is None:
		raise ValueError("Одинаковых элементов нет.")
	print(*pair)


if __name__ == "__main__":
	menu([
		("Первые N нечётных", odds), ("Геометрическая прогрессия", geometric),
		("Сумма предыдущих элементов", sum_of_previous), ("Вывод с двух концов", alternating_ends),
		("Нечётные номера, затем чётные", odd_then_even), ("Среднее на отрезке K–L", segment_mean),
		("Арифметическая прогрессия", arithmetic_difference), ("Минимум на чётных местах", even_minimum),
		("Последний локальный максимум", last_local_maximum), ("Номера одинаковых элементов", equal_positions),
	])
