from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Theory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    text = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self',null=True,blank=True)

    @staticmethod
    def get_top_list():
        return Theory.objects.filter(parent__isnull = True)

    def __str__(self):
        return self.name

    def has_parent(self):
        return self.parent != None

    def is_top(self):
        return not self.has_parent()

    def get_children(self):
        children = Theory.objects.filter(parent=self)
        return children

    def is_leaf(self):
        children = self.get_children()
        if children:
            return False
        else:
            return True

    def is_middle(self):
        return not (self.is_top() or self.is_leaf())

    def get_url(self):
        return reverse('theory', kwargs={'pk': self.pk})
