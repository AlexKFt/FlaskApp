{% extends "base.tpl" %}

{% block content %}
    {% for person in group %}
{% include "item.tpl" ignore missing %}
    {% else %}
Group is empty
    {% endfor %}

{% include "add_person.tpl" ignore missing %}
{% include "add_worker.tpl" ignore missing %}
{% include "add_director.tpl" ignore missing %}
{% endblock %}