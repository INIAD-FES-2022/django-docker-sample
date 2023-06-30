from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import Http404
from todo.models import Todo
from todo.forms import TodoForm


class Index(ListView, ModelFormMixin):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return Todo.objects.order_by('id')

def done(request):
    if request.method == 'POST':
        pk = int(request.POST.get('id'))
        todo = Todo.objects.get(pk=pk)
        todo.is_done = True if request.POST.get('is_done') == 'true' else False
        todo.save()

    return redirect('index')


