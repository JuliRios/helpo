from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from actividades.models import Actividad, Organizacion, TipoDeOrganizacion
from actividades.serializers import ActividadSerializer, OrganizacionSerializer, TipoDeOrganizacionSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actividades to be viewed or edited.
    """
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class OrganizacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organizaciones to be viewed or edited.
    """
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer

class TipoDeOrganizacionCreateReadView(ListCreateAPIView):
    """
    API endpoint para crear o ver todos los tipos de organizacion
    """
    queryset = TipoDeOrganizacion.objects.all()
    serializer_class = TipoDeOrganizacionSerializer

class TipoDeOrganizacionReadUpdateDeleteView( RetrieveUpdateDestroyAPIView):
    """
    API endpoint para leer, actualizar o eliminar un tipo de organizacion
    """
    queryset = TipoDeOrganizacion.objects.all()
    serializer_class = TipoDeOrganizacionSerializer
    lookup_field = 'id'