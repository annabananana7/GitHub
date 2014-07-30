from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render_to_response, redirect, render

from todo.models import Todo, Item
from todo.forms import TodoForm

class IndexView(generic.ListView):
    model = Todo
    template_name = 'todo/index.html'

class AboutView(generic.ListView):
    model = Todo
    template_name = 'todo/about.html'

class CreateView(generic.ListView):
    model = Todo
    template_name = 'todo/create.html'

def addItem(request):
    t = Todo()
    t.text = request.POST.get('todo_text', '')
    t.save()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        #Item.objects.create(text=request.POST['item_text'])
        #return redirect('/')

    else:
        return render(request, 'todo/create.html', {'form': form})
        #form = TodoForm()

    #items = Item.objects.all()
    #return render_to_response('todo/create.html', {'items': items})

class LoadView(generic.ListView):
    model = Todo
    template_name = 'todo/load.html'

    def get_queryset(self):
        return Todo.objects.all().order_by('-created')

class LinksView(generic.ListView):
    model = Todo
    template_name = 'todo/links.html'
