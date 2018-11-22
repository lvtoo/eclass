from django.views.generic import ListView
from home.models import New


class Index(ListView):
    model = New
    template_name = 'home/index.html'
    paginate_by = 10
    context_object_name = 'news'
    ordering = 'pub_date'
