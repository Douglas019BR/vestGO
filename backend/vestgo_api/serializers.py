from rest_framework import serializers

from django.contrib.auth.models import Group


from vestgo_api.models import School, CustomUser


class CustomUserCreateListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(default=False)
    name = serializers.CharField(required=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), required=False, allow_null=True
    )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        if not user.is_staff:
            group = Group.objects.get(name="Main")
            user.groups.add(group)

        return user


class CustomUserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    is_staff = serializers.BooleanField(required=False)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), required=False, allow_null=True
    )

    def update(self, instance, validated_data: dict):
        for attr, value in validated_data.items():
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class CustomUserRetrieveSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    name = serializers.CharField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    school = serializers.SerializerMethodField()

    def get_school(self, obj: CustomUser) -> dict:
        if obj.school:
            return {"id": obj.school.id, "name": obj.school.name}
        return None
