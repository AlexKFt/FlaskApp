{% extends "base.tpl" %}

{% block content %}
    {% for it in items %}
{% include "item.tpl" ignore missing %}
    {% else %}
Group is empty
    {% endfor %}

{% include "add.tpl" ignore missing %}
{% endblock %}