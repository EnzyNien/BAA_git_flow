from django.conf.urls import url, include
from mainapp import views

app_name = 'mainapp'


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^books/$', views.BooksList.as_view(), name='book_list'),
    url(r'^tags/$', views.TagsList.as_view(), name='tags_list'),
    url(r'^authors/$', views.AuthorsList.as_view(), name='authors_list'),
]

