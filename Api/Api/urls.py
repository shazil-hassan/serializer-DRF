
from django.contrib import admin
from django.urls import path
from create_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studata/<int:pk>',views.student_data),
    path('studata/',views.student_list)
]
