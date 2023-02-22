from django.urls import path
from . import views
from book_api.views import BookList, BookCreate, BookDetail

# urlpatterns = [
#     path('', views.book_create),
#     path('list/', views.books_list),
#     path('<int:pk>', views.book)
# ]

urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>/', BookDetail.as_view())
]
