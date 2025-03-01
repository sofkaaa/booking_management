from django.urls import path
from .views import pcroom_list, computer_list, create_pcroom
urlpatterns = [
    path("pcroom/list/", pcroom_list, name="PCRoom-list" ),
    path("computer/list/<int:pcroom_id>", computer_list, name = "Computer-list"),
    path("pcroom/create/", create_pcroom, name = "create-pcroom")
]
