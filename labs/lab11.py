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


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def insert(root, value):
	node = Node(value)
	if root is None:
		return node
	current = root
	while True:
		if value < current.value:
			if current.left is None:
				current.left = node
				break
			current = current.left
		else:
			if current.right is None:
				current.right = node
				break
			current = current.right
	return root


def search(root, target):
	while root is not None and root.value != target:
		if target < root.value:
			root = root.left
		else:
			root = root.right
	return root


def inorder(root, result):
	stack = []
	current = root
	while current is not None or stack:
		while current is not None:
			stack.append(current)
			current = current.left
		current = stack.pop()
		result.append(current.value)
		current = current.right


def main():
	values = numbers("Целые числа для построения дерева: ")
	root = None
	for value in values:
		root = insert(root, value)
	result = []
	inorder(root, result)
	print("Симметричный обход:")
	print(*result)
	target = int(input("Число для поиска: "))
	print("Элемент найден." if search(root, target) is not None else "Элемент не найден.")


def repeat():
	while run(main):
		if input("Enter — повторить, 0 — выйти: ").strip() == "0":
			return


if __name__ == "__main__":
	run(repeat)
