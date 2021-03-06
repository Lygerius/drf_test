from django.shortcuts import redirect
from rest_framework import status
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Images
from .serializers import ImageSerializer


class ImageViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "image_list.html"
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get(self, request):
        queryset = Images.objects.all().order_by("-pub_date")
        serializer = ImageSerializer()
        return Response({"images": queryset, "serializer": serializer})

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = request.data["images"]
            serializer.save(image=image)
            return redirect("image_list")
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
