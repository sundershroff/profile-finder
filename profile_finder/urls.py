from django.urls import path
from profile_finder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin),
    path('', views.mainpage),
    path('signup', views.signup),
    path('statelist/<int:pk>/',views.statelist),
    path('rstatelist/<int:pk>/',views.rstatelist),
    path('fstatelist/<int:pk>/',views.fstatelist),
    path('mstatelist/<int:pk>/',views.mstatelist),
    path('ccstatelist/<int:pk>/',views.ccstatelist),
    path('citylist/<int:pk>/',views.citylist),
    path('rcitylist/<int:pk>/',views.rcitylist),
    path('citylistp/<int:pk>/',views.citylistp),
    path('otp/<id>', views.opt_check),
    path('dashboard/<id>', views.profile_dashboard),
    path('profileidcard/<id>', views.profileidcard),
    path('profileforwhom/<id>', views.profileforwhom),
    path('profileform/<id>', views.profileform),
    #path('profilepicture', views.profilepicture),
    path('selfie_upload/<id>',views.selfie_upload),
    path('primary_details/<id>', views.primary_details),
    path('family_details/<id>',views.family_details),
    path('contact_details/<id>',views.contact_details),
    path('header/<id>',views.header),
    path('profile_page/<id>',views.profile_page),
    path('menu_header',views.menu_header),
    path('highlight_profile/<id>',views.highlight_profile),
    path('highlight_payment/<id>',views.highlight_payment),
    path('payment',views.payment),
    path('matching_list/<id>',views.matching_list),
    path('viewallmatch/<id>',views.viewallmatch),
    path('package_matching/<id>',views.package_matching),
    path('requested_list/<id>',views.requested_list),
    path('received/<id>',views.received),
    path('saved_Search/<id>',views.saved_search),
    path('request_received',views.follow_request1),
    path('sucess_story',views.happy_couples),
    path('hai',views.test2),
    #favorites
    path('myfavorites/<id>',views.myfavorites),
    #happy Couple
    path('happycouples/<id>', views.happycouple),
    path('success_story/<id>', views.success_Story),
    path('uploadyours/', views.uploadyours),
    path('package/<id>', views.package),
    path('package_amount/<id>', views.package_amount),
    path('happy_couples_upload/<id>', views.happy_couples_upload),

    # path('happycouples1/', views.happycouples1),
    path('happy_couples_test', views.happy_couples_test),
    path('Block', views.block),
    #settings
    path('settings_notification/<id>', views.settings_notification),
    path('settings_privacy/<id>', views.settings_privacy),
    path('settings_security/<id>', views.settings_security),
    path('settings_subscription/<id>', views.settings_subscription),
    path('settings_wallet/<id>', views.settings_wallet),
    path('settings_about/<id>', views.settings_about),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)