from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("submit/",views.SubmitConfession.as_view(),name="submit-confession"),
    path("confession/<int:pk>/",views.ConfessionDetail.as_view(),name="confession-detail")
]
