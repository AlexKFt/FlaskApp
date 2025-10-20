from flask import request

class WebIO:
    """
    Стратегия ввода/вывода для работы через Flask.
    Ожидает, что Flask будет передавать поля формы через request.form.
    """
    def read(self, field_name: str):
        return request.form.get(field_name, "")

    def write(self, title: str, value: str):
        return f"{title}: {value}"

    def info(self, message: str):
        return f"{message}"