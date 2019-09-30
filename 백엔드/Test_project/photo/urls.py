from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate, PhotoLike1, PhotoLike2, PhotoLike3, PhotoLike4, PhotoLike5
from django.conf.urls.static import static
from django.conf import settings

app_name = "photo"
urlpatterns = [
    path('create/',PhotoCreate.as_view(), name='create'),
    path('delete/<int:pk>/',PhotoDelete.as_view(), name='delete'),
    path('update/<int:pk>/',PhotoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/',PhotoDetail.as_view(), name='detail'),
    path('',PhotoList.as_view(), name='index'),
    path('like1/<int:photo_id>/',PhotoLike1.as_view(), name='like1'),
    path('like2/<int:photo_id>/',PhotoLike2.as_view(), name='like2'),
    path('like3/<int:photo_id>/',PhotoLike3.as_view(), name='like3'),
    path('like4/<int:photo_id>/',PhotoLike4.as_view(), name='like4'),
    path('like5/<int:photo_id>/',PhotoLike5.as_view(), name='like5'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)