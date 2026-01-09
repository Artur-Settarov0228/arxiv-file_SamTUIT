from django.urls import path
from .views import TalabalarView, AddTalaba, DeleteTalaba, TalabaUpdateView

app_name = "talabalar"

urlpatterns = [
    path("talabalar/", TalabalarView.as_view(), name="talabalar"),
    path("talabalar_add/", AddTalaba.as_view(), name="talabalar_add"),
    path("talabalar_delete/<int:talaba_id>/", DeleteTalaba.as_view(), name="talaba_delete"),
    path("talabalar_update/<int:talaba_id>/", TalabaUpdateView.as_view(), name="talabalar_update"),
]
