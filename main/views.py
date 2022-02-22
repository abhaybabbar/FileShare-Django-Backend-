from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FileShare, File
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
        
class UploadFiles(APIView):
    def post(self, request, format=None, **kwargs):
        try:
            files = request.FILES.getlist('files')
            if not files:
                return Response('No File Added', status=403)
            message = request.POST.get('message')
            fileshare = FileShare.objects.create(message=message)
            for file in files:
                fileshare.files.add(File.objects.create(file=file).id)
            return Response({'message': 'ok', 'slug': fileshare.slug}, status=200)
        except Exception as e:
            print(e)
            return Response('Something went wrong', status=403)