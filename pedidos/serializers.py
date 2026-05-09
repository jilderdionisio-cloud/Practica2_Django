from rest_framework import serializers
from .models import Cliente, Pedido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    cliente_direccion = serializers.CharField(source='cliente.direccion', read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'cliente_direccion',
            'fecha',
            'monto_total',
            'estado'
        ]