from django.views.generic.base import ContextMixin
from theory.models import Theory

class TheoryMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(TheoryMixin, self).get_context_data(**kwargs)
        top_list = Theory.get_top_list()
        context['top_list'] = top_list
        return context