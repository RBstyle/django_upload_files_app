from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from files.models import UploadFile
from api.serializers import UploadFileSerializer
from files.tasks import file_processing


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
        file_type = request.data.get("file").content_type

        if serializer.is_valid():
            serializer.save()
            file_id = serializer.data.get("id")
            file_processing.delay(file_id, file_type.split("/")[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
