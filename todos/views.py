from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ToDoList
from django.utils import timezone

class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = 'todos/list.html'
    context_object_name = 'todos'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = ToDoList.objects.filter(user=self.request.user, is_deleted=False)

        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(title__icontains=query)
            
        return queryset

class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDoList
    template_name = 'todos/create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todos:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDoList
    template_name = 'todos/update.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todos:list')

class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoList
    template_name = 'todos/delete.html'
    success_url = reverse_lazy('todos:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return super().delete(request, *args, **kwargs)

