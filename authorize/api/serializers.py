from rest_framework import serializers

from authorize.models import Menu


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MenuOutwardSerializer(DynamicFieldsModelSerializer):

    class Meta:

        model = Menu

        fields = (
            'id',
            'name',
            'code',
        )


class MenuCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Menu

        fields = (
            'id',
            'name',
            'code',
        )

    def validate(self, attrs):

        return attrs

    def create(self, validated_data):

        return Menu.objects.create(name=validated_data['name'], code=validated_data['code'])


class MenuUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Menu

        fields = (
            'id',
            'name',
            'code',
        )

    def validate(self, attrs):

        return attrs

    def update(self, instance, validated_data):

        instance.name = instance.name

        instance.code = instance.code

        instance.save()

        return instance
