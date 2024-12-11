from rest_framework.decorators import api_view
from rest_framework.response import Response


# testing how to create functions to manage requests from API
# yess!!!!!! fuck yesss!!!!1
@api_view(['GET','POST'])
def index(request):
    courses = {
        "course" : 'python',
        'learn' : ['c++', 'django'],
    }
    if request.method == 'GET':
        return Response(courses)