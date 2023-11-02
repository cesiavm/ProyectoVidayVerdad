from rest_framework import serializers
from curso_app.models import Curso,Grado, Turno
from django.shortcuts import render

# class CursoRSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model=Curso
#         fields="__all__"

    
class GradoSerializer(serializers.ModelSerializer):
    # cursos=serializers.HyperlinkedIdentityField(
    #     many=True,
    #     read_only=True,
    #     view_name='curso-detalle'
    #     )
    # cursos=CursoRSerializer(many=True, read_only=True)
    class Meta :
        model=Grado
        fields="__all__"
    
class TurnoSerializer(serializers.ModelSerializer):
    class Meta :
        model=Turno
        fields="__all__"

class CursoSerializer(serializers.ModelSerializer):
    grado = GradoSerializer()
    turno = TurnoSerializer()
    class Meta:
        model=Curso
        fields= ['grado', 'turno', 'capacidad_estudiantes', 'cantidad_estudiantes', 'cantidad_asignaturas', 'active']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['grado'] = instance.grado.nombre_grado
        representation['turno'] = instance.turno.nombre_turno
        
        return render(representation,"../core/templates/core/home.html")


# def column_longitud(value):
#     if len(value)<2:
#         raise serializers.ValidationError("La informacion es muy corta")
    
# class GradoSerializer(serializers.Serializer):
#     id_grado = serializers.IntegerField(read_only=True)
#     nombre_grado = serializers.CharField(max_length=50)

# class TurnoSerializer(serializers.Serializer):
#     id_turno = serializers.IntegerField(read_only=True)
#     nombre_turno = serializers.CharField(max_length=30)

# class CursoSerializer(serializers.Serializer):
#     id_curso=serializers.IntegerField(read_only=True)
#     grado = GradoSerializer()  # Incluye el serializador de Grado
#     turno = TurnoSerializer() 
#     capacidad_estudiantes=serializers.IntegerField()
#     cantidad_estudiantes=serializers.IntegerField()
#     cantidad_asignaturas=serializers.IntegerField()
    
#     def create(self, validated_data):
#         grado_data = validated_data.pop('grado')
#         turno_data = validated_data.pop('turno')
#         grado_instance = Grado.objects.create(**grado_data)
#         turno_instance = Turno.objects.create(**turno_data)
#         curso_instance = Curso.objects.create(grado=grado_instance, turno=turno_instance, **validated_data)
#         return curso_instance
    
#     def update(self,instance,validated_data):
#         instance.capacidad_estudiantes = validated_data.get('capacidad_estudiantes',instance.capacidad_estudiantes)
#         instance.cantidad_estudiantes = validated_data.get('cantidad_estudiantes',instance.cantidad_estudiantes)
#         instance.cantidad_asignaturas = validated_data.get('cantidad_asignaturas',instance.cantidad_asignaturas)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
