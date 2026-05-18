from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


def inicio(request):
    token = request.GET.get("token")
    return render(request, 'HTML/Pagina_Inicio.html', {'jwt_token' : token })

def login(request):
    return render(request,'HTML/Login.html')


#@api_view(['GET'])
#@permission_classes([IsAuthenticated])

#def comprobar_token(request):
 #   return Response({
   #     "ok": True
   # })

class comprobar_token(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "ok": True
        })
