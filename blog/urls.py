from django.urls import path
from .views import   addLike, post_list, new_post, post_details, postDelete, postUpdate

urlpatterns = [
    path('', post_list, name='home'),
    path('create/', new_post, name='create'),
    path('details/<int:id>/', post_details, name='details'),
    path('like/<int:id>/', addLike, name='like'),
    path('update/<int:id>/', postUpdate, name='update'),
    path('delete/<int:id>/', postDelete, name='delete'),

]