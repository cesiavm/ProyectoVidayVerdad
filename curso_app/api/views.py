from collections import Counter
from itertools import groupby
from django.shortcuts import get_object_or_404
from curso_app.models import Curso,Grado,Turno
from rest_framework.renderers import TemplateHTMLRenderer
from curso_app.api.serializers import CursoSerializer,GradoSerializer,TurnoSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render
from django_filters import rest_framework as filters


class TurnoList(generics.ListCreateAPIView):
     queryset=Turno.objects.all()
     serializer_class=TurnoSerializer
     

class TurnoCursoList(generics.ListAPIView):
    serializer_class=CursoSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Curso.objects.filter(grado=pk)
    
class TurnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Turno.objects.all()
    serializer_class=TurnoSerializer

# class CursoVS(viewsets.ModelViewSet):
#     queryset=Curso.objects.all()
#     serializer_class=CursoSerializer
   
# class CursoCreate(generics.CreateAPIView):
#      queryset=Curso.objects.all()
#      serializer_class=CursoSerializer
     
class CursoList(APIView):
      renderer_classes=[TemplateHTMLRenderer]
      template_name = 'curso_app/curso_list.html'  # Ruta al archivo de template
      context_object_name = 'cursos'  # Nombre del contexto que se usará en el template

      def get(self, request):
        cursos = Curso.objects.all().order_by('turno__nombre_turno', 'grado__nivel__nombre_nivel','fecha_registro')

        grouped_cursos = []
        for nombre_turno, cursos_por_turno in groupby(cursos, key=lambda x: x.turno.nombre_turno):
            turnos = []
            for nombre_nivel, cursos_por_nivel in groupby(cursos_por_turno, key=lambda x: x.grado.nivel.nombre_nivel):
                turnos.append({
                    'nombre_nivel': nombre_nivel,
                    'cursos': list(cursos_por_nivel),
                })
            grouped_cursos.append({
                'nombre_turno': nombre_turno,
                'turnos': turnos,
            })

        return Response({'cursos': grouped_cursos})
    
        #cursos = Curso.objects.all().order_by('turno')
    #     cursos = Curso.objects.all().order_by('turno', 'grado__nivel__nombre_nivel')\
    #         .values('turno', 'grado__nivel__nombre_nivel', 'grado__nombre_grado')\
            
    #     # Agrupa los cursos por turno
    #     grouped_cursos = []
        
    # #     for key, group in groupby(cursos, key=lambda x: (x.turno, x.grado.nivel)):
    # #         grouped_cursos.append({
    # #     'nombre_turno': key[0],
    # #     'nombre_nivel': key[1],
    # #     'cursos': list(group),
    # # })
    #     for curso in cursos:
    #         turno = curso['turno']
    #         nivel = curso['grado__nivel__nombre_nivel']
    #         nombre_curso = curso['grado__nombre_grado']
           
    #         grouped_cursos.append({
    #             'turno': turno,
    #             'nivel': nivel,
    #             'cursos': [{'nombre_curso': nombre_curso}] 
    #     })

        # Pasar la lista como contexto a la plantilla
       
    
    
# class CursoListAV(APIView):
    
#     def get(self, request):
#         cursos=Curso.objects.all()
#         serializer=CursoSerializer(cursos,many=True,context={'request':request})
#         return Response(serializer.data)        

#     def post(self, request):
#         serializer=CursoSerializer(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class CursoDetalleAV(APIView):
#     def get(self, request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer= CursoSerializer(curso,context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=CursoSerializer(curso,data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
#         try:
#             curso=Curso.objects.get(pk=pk)
#         except Curso.DoesNotExist:
#             return Response({'error':'Curso no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
#         curso.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST']) 
# def curso_list(request):
#     if request.method=='GET':
#         cursos=Curso.objects.all()
#         serializer=CursoSerializer(cursos,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         de_serializer=CursoSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
        
# @api_view(['GET','PUT','DELETE'])
# def curso_detalle(request,pk):
#     if request.method=='GET':
#         try:
#             curso=Curso.objects.get(pk=pk)
#             serializer=CursoSerializer(curso)
#             return Response(serializer.data)
#         except Curso.DoesNotExist:
#             return Response({'Error':'el curso no existe'},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='PUT':
#         curso=Curso.objects.get(pk=pk)
#         de_serializer=CursoSerializer(curso,data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method=='DELETE':
#         try:
#             curso=Curso.objects.get(pk=pk)
#             curso.delete()
#         except Curso.DoesNotExist:
#             return Response({'Error':'El Curso no existe'},status=status.HTTP_404_NOT_FOUND)
#         return Response (status=status.HTTP_204_NO_CONTENT)
        