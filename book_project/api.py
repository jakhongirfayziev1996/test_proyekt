from rest_framework import routers
from book_project import views

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet, basename='books')
router.register(r'lib-users', views.LibuserViewSet)
router.register(r'rented-books', views.LibuserViewSet)



for url in router.urls:
    print(url, '/n')