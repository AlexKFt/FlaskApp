{% extends "base.tpl" %}

{% block content %}
<h2>{{person.show()}}</h2>

<form action = '/add' method=POST>

<input type="hidden" name=obj_class value="2">

<input type=hidden name=id value={{person.id}}>
Имя:<input type=text name=name value={{person.name}}><br>
Возраст:<input type=text name=age value={{person.age}}>
Должность: <input type=text name=position value={{person.position}}>
<br><input type=submit value="Ok">
</form>

{% endblock %}