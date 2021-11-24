from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'}, write_only = True)
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)
    email = serializers.EmailField(validators= [UniqueValidator(User.objects.all())],required = True)


    class Meta:
        model = User
        fields = ['url','pk', 'username','email', 'password','password2']


    def validate(self, validated_data):
        user = self.context['request'].user
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'password':"Password must match!"})    
        elif not any(c.isupper() for c in validated_data['password']):
            raise serializers.ValidationError({'password':"must contain atleast one capital letter!"})
        return validated_data


    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk = user.pk).filter(email = value).exists():
            raise serializers.ValidationError("email address already taken!")
        return value    

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email= validated_data['email'],
        )    
        user.set_password(validated_data['password'])
        user.save()
        
        return user

    
    
class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(validators= [UniqueValidator(User.objects.all())],
                                required = True,
                            )                   
    class Meta:
        model = User
        fields = ['url','username','email']


    def update(self, instance, validated_data):
        user = self.context['request'].user
        
        if user.pk != instance.pk:
            raise serializers.ValidationError("You don't have permission to update this user!")

        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.save()    

        return instance
