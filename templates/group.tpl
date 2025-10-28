{% extends "base.tpl" %}

{% block content %}
    {% for student in students %}
{% include "item.tpl" ignore missing %}
    {% else %}
Group is empty
    {% endfor %}

{% include "add.tpl" ignore missing %}
{% endblock %}