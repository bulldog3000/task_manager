class Task:
    def init(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.done = False

    def mark_as_done(self):
        self.done = True

    def str(self):
        status = "Завершено" if self.done else "Не завершено"
        return f"Задача: {self.title}\nОписание: {self.description}\nПриоритет: {self.priority}\nСтатус: {status}"

class TaskList:
    def init(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"Задача {index}:\n{task}\n")

    def mark_task_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_as_done()
            print(f"Задача '{task.title}' помечена как завершенная.")
        else:
            print("Некорректный индекс задачи.")

def main():
    task_list = TaskList()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как завершенную")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет задачи: ")
            task = Task(title, description, priority)
            task_list.add_task(task)
            print(f"Задача '{title}' добавлена.")

        elif choice == "2":
            task_list.display_tasks()

        elif choice == "3":
            task_index = int(input("Введите номер задачи, которую хотите отметить как завершенную: "))
            task_list.mark_task_as_done(task_index)

        elif choice == "4":
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()
