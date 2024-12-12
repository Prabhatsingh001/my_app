from UserAuth.views import signup,login,dashboard,Update_Profile,delete_profile
from django.urls import path


urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('dashboard/', dashboard),
    path('update_profile/',Update_Profile),
    path('delete_profile/', delete_profile),
]