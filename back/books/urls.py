from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_calendar),
    path('budget/',views.budget), # 예산 GET, POST, PUT

    path('schedule/',views.schedule), #금융일정 GET, POST, PUT, DELETE


    path('day/',views.day), # 하루 내역 데이터 조회
    path('month/', views.month), # 한달치 결제 데이터 조히

    path('write/list/',views.write_account_data_list), # 여러 개 지출들 내역 POST, DELETE
    path('write/',views.write_account_data), # 한 개 지출들 POST, PUT, DELETE (post만들었는데 안씀)
    
    path('receipt/',views.receipt), # 영수증 OCR

    path('calender_data/',views.calender_data),

]


