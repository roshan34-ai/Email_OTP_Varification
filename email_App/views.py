from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser
from rest_framework import status

# Create your views here.
class UserRegister(APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.data['email']
            subject = "Your Account Varification Mail."
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            message = f"Your account varification code is {otp}"
            email_from = settings.EMAIL_HOST
            send_mail(subject, message, email_from, [email]) 
            # user_obj = CustomUser.objects.get(email=email)
            # # user_obj.otp=otp
            # user_obj.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Varify_otp(APIView):

    def post(self, request):
        data = request.data

        serializer = varifyAccountSerializer(data=data)

        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']

            user = CustomUser.objects.filter(email=email)
            
            if not user.exists():
                return Response({
                    'status':400,
                    'message':'Something went wrong',
                    'data':'Invalid email'
                    })
                    
            user = user.first()
            s_otp = request.session.get('otp')
            if str(s_otp) != otp:
                return Response({'status':400,
                                'message':'Something went wrong',
                                'data':'Invalid otp'
                                })      

            
            user.is_varified = True
            user.save()
            return Response({'status':400,
                            'message':'Email Varified'
                            })   