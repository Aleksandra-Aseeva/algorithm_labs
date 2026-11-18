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


def candy():
	price, = numbers("Цена килограмма: ", count=1)
	for tenths in range(1, 11):
		weight = tenths / 10
		print(f"{weight:.1f} кг — {price * weight:.2f} руб.")


def product():
	n = integer("N > 0: ", 1)
	result = 1
	for i in range(1, n + 1):
		result *= 1 + i / 10
	print(result)


def square():
	n = integer("N > 0: ", 1)
	total = 0
	for odd in range(1, 2 * n, 2):
		total += odd
		print(total)


def power_sum():
	a, = numbers("A: ", count=1)
	n = integer("N > 0: ", 1)
	term = total = 1
	for _ in range(n):
		term *= a
		total += term
	print(total)


def alternating_sum():
	a, = numbers("A: ", count=1)
	n = integer("N > 0: ", 1)
	term = total = 1
	for _ in range(n):
		term *= -a
		total += term
	print(total)


def repeated_numbers():
	a, b = numbers("Целые 0 < A < B: ", int, 2)
	if not 0 < a < b:
		raise ValueError("Нужно 0 < A < B.")
	for value in range(a, b + 1):
		for _ in range(value):
			print(value, end=" ")
		print()


def decimal_parts(text):
	if text.startswith("+"):
		text = text[1:]
	mantissa, separator, exponent = text.lower().replace(",", ".").partition("e")
	whole, _, fraction = mantissa.partition(".")
	digits = whole + fraction
	if not digits.isdecimal():
		raise ValueError("Введите положительную длину.")
	point = len(whole) + (int(exponent) if separator else 0)
	if point < 0:
		return "", "0" * (-point) + digits
	return digits[:point].ljust(point, "0"), digits[point:]


def remaining_length(a, b):
	chunks = [b]
	next_chunk = b + b
	while next_chunk <= a:
		chunks.append(next_chunk)
		next_chunk = next_chunk + next_chunk
	remaining = a
	for chunk in reversed(chunks):
		if chunk <= remaining:
			remaining -= chunk
	return remaining


def unused_length():
	first, second = numbers("Длины A B (A > B > 0): ", decimal_parts, 2)
	places = max(len(first[1]), len(second[1]))
	a = int(first[0] + first[1].ljust(places, "0"))
	b = int(second[0] + second[1].ljust(places, "0"))
	if not a > b > 0:
		raise ValueError("Нужно A > B > 0.")
	remaining = remaining_length(a, b)
	if places:
		digits = str(remaining).zfill(places + 1)
		print(digits[:-places] + "." + digits[-places:])
	else:
		print(remaining)


def sum_threshold():
	n = integer("N > 1: ", 2)
	k = total = 0
	while total < n:
		k += 1
		total += k
	print("K =", k, "Сумма =", total)


def deposit():
	percent, = numbers("Процент за месяц (0 < P < 25): ", count=1)
	if not 0 < percent < 25:
		raise ValueError("Нужно 0 < P < 25.")
	balance = 1000.0
	months = 0
	while balance <= 1100:
		next_balance = balance + balance * percent / 100
		if next_balance == balance:
			raise ValueError("Процент слишком мал для выбранной точности.")
		balance = next_balance
		months += 1
	print("Месяцев:", months, f"Сумма: {balance:.2f}")


def gcd():
	a, b = numbers("Положительные целые A B: ", int, 2)
	if a <= 0 or b <= 0:
		raise ValueError("Оба числа должны быть положительными.")
	while b:
		a, b = b, a % b
	print(a)


if __name__ == "__main__":
	menu([
		("Цена конфет по весу", candy), ("Произведение N сомножителей", product),
		("Квадрат как сумма нечётных", square), ("Сумма степеней", power_sum),
		("Знакопеременная сумма", alternating_sum), ("Повтор чисел", repeated_numbers),
		("Незанятая длина", unused_length), ("Минимальная сумма не меньше N", sum_threshold),
		("Банковский вклад", deposit), ("НОД по Евклиду", gcd),
	])
