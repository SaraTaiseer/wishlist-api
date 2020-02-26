from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item,FavoriteItem

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=['username','password']

    def create(self,validate_data):
        username=validate_data['username']
        password=validate_data['password']
        new_user=User('username')
        new_user.set_password(password)
        new_user.save()
        return validate_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['first_name','last_name']


class ItemSerializer(serializers.ModelSerializer):
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    class Meta:
        model = Item
        fields=['name','added_by','description','favourited','detail']

    def get_favourited(self,obj):
        favourites=FavoriteItem.objects.filter(user=obj.added_by)
        count=0
        for fav in favourites:
            count +=1
        return count



class ItemDetailsSerializer(serializers.ModelSerializer):
    favourited_by =serializers.SerializerMethodField()
    class Meta:
        model =Item
        fields=['image','name','description','favourited_by']
    def get_favourited_by(self,obj):
        favourites=FavoriteItem.objects.filter(user=obj.added_by)
        return favourites
