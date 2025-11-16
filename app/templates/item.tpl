<p>
{{person.io_handler.get_output()}}
</p>
{% set cls_id = 1 %}
{%if person is instanceof('Leader')%}
    {% set cls_id = 2 %}
{% endif %}
<a href="/edit_form/{{cls_id}}/{{person.id}}">Edit</a>
<a href="/delete/{{person.id}}">Delete</a>
<br><br>