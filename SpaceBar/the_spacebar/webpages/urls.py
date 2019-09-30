from django.urls import path
from . import views


urlpatterns = [
    path('apis/', views.apis, name='apis'),
    path('pictures/', views.pictures, name='pictures'),
    path('wiki/', views.wiki, name='wiki'),
    path('data-science/', views.wiki, name='data-science'),

     # 'apis/', 'pictures/', 'wiki/' is the name of the Url pattern when apis page is loaded 2. view.apis renders the HTML page. 3. the "name" is used to pass through the view.
]