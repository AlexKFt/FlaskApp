{% extends "base.tpl" %}

{% block content %}
<h2>{{student.Show()}}</h2>

<form action = '/add' method=POST>

<input type="hidden" name=obj_class value="Student">

<input type=hidden name=id value={{student.id}}>
Имя:<input type=text name=name value={{student.name}}><br>
Возраст:<input type=text name=age value={{student.age}}>
<br><input type=submit value="Ok">
</form>

{% endblock %}