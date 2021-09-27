from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from event_controller.models import EventFeature, EventMain
from event_controller.serializers import EventFeatureSerializer, EventMainSerializer
from user.serializers import AddressGlobalSerializer, CustomUserSerializer
from user.models import AddressGlobal

# Create your views here.

class EventMainView(ModelViewSet):

    serializer_class = EventMainSerializer
    queryset = EventMain.objects.select_related('author', 'address_info').prefetch_related('event_features')

    def create(self, request, *args, **kwargs):
        a_serializer = AddressGlobalSerializer(data=request.data)
        a_serializer.is_valid(raise_exception=True)
        a_serializer.save()

        data = {**request.data, 'address_info_id': a_serializer.data['id']}

        e_serializer = self.serializer_class(data=data)
        if not e_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data['id']).delete()
            raise Exception(e_serializer.errors)
        e_serializer.save()

        features = request.data.get('features', None)
        if not features:
            AddressGlobal.objects.filter(id=a_serializer.data['id']).delete()
            raise Exception('Feature field is required')

        if not isinstance(features, list):
            features = [features]

        data = []
        for f in features:
            if not isinstance(f, dict):
                AddressGlobal.objects.filter(id=a_serializer.data['id']).delete()
                raise Exception('Feature instance must be an objects.')
            data.append({
                **f, 'eventmain_id': e_serializer.data['id']
            })

        f_serializer = EventFeatureSerializer(data=data, many=True)
        if not f_serializer.is_valid():
            AddressGlobal.objects.filter(id=a_serializer.data['id']).delete()
            raise Exception(f_serializer)
        f_serializer.save()

        return Response(self.serializer_class(self.get_queryset().get(id=e_serializer.data['id'])).data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        evt_serializer = self.serializer_class(data=request.data, instance=instance, partial=True)
        evt_serializer.is_valid(raise_exception=True)
        evt_serializer.save()

        address_serializer = AddressGlobalSerializer(data=request.data, instance=instance.address_info, partial=True)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        features = request.data.get('features', None)
        if features:
            if not isinstance(features, list):
                features = [features]

            data = []

            for f in features:
                if not isinstance(f, dict):
                    raise Exception('Feature must be an object')
                data.append({
                    **f,
                    'eventmain_id': evt_serializer.data['id']
                })

            f_serializers = EventFeatureSerializer(data=data, many=True)
            f_serializers.is_valid(raise_exception=True)
            f_serializers.save()

        return Response(self.serializer_class(self.get_object()).data)