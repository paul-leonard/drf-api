from django.urls import path
from .views import (
  SummaryList,
  SummaryDetail,
)

urlpatterns = [
  path('api/v1/', SummaryList.as_view(), name='summary_list_api'),
  path('api/v1/<int:pk>', SummaryDetail.as_view(), name='summary_detail_api'),
]