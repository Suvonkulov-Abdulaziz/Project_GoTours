from django.urls import path
from .views import HomeView, BookView, StaffView, DeleteView
urlpatterns = [
    path('', HomeView, name='home'),
    path('book/', BookView, name="book"),
    path('staff/', StaffView, name="staff"),
    path('delete/<int:id>', DeleteView, name='delete')
]
