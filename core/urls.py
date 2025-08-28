from django.urls import path

from core.views import Home, Ben

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<int:ben>/', Ben.as_view(), name='ben'),
    # path('<int:pk>/', FinduserDetailView.as_view(), name='detail'),
    # path('username/<int:pk>/', UsernameDetailView.as_view(), name='username-detail'),
    # path('computername/<int:pk>/', ComputernameDetailView.as_view(), name='computername-detail'),
    # path('interfacae/<int:pk>/', InterfaceDetailView.as_view(), name='interface-detail'),
    # path('new/', AutoTicketCreateView.as_view(), name='ostac-create'),
    # path('<int:pk>/update/', AutoTicketUpdateView.as_view(), name='ostac-update'),
    # path('<int:pk>/delete/', AutoTicketDeleteView.as_view(), name='ostac-delete'),
]