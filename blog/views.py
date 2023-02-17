from django.db.models.aggregates import Count
from rest_framework.viewsets import ModelViewSet
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        products_count=Count('posts')).all()
    serializer_class = CategorySerializer
