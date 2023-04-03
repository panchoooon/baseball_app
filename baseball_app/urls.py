"""baseball_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prototype.views import frontpage, create_player, list_player, detail_player

urlpatterns = [
    path('admin/', admin.site.urls), #管理画面のパス
    path('index/', frontpage, name = 'index'), #選手作成画面(トップページ)
    path('create_player/', create_player, name='create_player'), #選手作成画面
    path('list_player/', list_player, name='list_player'), #選手一覧画面
    # path('detail_player/', detail_player, name='detail_player'), #選手詳細画面
    # path("<slug:slug>/", detail_player, name="detail_player") #選手詳細画面のスラグ
    path("<int:id>/", detail_player, name="detail_player") #選手詳細画面のスラグ
    
]
