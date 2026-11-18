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


UNITS = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять")
TEENS = ("десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
	"пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать")
TENS = ("", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят",
		"семьдесят", "восемьдесят", "девяносто")
HUNDREDS = ("", "сто", "двести", "триста", "четыреста", "пятьсот",
			"шестьсот", "семьсот", "восемьсот", "девятьсот")
DAYS = ("первое", "второе", "третье", "четвертое", "пятое", "шестое",
		"седьмое", "восьмое", "девятое", "десятое", "одиннадцатое",
		"двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое",
		"шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое")
MONTHS = ("января", "февраля", "марта", "апреля", "мая", "июня", "июля",
	"августа", "сентября", "октября", "ноября", "декабря")


def equalize():
	a, b = numbers("Целые A B: ", int, 2)
	if a > b:
		b = a
	elif a < b:
		a = b
	else:
		a = b = 0
	print(*(a, b))


def two_largest():
	a, b, c = numbers("Три числа: ", count=3)
	if a <= b and a <= c:
		print(b + c)
	elif b <= c:
		print(a + c)
	else:
		print(a + b)


def nearest():
	ax, ay, bx, by, cx, cy = numbers("Координаты Ax Ay Bx By Cx Cy: ", count=6)
	ab = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
	ac = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5
	if ab < ac:
		print(f"B ({bx}, {by}), расстояние {ab}")
	elif ac < ab:
		print(f"C ({cx}, {cy}), расстояние {ac}")
	else:
		print(f"B ({bx}, {by}) и C ({cx}, {cy}) равноудалены. Расстояние {ab}")


def quadrant():
	x, y = numbers("Координаты x y: ", count=2)
	if x == 0 or y == 0:
		raise ValueError("Точка лежит на оси.")
	if y > 0:
		print(1 if x > 0 else 2)
	else:
		print(4 if x > 0 else 3)


def parity(number):
	return "четное" if number % 2 == 0 else "нечетное"


def signed_description():
	number = integer("Целое число: ")
	if number == 0:
		print("нулевое число")
	else:
		sign = "положительное" if number > 0 else "отрицательное"
		print(sign, parity(number), "число")


def length_description():
	number = integer("Число от 1 до 999: ", 1, 999)
	kinds = ("однозначное", "двузначное", "трехзначное")
	print(parity(number), kinds[len(str(number)) - 1], "число")


def date_words():
	day, month = numbers("Номера дня и месяца: ", int, 2)
	if not 1 <= month <= 12:
		raise ValueError("Месяц должен быть от 1 до 12.")
	limits = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	if not 1 <= day <= limits[month - 1]:
		raise ValueError("В этом месяце нет такого дня.")
	if day <= 20:
		word = DAYS[day - 1]
	elif day < 30:
		word = "двадцать " + DAYS[day - 21]
	elif day == 30:
		word = "тридцатое"
	else:
		word = "тридцать первое"
	print(word, MONTHS[month - 1])


def number_words(number):
	hundreds = number // 100
	rest = number % 100
	words = []
	if hundreds > 0:
		words.append(HUNDREDS[hundreds])
	if 10 <= rest <= 19:
		words.append(TEENS[rest - 10])
	else:
		tens = rest // 10
		units = rest % 10
		if tens > 0:
			words.append(TENS[tens])
		if units > 0:
			words.append(UNITS[units])
	return " ".join(words)


def assignment_count():
	number = integer("Количество заданий от 10 до 40: ", 10, 40)
	units = number % 10
	if 11 <= number <= 14 or units == 0 or units >= 5:
		ending = "учебных заданий"
	elif units == 1:
		ending = "учебное задание"
	else:
		ending = "учебных задания"
	print(number_words(number), ending)


def three_digits():
	print(number_words(integer("Число от 100 до 999: ", 100, 999)))


def eastern_year():
	year = integer("Год: ")
	animals = ("крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
		"лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи")
	masculine = ("зеленого", "красного", "желтого", "белого", "черного")
	feminine = ("зеленой", "красной", "желтой", "белой", "черной")
	color, animal = divmod((year - 1984) % 60, 12)
	colors = masculine if animal in (2, 3, 4) else feminine
	print("год", colors[color], animals[animal])


if __name__ == "__main__":
	menu([
		("Новые значения A и B", equalize), ("Сумма двух наибольших", two_largest),
		("Ближайшая точка", nearest), ("Координатная четверть", quadrant),
		("Знак и четность числа", signed_description), ("Четность и разрядность", length_description),
		("Дата словами", date_words), ("Количество заданий словами", assignment_count),
		("Трехзначное число словами", three_digits), ("Восточный календарь", eastern_year),
	])
