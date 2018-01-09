# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', ])
def home_view(requests):
    """
    主页视图
    """
    return Response({'result': 'OK'})
