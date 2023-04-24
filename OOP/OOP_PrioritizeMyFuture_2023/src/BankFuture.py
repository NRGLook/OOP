from src.Bank import Bank
from src.ToDoList import ToDoList


class BankFuture(Bank):
    def __init__(self):
        super().__init__()
        self.task_for_ToDoList = ToDoList()
        self.list_of_DONE_tasks_Future_Bank = []

    def calculate_statistic_for_task(self):
        self.list_of_DONE_tasks_Future_Bank = self.task_for_ToDoList.show_done_task()
        count_of_not_done_tasks = len(self.list_of_DONE_tasks_Future_Bank)
        print(count_of_not_done_tasks)
