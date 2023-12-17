# Create your views here.
from rest_framework import generics,status,viewsets
from .serializers import BoxSerializer
from .models import Box
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .filters import BoxFilter, BoxUsernameDateFilter
from box.permissions import IsAuthenticatedAndIsStaff
from django_filters.rest_framework import DjangoFilterBackend

class ListAllViews(generics.ListAPIView):
  permission_classes=[IsAuthenticated]
  filter_backends=[DjangoFilterBackend]
  filterset_class=BoxUsernameDateFilter
  serializer_class=BoxSerializer
  queryset=Box.objects.all()

  def get_serializer_context(self):

    context = super(ListAllViews, self).get_serializer_context()
    context.update({"user_is_staff": self.request.user.is_staff})
    return context

class BoxCreateView(generics.CreateAPIView):
  permission_classes=[IsAuthenticated]
  serializer_class=BoxSerializer
  def post(request,self):
    serializer=BoxSerializer(data=request.data,context={"request":request})
    serializer.is_valid(raise_exception=True)
    serializer.save(creator=request.user)
    response={
      "Success":"True",
      "message":"Box created successfully",
    }    
    return Response(response,status=status.HTTP_201_CREATED)

class BoxUpdateView(generics.UpdateAPIView):
  permission_classes=[IsAuthenticated]
  serializer_class=BoxSerializer
  queryset=Box.objects.all()
  def patch(self,request,pk=None):
    box=Box.objets.get(pk=pk)
    serializer=BoxSerializer(box,data=request.data,context={"request":request},partial=True)  
    if serializer.is_valid():
      serializer.save()
      response={
        "success":"True",
        "message":"Box updated successfully",
      }
      return Response(response,status=status.HTTP_200_OK)
    else:
      response={
        "success":"False",
        "message":"Updation unscuccess"
      }  
      return Response(response,status=status.HTTP_400_BAD_REQUEST)

class ListMyBoxView(generics.ListAPIView):
  permission_classes=[IsAuthenticated]
  filter_backends=[DjangoFilterBackend]
  filterset_class=BoxFilter
  serializer_class=BoxSerializer
  def get_queryset(self):
    box_instance=Box.objects.filter(creator=self.request.user)
    return box_instance
    
class DestroyBoxView(generics.DestroyAPIView):
  permission_classes=[IsAuthenticated]
  def delete(self, request, pk=None):
        try:
            # Get the box instance by id and creator
            instance = Boxes.objects.get(id=pk, creator=request.user)
            instance.delete()
            response = {
                "success": "True",
                "message": "Box deleted successfully",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                "success": "False",
                "message": "Box cannot be deleted or unavailable",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)    
   
