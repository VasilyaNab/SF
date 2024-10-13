from abc import abstractmethod
class Student:
    def __init__(self, fio, group):
        self.fio = fio  # ФИО студента (строка)
        self.group = group  # группа (строка)
        self.lect_marks = []  # оценки за лекции
        self.homework_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self.lect_marks.append(mark)

    def add_homework_marks(self, mark):
        self.homework_marks.append(mark)

    def __str__(self):
        return f"Студент {self.fio}: оценки на лекциях: {str(self.lect_marks)}; оценки за д/з: {str(self.homework_marks)}"

class Mentor():
    def __init__(self, fio, subject):
        self.fio = fio
        self.subject = subject

    @abstractmethod
    def set_mark(self, student, mark):
        raise NotImplementedError

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        # super().__init__(student, mark)
        student.add_lect_marks(mark)

    def __str__(self):
        return (f'Лектор {self.fio}: предмет {self.subject}')

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        # super().__init__(student, mark)
        student.add_homework_marks(mark)
    def __str__(self):
        return (f'Эксперт {self.fio}: предмет {self.subject}')