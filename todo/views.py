from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.


class TodoList(ListView):
    model = TodoModel
    template_name = 'list.html'


class TodoDetail(DetailView):
    model = TodoModel
    template_name = "detail.html"


class TodoCreate(CreateView):
    model = TodoModel
    template_name = "create.html"
    # fieldsではmodels.py内で定義されているもの、かつ作成したい項目を選ぶこと
    fields = ('title', 'memo', 'priority', 'duedate')
    # 作成が成功したときにリダイレクトされるURLを記載する
    # reverse_lazyの中には、urls.pyのurlpatternsに入っているnameで紐付けをする
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    model = TodoModel
    template_name = "delete.html"
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    model = TodoModel
    template_name = "update.html"
    # updateしたい項目をfieldsに入れる。全部入れる必要は無い。
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
