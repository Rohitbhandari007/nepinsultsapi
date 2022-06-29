from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Insult
from .serializers import InsultSerializer
#random
from random import choice


@api_view(['GET'])
def getData(request):
    insults = Insult.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = A.objects.get(pk=random_pk)
    serializer = InsultSerializer(random_insult)
    return Response(serializer.data)


