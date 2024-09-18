from rest_framework import serializers
from api.models import Products,Carts
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)                      #read only: tablil ninn get cheyth searialize cheyyan mathram.no deserialization
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    catogory=serializers.CharField()
    image=serializers.ImageField(required=False,default=None)

 
class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:

        model=Products
        fields="__all__"
        # fields=["name","price","description"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User
        fields=["first_name","last_name","email","username","password"]
    


    def create(self, validated_data):       #save le create ne update cheyyan parentile creatine childk override cheythu  
        return User.objects.create_user(**self.validated_data)       #to hide password


class CartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True) 
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:

        model=Carts
        fields="__all__"
