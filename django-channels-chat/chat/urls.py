from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views
from django.contrib.auth import views as auth_views

# django.contrib.auth.views.LogoutView
urlpatterns = [

    path('admin/', admin.site.urls),
#    url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),

    path('', include('core.urls')),
    path('login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/login.html"), {'next_page': '/'}, name='logout', )

]

# urlpatterns = [
#    url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
# ]