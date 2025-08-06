from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from blog.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
def example(request):
    return render(request, 
                  template_name='example\example.html',
                  )

#@api_view([])
#다섯가지 기능 - 전체리스트,상세보기,생성하기,수정하기,삭제하기
#GET-전체리스트,한개 상세정보 보기,
#POST-새로 생성하기,작성하기(form을 작성해서 제출하기 누른 경우),[제출버튼] --> url에 붙어서 보여진 채로 보내짐 http://naver,com/?name='홍길동'
#<form type='post'> [제출버튼] --> http request payload form을 숨겨서 보내짐 http://naver.com/
#PUT -> Post를 수정했다면, 전체 항목을 다시 보내줌,
#PATCH -> Post를 수정할때 title='수정한 타이틀' 일부 항목만 보내면 됨,
#DELETE -> 삭제할때 사용된다.

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

@api_view(['GET'])
def hiAPI(request):
    return Response("Hi world")

@api_view(['GET', 'DELETE', 'PUT'])
def postAPI(request, pk):
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post)
        return Response(postSerializer.data)
    elif request.method == "DELETE":
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post,data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_200_OK)
        
    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def blogAPI(request):
    if request.method == 'GET': # 글 전체 리스트 보여주기
        post = Post.objects.all()
        postSerializer = PostSerializer(post, many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)
    else:
        # 새로운 글 create 해준다.
        # 화면에서 작성 json -> django 서버로 전달됨
        # json -> post instance 로 변경  - deserialize
        postSerializer = PostSerializer(data = request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_201_CREATED)
    
    return Response(postSerializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def commentAPI(request, post_id):
    if request.method == 'GET':
        # 해당 게시글의 전체 댓글 조회
        comments = Comment.objects.filter(post_id=post_id)
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # 댓글 생성
        data = request.data.copy()
        data['post'] = post_id
        commentSerializer = CommentSerializer(data=data)
        if commentSerializer.is_valid():
            commentSerializer.save()
            return Response(commentSerializer.data, status=status.HTTP_201_CREATED)
        return Response(commentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # 댓글 수정 (댓글 id가 필요)
        comment_id = request.data.get('id')
        if not comment_id:
            return Response({'error': '댓글 ID (id)가 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.filter(pk=comment_id, post_id=post_id).first()
        if not comment:
            return Response({'error': '해당 댓글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        commentSerializer = CommentSerializer(comment, data=request.data, partial=True)
        if commentSerializer.is_valid():
            commentSerializer.save()
            return Response(commentSerializer.data, status=status.HTTP_200_OK)
        return Response(commentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # 특정 댓글 삭제 or 전체 삭제
        comment_id = request.data.get('id')
        if comment_id:
            comment = Comment.objects.filter(pk=comment_id, post_id=post_id).first()
            if not comment:
                return Response({'error': '해당 댓글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
            comment.delete()
            return Response({'message': '댓글 삭제 완료'}, status=status.HTTP_204_NO_CONTENT)
        else:
            Comment.objects.filter(post_id=post_id).delete()
            return Response({'message': '해당 게시글의 모든 댓글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)



def comment_html_page(request):
    return render(request, 'example/comment.html')  # HTML 보여주기

@api_view(['GET'])
def commentAPI_data(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)