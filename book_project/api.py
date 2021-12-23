from rest_framework import routers

router = routers.DefaultRouter()
zzrouter.register(r'books', migrations.BooksViewSet)
router.register(r'lib-users', migrations.LibuserViewSet)
router.register(r'rented-books', migrations.LibuserViewSet)
