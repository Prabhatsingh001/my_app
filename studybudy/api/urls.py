from UserAuth.views import signup,login,dashboard,Update_Profile
from django.urls import path


urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('dashboard/', dashboard),
    path('update_profile/',Update_Profile),
]