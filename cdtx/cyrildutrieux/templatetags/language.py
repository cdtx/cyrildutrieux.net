from django import template

register = template.Library()

@register.filter(name='lang')
def lang(value, lang):
    if type(value) == dict and lang in value.keys():
        return value[lang]
    return value
