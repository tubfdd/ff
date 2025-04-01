from asyncio import current_task

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        if not self.tail:
            return None
        data = self.tail.data
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def pop_start(self):
        if not self.head:
            return None
        data = self.head.data
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.tail.data

class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def do(self):
        if self.subtasks:
            print(f"Виконую завдання: {self.name}. Розбиваю на підзавдання")
        else:
            print(f"Завершено завдання: {self.name}")
        return self.subtasks

class Project:
    def __init__(self, tasks):
        self.tasks = DoubleLinkedList()
        self.tasks.push_end(tasks)

    def do_task(self):
        if self.tasks.is_empty():
            print("Немає завдань.")
            return
        current_task = self.tasks.pop_end()
        new_task = current_task.do()
        for t in new_task:
            self.tasks.push_end(t)

    def is_finished(self):
        if self.tasks.is_empty():
            print("Немає невиконаних завдань.")
        return self.tasks.is_empty()

task = Task('Підготовка до зйомок')
task.subtasks = [
    Task('Пошук локацій'),
    Task('Підготовка сценарію'),
    Task('Кастинг акторів')
]
task.subtasks[0].subtasks = [
    Task('Огляд локацій у місті'),
    Task('Огляд локацій за містом'),
    Task('Узгодження місць для зйомок')
]
task.subtasks[1].subtasks = [
    Task('Написання основного сценарію'),
    Task('Редагування сценарію'),
    Task('Підготовка сценарних приміток')
]
task.subtasks[2].subtasks = [
    Task('Пошук головних акторів'),
    Task('Пошук другорядних акторів'),
    Task('Підготовка контрактів для акторів')
]
task.subtasks[0].subtasks[0].subtasks = [
    Task('Вибір декорацій для зйомок'),
    Task('Узгодження з власниками приміщень')
]
task.subtasks[0].subtasks[1].subtasks = [
    Task('Вибір лісу для сцени битви'),
    Task('Пошук старовинних будівель для сцени')
]
task.subtasks[1].subtasks[0].subtasks = [
    Task('Написання першої частини'),
    Task('Написання другої частини')
]
task.subtasks[2].subtasks[0].subtasks = [
    Task('Пошук актора на роль головного героя'),
    Task('Пошук актриси на роль головної героїні')
]

project = Project(task)
while not project.is_finished():
    project.do_task()
