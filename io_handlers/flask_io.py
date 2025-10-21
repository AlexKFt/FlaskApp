from flask import render_template, redirect, url_for, request

class FlaskIO:
    def __init__(self, group):
        self.group = group

    def render_index(self):
        students = self.group.show_students()
        return render_template("index.html", students=students)

    def render_add_form(self):
        return render_template("add_student.html")

    def render_edit_form(self, student):
        return render_template("edit_student.html", student=student)