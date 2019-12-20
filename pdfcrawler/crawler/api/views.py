import os
from crawler.models import Document, Url
from crawler.serializers import (
    DocumentSerializerMany,
    DocumentSerializer,
    UrlSerializerMany
)
from crawler.utils import extract_urls_from_pdf

from rest_framework import generics, views
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.exceptions import ParseError


class UrlsList(generics.ListAPIView):
    serializer_class = UrlSerializerMany
    queryset = Url.objects.all()


class DocumentListView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializerMany


class DocumentSingleView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class DocumentCreateView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        filename, file_ext = os.path.splitext(file_obj.name)
        if file_ext.lower() != '.pdf' \
                or file_obj.content_type != 'application/pdf':
            raise ParseError('Only PDF files are allowed')
        parsed_urls = set()
        try:
            parsed_urls = set(extract_urls_from_pdf(file_obj))
        except:
            '''
            I have used a bare except here because I don't know
            which exactly exceptions I could get
            '''
            raise ParseError('Cannot parse the PDF file')
        document, created = Document.objects.get_or_create(name=filename)
        exist_urls = set(Url.objects.values_list('address', flat=True))
        urls_to_update = parsed_urls & exist_urls
        urls_to_create = parsed_urls - exist_urls
        if urls_to_update:
            for url in Url.objects.filter(address__in=urls_to_update):
                url.documents.add(document)
        if urls_to_create:
            urls = Url.objects.bulk_create(
                Url(
                    address=url
                ) for url in urls_to_create
            )
            document.urls.add(*urls)
        return Response(204)
