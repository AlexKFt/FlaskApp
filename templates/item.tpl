Имя: {{person.name}}<br>
Возраст: {{person.age}}<br>
Id: {{person.id}}<br>
{%if person is instanceof('Worker')%}
    Должность: {{person.position}}
{% endif %}
{%if person is instanceof('Director')%}
    Отдел: {{person.department}}
{% endif %}
<a href="/edit/{{person.id}}">Edit</a>
<a href="/delete/{{person.id}}">Delete</a>
<br><br>