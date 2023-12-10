from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import EntryForm
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


def newEntry (request):
    # If we are saving a new entry, add it to the database
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            # save to the database
            entry = form.save()
            return redirect('view_entry', entry_id=entry.pk)
        else:
            print(form.errors)
            return redirect('diary')
    else:
        # Otherwise show the form
        # Get default values
        return render(request, 'editpage.html', {'form': EntryForm()})


def editEntry (request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            # save to the database
            form.save()
        else:
            print(form.errors)
        return redirect('view_entry', entry_id=entry_id)
    else:
        # Otherwise show the form
        # Get default values
        return render(request, 'editpage.html', {'form': EntryForm(instance=entry)})


def viewEntry (request, entry_id):
    # Get the values of the entry and pass them in
    entry = Entry.objects.get(pk=entry_id)
    return render(request, 'displaypage.html', {'entry': entry})

