from rest_framework import serializers

from test_app.models import TestModel

class SimpleSerializer(serializers.Serializer):

    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.CharField()
    is_alive = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        TestModel.objects.filter(id=instance.id).update(**validated_data)
        return TestModel.objects.get(id=instance.id)