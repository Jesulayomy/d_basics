from rest_framework import serializers

from core.models import (
    Family,
    Person,
)

class FamilySerializer(serializers.Serializer):
    """Fam Serializer """

    class Meta:
        model = Family
        fields = '__all__'
