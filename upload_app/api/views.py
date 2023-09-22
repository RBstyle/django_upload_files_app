from rest_framework.decorators import api_view
from rest_framework.response import Response

from files.models import File
from api.serializers import FileSerializer


# @swagger_auto_schema(
#     methods=["post"],
#     request_body=NumberOfProductsSerializer,
#     operation_description="Введите количество продуктов(от 0 до 50)",
# )
# @swagger_auto_schema(
#     methods=["get"],
#     operation_description="Возвращает список всех товаров",
# )
@api_view(["GET"])
def get_files(request):
    if request.method == "GET":
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def upload_file(request):
    if request.method == "POST":
        return Response("POST")
