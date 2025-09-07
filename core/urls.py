from django.urls import path

from core.views import Home, Ben

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ben/<int:id>/', Ben.as_view(), name='ben'),
    path('annex/<int:id/', Home.as_view(), name='annex'),
    path('serviceprovider/<int:id>/', Home.as_view(), name='service_provider'),
    path('form470/<int:id>/', Home.as_view(), name='form470basic'),
    # path('consultingfirm/<int:pk>/', Home.as_view(), name='consulting_firm'),
    # path('consultant/<int:pk>/', Home.as_view(), name='consultant'),
    # path('c2budget/<int:pk>/', Home.as_view(), name='c2budget'),
    # path('<int:pk>/', FinduserDetailView.as_view(), name='detail'),
    # path('username/<int:pk>/', UsernameDetailView.as_view(), name='username-detail'),
    # path('computername/<int:pk>/', ComputernameDetailView.as_view(), name='computername-detail'),
    # path('interfacae/<int:pk>/', InterfaceDetailView.as_view(), name='interface-detail'),
    # path('new/', AutoTicketCreateView.as_view(), name='ostac-create'),
    # path('<int:pk>/update/', AutoTicketUpdateView.as_view(), name='ostac-update'),
    # path('<int:pk>/delete/', AutoTicketDeleteView.as_view(), name='ostac-delete'),
]