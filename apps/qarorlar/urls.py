from django.urls import path
from .views import (QarorlarView,
                    PQarorlar,
                    QarorQoshish,
                    QarorView,
                    QarorTahrirlash,
                    VQarorlar,
                    VQarorQoshish,
                    VQarorView,
                    VQarorTahrirlash
)

app_name = "qarorlar"

urlpatterns = [
    path("qarorlar/", QarorlarView.as_view(), name="qarorlar_bosh"),
    path("prezident-qarorlari/", PQarorlar.as_view(), name="prezident_qarorlari"),
    path("add_qaror/", QarorQoshish.as_view(), name="qaror_add"),
    path('tahrirlash/<int:pk>/', QarorTahrirlash.as_view(), name='qaror_edit'),
    path('ochirish/<int:pk>/', QarorView.as_view(), name='qaror_delete'),



    #vazirlik qarorlari uchun url lar shu yerda joylashadi

    path("vazirlik-qarorlari/", VQarorlar.as_view(), name="vazirlik_qarorlari"),
    path("vadd_qaror/", VQarorQoshish.as_view(), name="vqaror_add"),
    path('tahrirlash_v/<int:pk>/', VQarorTahrirlash.as_view(), name='vqaror_edit'),
    path('ochirish_v/<int:pk>/', VQarorView.as_view(), name='vqaror_delete'),
]
