from django.urls import path
from . import views
from . import recognation

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index', views.index, name='index'),
    path('first', views.first, name='first'),
    path('user_idfirst', views.user_idfirst, name='user_idfirst'),
    path('user_idsecond', views.user_idsecond, name='user_idsecond'),
    path('second', views.second, name='second'),
    path('add_sup', views.add_supervisor, name='add_supervisor'),
    path('detailofworker', views.detail, name='detail_of_workers'),
    path('applied', views.applied_job, name='applied'),
    path('add_sups', views.add_sups, name='add'),
    path('workers_add', views.add_worker, name='added'),
    path('bankdetail', views.bank_detail, name='bank_detail_worker'),
    path('hello2', views.hello2, name='hello2'),
    # path('hello', recognation.hello, name='hello'),
    path('verify', views.verify, name='verify'),
    path('verifing', views.verifing, name='verification'),
    path('status', views.app_status, name='application_status'),
    path('result', views.result),
    path('not_verify', views.not_verified, name='verify_table'),
    path('photo', recognation.photos, name='photo'),
    path('first_verify', recognation.account_verify, name='account_verify'),
    path('capture', recognation.capture, name='capture'),
    path('add_office', views.add_officer, name='office'),
    path('attend', views.Attendence, name='attendence'),
    path('mark', recognation.faceverify, name='face'),
    path('date_att', views.date_att, name='attendence_date'),
    path('date', views.table_att, name='date'),
    path('muster', views.muster, name='musteroll'),
    path('attby_app', views.attby_app, name='app_attendence'),
    path('att_search', views.att_search, name='attendece_search'),
    path('work', views.work, name='work'),
    path('bankby_app', views.bank_by_app, name='bank detail by attendence number'),
    path('pass_change', views.password2, name='password_change'),
    path('logout2', views.logout2, name='logout_2'),
    path('hello', views.hello, )
]
