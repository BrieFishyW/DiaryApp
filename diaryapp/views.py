from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Entry


# Create your views here.
def listpage (request):
    entry_list = Entry.objects.all()
    entry_title = request.GET.get('entry_title')
    if entry_title != '' and entry_title is not None:
        entry_list = entry_list.filter(entry_title__icontains=entry_title)
    paginator = Paginator(entry_list, 10)
    page = request.GET.get('page')
    entry_list = paginator.get_page(page)
    return render(request, 'listpage.html', {'entry_list': entry_list})

