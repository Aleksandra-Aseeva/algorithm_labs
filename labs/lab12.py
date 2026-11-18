def run(action):
	try:
		action()
	except EOFError:
		print("Ввод завершён.")
	except (ValueError, ArithmeticError, RecursionError) as error:
		print(f"Ошибка: {error}")


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue:
	def __init__(self):
		self.clear()

	def clear(self):
		self.first = None
		self.last = None
		self.size = 0

	def add(self, value):
		node = Node(value)
		if self.last is None:
			self.first = node
		else:
			self.last.next = node
		self.last = node
		self.size += 1

	def take(self):
		node = self.first
		self.first = node.next
		if self.first is None:
			self.last = None
		self.size -= 1
		return node.value

	def values(self):
		node = self.first
		while node is not None:
			yield node.value
			node = node.next


def main():
	queue = Queue()
	print("1 — добавить, 2 — извлечь, 3 — посмотреть первый, 4 — размер и пустота")
	print("5 — показать очередь, 6 — проверить наличие, 7 — очистить, 0 — выход")
	while True:
		action = input("Команда: ").strip()
		if action == "0":
			return
		if action == "1":
			value = input("Элемент: ").strip()
			if value:
				queue.add(value)
				print("Добавлено:", value)
			else:
				print("Введите непустой элемент.")
		elif action == "2":
			if queue.size == 0:
				print("Очередь пуста.")
			else:
				value = queue.take()
				print("Извлечено:", value)
		elif action == "3":
			if queue.size == 0:
				print("Очередь пуста.")
			else:
				print("Первый элемент:", queue.first.value)
		elif action == "4":
			print("Размер:", queue.size, "Пуста:", "нет" if queue.size else "да")
		elif action == "5":
			print("Очередь:", " → ".join(queue.values()) if queue.size else "пуста")
		elif action == "6":
			value = input("Элемент: ").strip()
			print("Есть в очереди." if value in queue.values() else "В очереди нет.")
		elif action == "7":
			queue.clear()
			print("Очередь очищена.")
		else:
			print("Введите команду от 0 до 7.")


if __name__ == "__main__":
	run(main)
