from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    # detailの、どこの詳細を確認するかわからないので<int:pk>を入れている
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    # delete、どこの詳細を確認するかわからないので<int:pk>を入れている
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    # updateの、どこの詳細を確認するかわからないので<int:pk>を入れている
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
