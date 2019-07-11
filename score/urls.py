from django.urls import path
from . import views, VerificationCode

app_name = "score"

urlpatterns = [
    path('test/', views.test, name='test'),
    # path('verificationCode/get/', VerificationCode.verification_code, name='getVerificationCode'),

    ## path('refresh/6/', views.refresh6, name="refresh6"),
    ## path('refresh/1_5/', views.refresh1_5, name="refresh1_5"),
    ## path('refresh/score/', views.refresh_score, name='refresh_score'),
    ## path('refresh/password/', views.refresh_password, name='refresh_password'),
    path('login/', views.login_html, name='login_html'),
    # path('login/check/', views.login_check, name='login_check'),
    #
    # path('show/', views.show, name='show'),
    # path('get/rank/', views.get_rank, name='get_rank'),
]
