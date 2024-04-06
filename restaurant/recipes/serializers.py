from rest_framework import serializers
from .models import Chef, Recipe


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'

class RecipeSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

        