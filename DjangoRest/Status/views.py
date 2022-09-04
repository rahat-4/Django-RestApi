# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, parsers


from .models import Status
from .serializers import StatusSerializer

# Create your views here.
# class StatusApiView(APIView):

#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)

#         return Response(status_serializer.data)
    
# class StatusGetPostApiView(mixins.CreateModelMixin,generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusGetPostApiView(generics.ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusCreateApiView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusUpdateRetrieveDeleteApiView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StatusUpdateRetrieveDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# class StatusDetailApiView(generics.RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# class StatusUpdateApiView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

class StatusViewSets(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]