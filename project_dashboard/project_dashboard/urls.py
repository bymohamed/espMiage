
from django.contrib import admin
from django.urls import path, include
import main.views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', mainViews.dashboard, name="dashboard"),
    path('login/', mainViews.viewlogin, name="login"),
    path('tables/', mainViews.tables, name="tables"),
    path('charts/', mainViews.charts, name="charts"),
    path('charts/<int:id>', mainViews.charts, name="charts"),


]
