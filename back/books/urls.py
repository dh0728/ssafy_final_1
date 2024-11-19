from django.urls import path
from . import views

urlpatterns = [
    path('calendar/',views.get_calendar), #켈린더 페이지
    path('budget/',views.budget),
    path('write/',views.write_account_data), # 지출 내역 추가, 수정 삭제
    path('receipt',views.receipt), # 영수증 OCR
    path('myhisory/',views.get_history), # 내역 페이지

]

