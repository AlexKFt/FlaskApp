{% extends "group/base.tpl" %}

{% include "group/load_from_pickle.tpl" ignore missing %}

{% block content %}
    {% for person in group %}
{% include "group/item.tpl" ignore missing %}
    {% else %}
Group is empty
    {% endfor %}

{% include "group/add_student.tpl" ignore missing %}
{% include "group/add_leader.tpl" ignore missing %}

{% endblock %}