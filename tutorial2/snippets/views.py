from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from .models import Snippet
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer,SnippetSerializer
from rest_framework import viewsets,permissions,renderers
from rest_framework.response import Response

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这个视图集自动提供 `list` 和 `detail` 操作。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class SnippetViewSet(viewsets.ModelViewSet):
    """
    这个视图集自动提供 `list`， `create`， `retrieve`， `update`和`destroy`操作。
    另外我们还提供了一个额外的 `highlight` 操作。
    """
    queryset = Snippet.objects.all().order_by('id')
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })