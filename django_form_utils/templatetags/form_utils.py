"""
templatetags for django_form_utils

Time-stamp: <2008-10-14 14:57:12 carljm form_utils.py>

"""
from django import template

from django_form_utils.forms import BetterForm, BetterModelForm
from cjmango.utils import get_template_from_string

register = template.Library()

@register.filter
def render(form, template_name=None):
    """
    Renders a ``django.forms.Form`` or
    ``django_form_utils.forms.BetterForm`` instance using a template.

    The template name(s) may be passed in as the argument to the
    filter (use commas to separate multiple template names for
    template selection).

    If not provided, the default template name is
    ``form_utils/form.html``.

    If the form object to be rendered is an instance of
    ``django_form_utils.forms.BetterForm`` or
    ``django_form_utils.forms.BetterModelForm``, the template
    ``form_utils/better_form.html`` will be used instead if present.
    
    """
    default = 'form_utils/form.html'
    if isinstance(form, (BetterForm, BetterModelForm)):
        default = ','.join(['form_utils/better_form.html', default])
    tpl = get_template_from_string(template_name or default)

    return tpl.render(template.Context({'form': form}))

        

    