from flask import render_template, redirect, url_for, request

class FlaskIO:
    def __init__(self, group):
        self.group = group
        self.data = {}

    def read(self, field_name: str):
        return self.data.get(field_name, "")

    def write(self, field_name: str, value: str):
        self.data[field_name] = value

    def info(self, message: str):
        print(message)