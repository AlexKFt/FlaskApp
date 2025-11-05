{% extends "base.tpl" %}

{% block content %}
<h2>{{person.show()}}</h2>

<form action = '/add' method=POST>

<input type="hidden" name=obj_class value="3">

<input type=hidden name=id value={{person.id}}>
Имя:<input type=text name=name value={{person.name}}><br>
Возраст:<input type=text name=age value={{person.age}}>
Отдел: <input type=text name=department value={{person.department}}>
<br><input type=submit value="Ok">
</form>

{% endblock %}