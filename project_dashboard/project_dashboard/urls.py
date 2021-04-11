
from django.contrib import admin
from django.urls import path, include
import main.views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', mainViews.dashboard, name="dashboard"),
    path('datarecup/', mainViews.datarecup, name="datarecup"),
    path('login/', mainViews.viewlogin, name="login"),
    path('tables/', mainViews.tables, name="tables"),

]
