from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Board
from .serializers import BoardSerializer


@api_view(['GET'])
def boardList(request): #게시글 리스트
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True) #리스트이기때문에 한 건 이상 받기위해 true

    return Response(serializer.data)

@api_view(['GET'])
def boardView(request,pk): # 게시글 자세한 확인 #게시글 번호에 PK를 줘서 그 값으로 구별하기 위하여 PK의 유무가 있음
    boards = Board.objects.get(id=pk)
    serializer = BoardSerializer(boards, many=False) #한 건만 받기 위해 false

    return Response(serializer.data)

@api_view(['POST'])
def boardInsert(request): #게시글 작성
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        print('성공') #정상적으로 데이터가 들어갔는지 확인하기 위하여 작성
        serializer.save()
    else:
        print("실패")

    return Response(serializer.data)

@api_view(['PUT'])
def boardUpdate(request,pk): #게시글 수정
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance=board, data=request.data)

    if serializer.is_valid():
        print('성공')
        serializer.save()
    else:
        print("실패")

    return Response(serializer.data)

@api_view(['DELETE'])
def boardDelete(request,pk): #게시글 삭제
    board = Board.objects.get(id=pk)

    if board:
        board.delete()

    return Response("삭제 완료")