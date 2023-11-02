from django.db import models


# Create your models here.
class Trimestre(models.Model):
    id_trimestre = models.AutoField(primary_key=True)
    numero_trimestre = models.CharField(max_length=30,verbose_name='Trimestre')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'trimestre' 

    def __str__(self):
        return self. numero_trimestre
    
class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nombre_nivel = models.CharField(max_length=50,verbose_name='Nombre Nivel')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'nivel' 

    def __str__(self):
        return self.nombre_nivel
    
class Grado(models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre_grado = models.CharField(max_length=50)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE,db_column='nivel', to_field='id_nivel')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'grado' 
    def __str__(self):
        return self.nombre_grado
    
class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nombre_turno = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'turno' 
    def __str__(self):
        return self.nombre_turno 

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE,db_column='grado', to_field='id_grado',related_name="cursos")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE,db_column='turno', to_field='id_turno')
    capacidad_estudiantes = models.IntegerField()
    cantidad_estudiantes = models.IntegerField(default=0)
    cantidad_asignaturas = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'curso' 
    def __str__(self):
        return f"Curso {self.id_curso}"
    

