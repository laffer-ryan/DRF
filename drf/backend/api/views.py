from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF - API view
    """
    serializer = ProductSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True): # raise_exception will good error message on model issues
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)