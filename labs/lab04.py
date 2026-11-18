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


def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n - 1)


def fibonacci_pair(n):
	if n == 0:
		return 0, 1
	current, following = fibonacci_pair(n // 2)
	even = current * (2 * following - current)
	odd = current ** 2 + following ** 2
	if n % 2 == 0:
		return even, odd
	return odd, even + odd


def fibonacci(n):
	return fibonacci_pair(n)[0]


def power(x, n):
	if n == 0:
		return 1
	if n < 0:
		return 1 / power(x, -n)
	half = power(x, n // 2)
	return half * half * x if n % 2 else half * half


def palindrome(text, left, right):
	if left >= right:
		return True
	return text[left] == text[right] and palindrome(text, left + 1, right - 1)


def binary_search(values, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	if values[middle] == target:
		return middle
	if target < values[middle]:
		return binary_search(values, target, left, middle - 1)
	return binary_search(values, target, middle + 1, right)


def reverse_words(words, index, result):
	if index < 0:
		return
	result.append(words[index])
	reverse_words(words, index - 1, result)


def prime_parts(n):
	if n < 4:
		return [n]
	if n % 2 == 0:
		half = prime_parts(n // 2)
		return half + half
	return [3] + prime_parts(n - 3)


def digit_count(n):
	if n < 10:
		return 1
	return 1 + digit_count(n // 10)


def hanoi(n, source, target, spare):
	if n == 0:
		return
	hanoi(n - 1, source, spare, target)
	print(f"Диск {n}: {source} → {target}")
	hanoi(n - 1, spare, target, source)


def read_power():
	x, = numbers("Основание x: ", count=1)
	print(power(x, integer("Целый показатель n: ")))


def read_palindrome():
	text = input("Строка: ")
	print("Да" if palindrome(text, 0, len(text) - 1) else "Нет")


def read_search():
	values = numbers("Отсортированные целые числа: ", int)
	if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
		raise ValueError("Массив должен быть отсортирован по неубыванию.")
	target = integer("Искомое число: ")
	print("Индекс:", binary_search(values, target, 0, len(values) - 1))


def read_words():
	words = input("Строка: ").split()
	result = []
	reverse_words(words, len(words) - 1, result)
	print(*result)


def read_factorial():
	n = integer("n ≥ 0: ", 0)
	print(factorial(n))


def read_fibonacci():
	n = integer("n ≥ 0: ", 0)
	print(fibonacci(n))


def read_prime_parts():
	n = integer("n ≥ 2: ", 2)
	parts = prime_parts(n)
	text_parts = [str(part) for part in parts]
	print(" + ".join(text_parts))


def read_digit_count():
	n = integer("Целое число: ")
	print(digit_count(abs(n)))


def read_hanoi():
	n = integer("Количество дисков (от 1): ", 1)
	hanoi(n, "A", "C", "B")


if __name__ == "__main__":
	menu([
		("Факториал", read_factorial),
		("Число Фибоначчи", read_fibonacci),
		("Возведение в степень", read_power),
		("Палиндром", read_palindrome),
		("Рекурсивный бинарный поиск", read_search),
		("Слова в обратном порядке", read_words),
		("Сумма простых чисел", read_prime_parts),
		("Количество цифр", read_digit_count),
		("Ханойская башня", read_hanoi),
	])
