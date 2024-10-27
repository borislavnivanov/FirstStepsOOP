from project.task import Task

class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str) -> str:
        for _task in self.tasks:
            if _task.name == task_name:
                _task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self) -> str:
        counter = 0
        for _task in self.tasks:
            if _task.completed:
                self.tasks.remove(_task)
                counter += 1
        return f'Cleared {counter} tasks.'

    def view_section(self) -> str:
        formated_str: list = [f'Section {self.name}:']
        for _task in self.tasks:
            formated_str.append(_task.details())

        return f'\n'.join(formated_str)


