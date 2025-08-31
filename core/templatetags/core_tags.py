from django import template

register = template.Library()

@register.filter
def iends_with(value, arg):
    """
    Checks if a string ends with a specified substring.
    Usage: {{ my_string|iends_with:"_suffix" }}
    """
    return str(value).lower().endswith(str(arg.lower()))