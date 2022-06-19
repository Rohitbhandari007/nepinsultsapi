from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Insult
from .serializers import InsultSerializer

import random


@api_view(['GET'])
def getData(request):

    insults = list(Insult.objects.all())
    random_insult = random.choice(insults)
    serializer = InsultSerializer(random_insult)

    return Response(serializer.data)


