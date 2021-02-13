from rest_framework import serializers

from .models import Package, Journal



class PackageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package
        fields = ('id', 'name', 'min_value', 'max_value', 'coefficient')


class JournalSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    package = serializers.StringRelatedField()
    
    
    class Meta:
        model = Journal
        fields = (
                    'id', 'user', 'package', 
                    'date', 'package', 'old_balance', 
                    'new_balance', 'coefficient'
                 )
