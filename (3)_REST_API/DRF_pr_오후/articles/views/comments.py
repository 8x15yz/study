from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from articles.models import Comment
from articles.serializers import CommentCreateSerializer


@api_view(['PUT', 'DELETE'])
def update_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'PUT':
        serializer = CommentCreateSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': f'{pk}번 댓글이 삭제 되었습니다.'}, HTTP_204_NO_CONTENT)
    
