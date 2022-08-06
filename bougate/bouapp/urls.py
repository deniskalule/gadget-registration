from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path form registration
    path('badge', views.badge, name='badge'),
    path('register_item', views.register_item, name='register_item'),
    path('person', views.person, name='person'),
    # path for view data in database
    path('view_person', views.view_person, name='view_person'),
    path('view_items', views.view_items, name='view_items'),
    path('view_badge', views.view_badge, name='view_badge'),
    # Path for updating data in database
    path('update_person/<int:pk>/', views.update_person, name='update_person'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('update_badge/<int:pk>/', views.update_badge, name='update_badge'),
    path('update_badge_out/<int:pk>/', views.update_badge_out, name='update_badge_out'),
    # Path for Deleting data in database
    path('delete_badge/<int:pk>/', views.delete_badge, name='delete_badge'),
    path('delete_person/<int:pk>/', views.delete_person, name='delete_person'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    # Path for Searching data in database
    path('search_person', views.person_search_bar, name='search_person'),
    path('search_item', views.item_search_bar, name='search_item'),
    path('search_badge', views.badge_search_bar, name='search_badge'),

]
