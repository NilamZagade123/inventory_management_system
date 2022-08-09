from django.views import generic
from .models import Supplier, Inventory
from .serializer import InventoryReadSerializer,InventoryDataReadSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class GetInventoryView(viewsets.GenericViewSet):
    # specify serializer to be used
    serializer_class =InventoryReadSerializer

    def list(self, request,name=None, *args, **kwargs):
        name = self.request.query_params.get('name',None)
        #access all inventory details
        queryset = Inventory.objects.all() 

        if name: 
            #if user add name filter then it will filter by name
            queryset = queryset.filter(name=name)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)
                  



class GetInventoryDetailsView(generic.TemplateView):
    # specify serializer to be used
    serializer_class =InventoryDataReadSerializer
    # specify template to be used
    template_name = 'index.html'

    # override context data
    def get_context_data(self, **kwargs):
        context = super(GetInventoryDetailsView, self).get_context_data(**kwargs)
        id = self.kwargs.get('id')
        if id:
            queryset_object = Inventory.objects.filter(id=id).first
            # add extra field 
            context['data'] = queryset_object
        return context
