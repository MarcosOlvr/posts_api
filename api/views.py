from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import PostSerializer

# Create your views here.
url = "https://dev.codeleap.co.uk/careers/"

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/post-list/',
        'Detail View': '/post-detail/<int:pk>/',
        'Create': '/post-create/',
        'Update': '/post-update/<int:pk>/',
        'Delete': '/post-delete/<int:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    response = requests.get(url)
    posts = response.json()["results"]

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    response = requests.get(url)
    posts = response.json()["results"]

    for post in posts:
        if post["id"] == pk:
            serializer = PostSerializer(post, many=False)    

            if (serializer):
                return Response(serializer.data)
            
    return Response({"error": "post not found"}, status=404)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        response = requests.post(url, json=serializer.data)
        print(response.status_code)

        if (response.status_code == 200):
            return Response(serializer.data)
        
@api_view(['PATCH'])
def postUpdate(request, pk):
    response = requests.get(url)
    posts = response.json()["results"]

    for post in posts:
        if post["id"] == pk:
            post["title"] = request.data["title"]
            post["content"] = request.data["content"]

            serializer = PostSerializer(data=post)

            if serializer.is_valid():
                result = requests.patch(url + f"{pk}/", json=post)

                return Response(request.data)

    return Response({"error": "post not found"}, status=404)

@api_view(['DELETE'])
def postDelete(request, pk):
    requests.delete(url + f"{pk}/")
    
    return Response({})