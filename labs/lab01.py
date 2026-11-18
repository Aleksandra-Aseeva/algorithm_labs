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


def length(dx, dy):
	return (dx ** 2 + dy ** 2) ** 0.5


def rectangle():
	a, b = numbers("Стороны a b: ", count=2)
	print("Площадь:", a * b, "Периметр:", 2 * (a + b))


def circle():
	diameter = real(input("Диаметр: "))
	circumference = 3.14 * diameter
	print(f"{circumference:.12g}")


def average():
	values = numbers("Числа a b: ", count=2)
	first = values[0]
	second = values[1]
	total = first + second
	print(total / 2)


def operations(a, b):
	print("Сумма, разность, произведение, частное:")
	print(*(a + b, a - b, a * b, a / b))


def squares():
	a, b = numbers("Два ненулевых числа: ", count=2)
	operations(a ** 2, b ** 2)


def absolute_values():
	a, b = numbers("Два ненулевых числа: ", count=2)
	operations(abs(a), abs(b))


def distance():
	x1, y1, x2, y2 = numbers("Координаты x1 y1 x2 y2: ", count=4)
	print(length(x2 - x1, y2 - y1))


def segment_sum():
	a, b, c = numbers("Координаты A B C: ", count=3)
	ac, bc = abs(a - c), abs(b - c)
	print(*(ac, bc, ac + bc))


def segment_product():
	a, b, c = numbers("Координаты A B C (C между A и B): ", count=3)
	print(abs(a - c) * abs(b - c))


def rectangle_vertices():
	x1, y1, x2, y2 = numbers("Координаты x1 y1 x2 y2: ", count=4)
	width, height = abs(x2 - x1), abs(y2 - y1)
	print("Периметр:", 2 * (width + height), "Площадь:", width * height)


def triangle():
	x1, y1, x2, y2, x3, y3 = numbers("Координаты x1 y1 x2 y2 x3 y3: ", count=6)
	perimeter = length(x2 - x1, y2 - y1) + length(x3 - x2, y3 - y2) + length(x1 - x3, y1 - y3)
	area = abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) / 2
	print("Периметр:", perimeter, "Площадь:", area)


def polynomial():
	x, = numbers("x: ", count=1)
	print(3 * x ** 6 - 6 * x ** 2 - 7)


def shifted_polynomial():
	x, = numbers("x: ", count=1)
	shifted = x - 3
	print(4 * shifted ** 6 - 7 * shifted ** 3 + 2)


if __name__ == "__main__":
	menu([
		("Площадь и периметр прямоугольника", rectangle),
		("Длина окружности", circle),
		("Среднее двух чисел", average),
		("Операции с квадратами", squares),
		("Операции с модулями", absolute_values),
		("Расстояние между точками", distance),
		("Длины отрезков и их сумма", segment_sum),
		("Произведение длин отрезков", segment_product),
		("Прямоугольник по вершинам", rectangle_vertices),
		("Периметр и площадь треугольника", triangle),
		("Полином от x", polynomial),
		("Полином от x − 3", shifted_polynomial),
	])
