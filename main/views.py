from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FileShare
from .serializers import FileShareSerializer

# Create your views here.
class GetFiles(APIView):
    def get(self, request, format=None, **kwargs):
        try:
            slug = kwargs['slug']
            files = FileShare.objects.filter(slug = slug)
            if not files.exists():
                return Response('No Such URL Exisits', status=404)
            serializer = FileShareSerializer(files.first())
            return Response(serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response('Something went wrong', status=400)
        