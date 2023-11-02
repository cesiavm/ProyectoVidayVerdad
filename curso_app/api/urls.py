from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from cursolist_app.api.views import curso_list,curso_detalle
#from cursolist_app.api.views import (CursoCreate,CursoListAV,CursoDetalleAV,
   #                                  TurnoCursoList,TurnoList,TurnoDetail)
from . import views
from curso_app.api.views import CursoList,TurnoCursoList,TurnoList,TurnoDetail
# router=DefaultRouter()
# router.register('curso',CursoVS,basename='curso')
urlpatterns = [
    #path('',include(router.urls)),
    # path('curso-create/',CursoCreate.as_view(),name='curso-create'),
    path('curso/', CursoList.as_view(), name='curso-list'),
    # path('curso/<int:pk>',CursoDetalleAV.as_view(), name='curso-detail'),
    path('curso/turno/<int:pk>',TurnoCursoList.as_view(), name='turnocurso-list'),
    path('turno/',TurnoList.as_view(), name='turno-list'),
    path('turno/<int:pk>',TurnoDetail.as_view(), name='turno-detail'),
    # path('curso/turno/',TurnoListAV.as_view(), name='turno-list'),
    # path('turno/<int:pk>',TurnoDetalleAV.as_view(), name='turno-detail'),
]
