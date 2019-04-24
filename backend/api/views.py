from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from api.serializers import UserSerializer, GroupSerializer, PlayerSerializer, ItemSerializer,StatusSerializer, RoomSerializer, TestSerializer
from api.models import Player, Item, Status, Room
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response

# Note: the rest_framework class ModelViewSet automatically
#       provides `list`, `create`, `retrieve`,`update` and `destroy` actions.

#################################################
##  User
#################################################
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

#################################################
##  Group
#################################################
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#################################################
##  Player
#################################################
class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['delete'])
    def mass_player_destroy(self, request):
        """Delete the user's password."""
        players = Player.objects.all()
        players.delete()

#################################################
##  Item
#################################################
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#################################################
##  Room
#################################################
class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rooms to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#################################################
##  Status
#################################################
class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    @action(detail=False, methods=['delete'])
    def mass_status_destroy(self, request):
        """Delete the user's password."""
        status = Status.objects.all()
        status.delete()

#################################################
##  For Testing Purposes
#################################################

@csrf_exempt
def TestPoint(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True,context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    #{
	#"test":"test"
    #}
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)
