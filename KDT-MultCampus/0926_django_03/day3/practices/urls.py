from django.urls import path
from . import views

app_name = "practices"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("ping/", views.ping, name="ping"),
    path("pong/", views.pong, name="pong"),
    path("is-odd-even/<int:number>/", views.is_odd_even),
    path("calculate/<int:num1>/<int:num2>/", views.calculate),
    path("pre-life/", views.pre_life),
    path("pre-life-result/", views.pre_life_result),
    path("lipsum-kor/", views.lipsum_kor),
    path("lipsum-kor-result/", views.lipsum_kor_result),
]
