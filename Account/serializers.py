from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, Student, Teacher, Follow


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class StudentSerializer(CustomUserSerializer):
    is_student = serializers.BooleanField(default=True)

    class Meta(CustomUserSerializer.Meta):
        model = Student
        fields = CustomUserSerializer.Meta.fields + ['is_student']

    def create(self, validated_data):
        student = Student.objects.create_user(**validated_data)
        return student


class TeacherSerializer(CustomUserSerializer):
    is_teacher = serializers.BooleanField(default=True)

    class Meta(CustomUserSerializer.Meta):
        model = Teacher
        fields = CustomUserSerializer.Meta.fields + ['is_teacher']

    def create(self, validated_data):
        teacher = Teacher.objects.create_user(**validated_data)
        return teacher


class AccountantSerializer(CustomUserSerializer):
    is_accountant = serializers.BooleanField(default=True)

    class Meta(CustomUserSerializer.Meta):
        model = CustomUser
        fields = CustomUserSerializer.Meta.fields + ['is_accountant']

    def create(self, validated_data):
        accountant = CustomUser.objects.create_user(**validated_data)
        return accountant


class UserSignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'address', 'position', 'is_teacher', 'email',
                  'is_accountant', 'is_student', 'is_superuser']


class TeacherViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'first_name', 'last_name', 'bio']


class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'bio']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8)