from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from api.permissions import *
from api import models, serializers


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.Article
    permission_classes = (IsOwnerOrReadOnly,)


class ArticleList(ListCreateAPIView):
    queryset = models.Article.objects.all().order_by("-regDate")
    serializer_class = serializers.Article
    permission_classes = (IsAuthenticatedOrReadOnly,)


class Log(ListCreateAPIView):
    queryset = models.Log.objects.all().order_by("-regDate")
    serializer_class = serializers.Log
    permission_classes = (IsAuthenticatedOrAdminOnly,)