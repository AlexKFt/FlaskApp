{% extends "base.tpl" %}

{% include "load_from_pickle.tpl" ignore missing %}

{% block content %}
    {% for person in group %}
{% include "item.tpl" ignore missing %}
    {% else %}
Group is empty
    {% endfor %}

{% include "add_student.tpl" ignore missing %}
{% include "add_leader.tpl" ignore missing %}

{% endblock %}