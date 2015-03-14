from django import template
from django.template.loader import select_template


register = template.Library()


@register.simple_tag(takes_context=True)
def render_price(context, session):
    template_ = select_template(['catalogue/partials/price.html'])
    context['session'] = session
    return template_.render(context)
