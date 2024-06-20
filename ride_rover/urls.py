from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Car_list.as_view(), name="home"),
    path("profile/", include("user_profile.urls")),
    path("user_credential/", include("user_credintial.urls")),
    path("add_car/", include("add_car.urls")),
    path("brands/", include("brands.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)