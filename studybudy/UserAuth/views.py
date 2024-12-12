from rest_framework.response import Response
from UserAuth.models import person
from UserAuth.serializers import peopleSerializer,SignupSerializer,LoginSerializer,UpdateProfileSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated


# for signup
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print({"message": "User registered successfully!"})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# for login
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "success": True,
                "message": "Login successful",
                "data": {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email
                    }
                },
                'message': 'Please update your profile to complete your account setup.'
            }, status=status.HTTP_200_OK)
        return Response({'success': False, 'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#for user info in dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user  = request.user
    return Response({
        "id" : user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender" : user.gender,
        "phone_number" : user.phone_number,
        "date_of_birth" : user.date_of_birth
    }, status=status.HTTP_200_OK)


#for user to update his/her profile
@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def Update_Profile(request):
    user = request.user
    serializer = UpdateProfileSerializer(user, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message" : "Profile updated successfully",
            "user" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# to delete user profile
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    user = request.user
    if user:
        user.delete()
        return Response({"message": "User profile deleted successfully."}, status=status.HTTP_200_OK)
    return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
