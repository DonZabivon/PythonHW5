from rest_framework.decorators import action
from rest_framework.response import Response

class CommentViewSet(viewsets.ModelViewSet): 
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            status = 'unliked'
        else:
            comment.likes.add(user)
            status = 'liked'
        return Response({'status': status})