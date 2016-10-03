from django import template

register = template.Library()

@register.filter(name='lang')
def lang(value, lang):
    if type(value) == dict:
        if lang in value.keys():
            return value[lang]
        else:
            return value.get('fr', 'Text not available')
    return value
