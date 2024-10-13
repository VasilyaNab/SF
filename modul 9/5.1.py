class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task_name):
        return any(task['name'] == task_name for task in self.__task_list)

    def add_task(self, task_name):
        if not self.__is_task_in_list(task_name):
            task = {'name': task_name, 'done': False}
            self.__task_list.append(task)
            print(f'Задача "{task_name}" добавлена в список')
        else:
            print(f'Задача "{task_name}" уже есть в списке')

    def remove_task(self, task_name):
        if self.__is_task_in_list(task_name):
            self.__task_list = [task for task in self.__task_list if task['name'] != task_name]
            print(f'Задача "{task_name}" удалена из списка')
        else:
            print(f'Задачи "{task_name}" нет в списке')