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


def read_matrix(rows, columns, convert=real):
	return [numbers(f"Строка {i + 1} ({columns} чисел): ", convert, columns)
			for i in range(rows)]


def rectangular(convert=real):
	rows, columns = numbers("Количество строк M и столбцов N: ", int, 2)
	if rows < 1 or columns < 1:
		raise ValueError("Размеры должны быть положительными.")
	return read_matrix(rows, columns, convert)


def print_matrix(matrix):
	for row in matrix:
		print(*row)


def product(values):
	result = 1
	for value in values:
		result *= value
	return result


def spiral():
	size = integer("Нечётный порядок M: ", 1)
	if size % 2 == 0:
		raise ValueError("M должно быть нечётным.")
	matrix = read_matrix(size, size)
	values = []
	for layer in range(size // 2):
		end = size - 1 - layer
		for row in range(layer, end):
			values.append(matrix[row][layer])
		for col in range(layer, end):
			values.append(matrix[end][col])
		for row in range(end, layer, -1):
			values.append(matrix[row][end])
		for col in range(end, layer, -1):
			values.append(matrix[layer][col])
	center = size // 2
	values.append(matrix[center][center])
	print(*values)


def row_sum_and_product():
	matrix = rectangular()
	k = integer("Номер строки K: ", 1, len(matrix))
	row = matrix[k - 1]
	print("Сумма:", sum(row), "Произведение:", product(row))


def minimum_column_product():
	matrix = rectangular()
	products = [product(column) for column in zip(*matrix)]
	smallest = min(products)
	print("Столбец:", products.index(smallest) + 1, "Произведение:", smallest)


def above_column_mean():
	matrix = rectangular()
	counts = []
	for column in zip(*matrix):
		mean = sum(column) / len(column)
		counts.append(sum(value > mean for value in column))
	print(*counts)


def first_odd_column():
	matrix = rectangular(int)
	for index, column in enumerate(zip(*matrix), 1):
		if all(value % 2 != 0 for value in column):
			print(index)
			return
	print(0)


def swap_row_extremes():
	matrix = rectangular()
	for row in matrix:
		low, high = row.index(min(row)), row.index(max(row))
		row[low], row[high] = row[high], row[low]
	print_matrix(matrix)


def swap_extreme_columns():
	matrix = rectangular()
	smallest = largest = matrix[0][0]
	low = high = 0
	for row in matrix:
		for column, value in enumerate(row):
			if value < smallest:
				smallest, low = value, column
			if value > largest:
				largest, high = value, column
	for row in matrix:
		row[low], row[high] = row[high], row[low]
	print_matrix(matrix)


def swap_quarters():
	rows, columns = numbers("Чётные размеры M N: ", int, 2)
	if rows < 2 or columns < 2 or rows % 2 or columns % 2:
		raise ValueError("Размеры должны быть положительными и чётными.")
	matrix = read_matrix(rows, columns)
	half_rows, half_columns = rows // 2, columns // 2
	for row in range(half_rows):
		for col in range(half_columns):
			opposite = matrix[row + half_rows]
			matrix[row][col], opposite[col + half_columns] = opposite[col + half_columns], matrix[row][col]
	print_matrix(matrix)


def merge_rows(left_rows, right_rows):
	result = []
	left = 0
	right = 0
	while left < len(left_rows) and right < len(right_rows):
		if left_rows[left][0] <= right_rows[right][0]:
			result.append(left_rows[left])
			left += 1
		else:
			result.append(right_rows[right])
			right += 1
	result.extend(left_rows[left:])
	result.extend(right_rows[right:])
	return result


def sort_rows(rows):
	if len(rows) <= 1:
		return rows
	middle = len(rows) // 2
	left_rows = sort_rows(rows[:middle])
	right_rows = sort_rows(rows[middle:])
	return merge_rows(left_rows, right_rows)


def order_rows():
	matrix = rectangular()
	ordered = sort_rows(matrix)
	print_matrix(ordered)


def diagonal_sums():
	size = integer("Порядок матрицы M: ", 1)
	matrix = read_matrix(size, size)
	totals = []
	for offset in range(size - 1, -size, -1):
		start = max(0, -offset)
		end = min(size, size - offset)
		totals.append(sum(matrix[row][row + offset] for row in range(start, end)))
	print(*totals)


if __name__ == "__main__":
	menu([
		("Спираль против часовой стрелки", spiral), ("Сумма и произведение строки", row_sum_and_product),
		("Столбец с наименьшим произведением", minimum_column_product),
		("Элементы выше среднего столбца", above_column_mean), ("Первый нечётный столбец", first_odd_column),
		("Обмен минимума и максимума строки", swap_row_extremes),
		("Обмен столбцов с экстремумами", swap_extreme_columns), ("Обмен четвертей", swap_quarters),
		("Сортировка строк по первому элементу", order_rows), ("Суммы параллельных диагоналей", diagonal_sums),
	])
