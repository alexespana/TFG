from django import template

register = template.Library()

# Register a tag to be used in templates to check if the user is in a group
# How to use it:
# {% if user | is_in_group: "group_name" %}
#   ...
# {% endif %}
@register.filter(name='is_in_group') 
def in_group(user, group_name):
    """
    Checks if a user is in a group
    """
    return user.groups.filter(name=group_name).exists()
