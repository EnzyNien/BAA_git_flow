from django import template
from mainapp.models import Author
from mainapp.models import MODEL_DICT

register = template.Library()

@register.simple_tag(name='get_fields_from_row')
def get_fields_from_row(row, model_name):
    field_names = MODEL_DICT[model_name].get_field_names_gen()
    return [getattr(row,item) for item in field_names]
