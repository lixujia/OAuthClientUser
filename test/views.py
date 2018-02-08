# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', ])
def home_view(requests):
    """
    主页视图
    """
    return Response({'result': 'OK', 'user': requests.user.username if not isinstance(requests.user, AnonymousUser) else 'None'})
