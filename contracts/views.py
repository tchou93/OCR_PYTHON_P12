from rest_framework.viewsets import ModelViewSet

from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractView(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()
