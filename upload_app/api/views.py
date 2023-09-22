from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from files.models import UploadFile
from api.serializers import UploadFileSerializer


@api_view(["GET"])
def get_files(request):
    if request.method == "GET":
        queryset = UploadFile.objects.all()
        serializer = UploadFileSerializer(queryset, many=True)
        return Response(serializer.data)


class AddFile(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
