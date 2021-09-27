from rest_framework import serializers

from event_controller.models import EventFeature, EventMain, EventAttender
from user.serializers import AddressGlobalSerializer, CustomUserSerializer

class EventFeatureSerializer(serializers.ModelSerializer):

    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = EventFeature
        fields = '__all__'


class EventMainSerializer(serializers.ModelSerializer):

    author = serializers.CharField(required=False)
    author_email = serializers.ReadOnlyField(source='author.email', read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    address_info = AddressGlobalSerializer(read_only=True)
    address_info_id = serializers.IntegerField(write_only=True)
    event_features = EventFeatureSerializer(read_only=True, many=True)
    attenders = serializers.SerializerMethodField('get_attenders')

    class Meta:
        model = EventMain
        fields = '__all__'

    def get_attenders(self, obj):
        attenders = obj.event_attenders.all().count()
        return attenders


class EventAttenderSerializer(serializers.ModelSerializer):

    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.IntegerField(write_only=True)
    user = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = EventAttender
        fields = '__all__'
