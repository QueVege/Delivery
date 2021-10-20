from rest_framework import serializers
from .models import (
    Company, Category, Driver, Transport
)


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    drivers = serializers.HyperlinkedIdentityField(
        view_name='driver-list')

    transport = serializers.HyperlinkedIdentityField(
        view_name='transport-list')

    class Meta:
        model = Company
        fields = (
            'url',
            'name',
            'drivers',
            'transport'
        )


class DriverSerializer(serializers.HyperlinkedModelSerializer):

    company = serializers.ReadOnlyField(source='company.name')

    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='category',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Driver
        fields = (
            'url',
            'first_name',
            'last_name',
            'categories',
            'company'
        )


class TransportSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        drivers = data.get('drivers')
        category = data.get('required_category')

        pk = self.context.get('pk')
        if pk:
            company = Company.objects.get(id=pk)            # create transport (get company by pk)
        else:
            company = self.instance.company                 # update transport (company already exists)

        if drivers:
            for driver in drivers:
                if category not in driver.categories.all():
                    raise serializers.ValidationError(
                        'The driver\'s category doesn\'t match the transport\'s category.')
                elif company != driver.company:
                    raise serializers.ValidationError(
                        'The driver\'s company doesn\'t match the transport\'s company.')
        return data

    company = serializers.ReadOnlyField(source='company.name')

    required_category = serializers.SlugRelatedField(
        slug_field='category',
        queryset=Category.objects.all()
    )

    drivers = serializers.HyperlinkedRelatedField(
        view_name='driver-detail',
        queryset=Driver.objects.all(),
        many=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Transport
        fields = (
            'url',
            'number',
            'model',
            'company',
            'required_category',
            'drivers'
        )

