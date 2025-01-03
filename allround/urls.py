from django.contrib import admin
from django.urls import path
from wisata import views as wisataView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wisataView.home,name='home'),
    path('about/',wisataView.about,name='about'),
    path('detail/<int:wisata_id>', wisataView.detail,name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)