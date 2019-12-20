import requests
from requests.exceptions import (
    ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
    ProxyError, RetryError, InvalidSchema, InvalidProxyURL,
    InvalidURL
)


from rest_framework import serializers
from crawler.models import Document, Url

network_exceptions = (
    ConnectionError, ConnectTimeout, ReadTimeout, SSLError,
    ProxyError, RetryError, InvalidSchema, InvalidProxyURL,
    InvalidURL
)


class IsAliveMixin(object):
    __metaclass__ = serializers.SerializerMetaclass
    is_alive = serializers.SerializerMethodField()

    def get_is_alive(self, obj):
        try:
            response = requests.get(obj.address, timeout=1)
            result = response.status_code == 200
        except network_exceptions:
            result = False
        return result


class UrlSerializer(IsAliveMixin, serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('address', 'is_alive')


class UrlSerializerMany(IsAliveMixin, serializers.ModelSerializer):
    documents_count = serializers.IntegerField(
        source='documents.count',
        read_only=True
    )

    class Meta:
        model = Url
        fields = ('address', 'documents_count', 'is_alive')


class DocumentSerializerMany(serializers.ModelSerializer):
    urls_count = serializers.IntegerField(
        source='urls.count',
        read_only=True
    )

    class Meta:
        model = Document
        fields = ('id', 'name', 'urls_count')


class DocumentSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(read_only=True, many=True)

    class Meta:
        model = Document
        fields = ('id', 'name', 'urls')
