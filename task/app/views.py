from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,decorators, viewsets
from django.contrib.auth.models import User
from app.models import UserProfile, Contacts
from rest_framework import status
# Create your views here.


class SearchNameViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    @decorators.action(detail = False, methods=['post'],url_path="search-name")
    def search_name(self, request):
        data = request.data
        name = data.get("name")
        names = Contacts.objects.filter(name__icontains = name)
        data = []
        for name in names:
            x = {
                "name": name.name,
                "phone": name.phone,
                "spam":name.spam
            }
            user = UserProfile.objects.filter(phone=name.phone).first()
            if user:
                x["email"] = user.user.email

            data.append(x)
        return Response(data=data, status=status.HTTP_201_CREATED)


class SearchNumberViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    @decorators.action(detail = False, methods=['post'],url_path="search-number")
    def search_number(self, request):
        data = request.data
        phone = data.get("phone")
        names = Contacts.objects.filter(phone = phone)
        data = []
        for name in names:
            x = {
                "name": name.name,
                "phone": name.phone,
                "spam":name.spam
            }
            user = UserProfile.objects.filter(phone=name.phone).first()
            if user:
                x["email"] = user.user.email

            data.append(x)


        return Response(data=data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    @decorators.action(detail = False, methods = ['post'],url_path = "register-user")
    def register_user(self,request):
        user_data = request.data
        phone = user_data.get("phone")
        email = user_data.get("email")
        name = user_data.get("user")
        password = user_data.get("password")
        user, exists = User.objects.get_or_create(username=name,email = email)
        if not exists:
            return Response("user already exist" , status =status.HTTP_201_CREATED)
        user.set_password(password)
        user.save()
        user_profile = UserProfile(phone = phone, user=user )

        user_profile.save()
        Contacts.objects.create(name = name , phone=phone,spam=False, user=user_profile)

        data = {
            "msg":"created new enter"
        }
        return Response(data=data , status =status.HTTP_201_CREATED)


class SpamViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    @decorators.action(detail = False, methods=['post'],url_path="mark-spam")
    def mark_spam(self,request):
        request_data = request.data
        phone = request_data.get("phone")
        contact = Contacts(phone = phone,spam = True )
        contact.save()
        return Response("marked spam Successfully")

class TestUser(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    @decorators.action(detail = False, methods=['get'],url_path="ping")
    def ping(self,request):
        return Response("pong")
