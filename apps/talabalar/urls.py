from django.urls import path
from .views import Talabalar, AddTalaba

app_name = "talabalar"

urlpatterns = [
    path("talabalar/", Talabalar.as_view(), name="talabalar"),
    path("talabalar_add/", AddTalaba.as_view(), name="talabalar_add"),
]
