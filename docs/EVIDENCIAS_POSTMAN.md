# Evidencias para Postman

Este documento sirve como guia para demostrar en Postman que la API cumple con la actividad del Gestor de Pedidos.

## Preparacion

1. Ejecutar el servidor:

```powershell
python manage.py runserver
```

2. Abrir Postman.
3. Importar la coleccion:

```text
postman/orderflow_api.postman_collection.json
```

4. Verificar que la variable `base_url` tenga este valor:

```text
http://127.0.0.1:8000/api
```

## Evidencias que debes capturar

### 1. CRUD de Clientes

Entidad 2: Clientes.

#### Crear cliente

Solicitud:

```text
POST {{base_url}}/clientes/
```

Body:

```json
{
  "nombre": "Juan Perez",
  "direccion": "Av. Principal 123"
}
```

Evidencia esperada:

- Status `201 Created`.
- Respuesta con `id`, `nombre` y `direccion`.

#### Listar clientes

Solicitud:

```text
GET {{base_url}}/clientes/
```

Evidencia esperada:

- Status `200 OK`.
- Lista de clientes.

#### Editar cliente

Solicitud:

```text
PATCH {{base_url}}/clientes/{{cliente_id}}/
```

Body:

```json
{
  "direccion": "Av. Actualizada 456"
}
```

Evidencia esperada:

- Status `200 OK`.
- El campo `direccion` cambia.

#### Eliminar cliente

Esta prueba debe hacerse al final, despues de eliminar los pedidos relacionados.

Solicitud:

```text
DELETE {{base_url}}/clientes/{{cliente_id}}/
```

Evidencia esperada:

- Status `204 No Content`.

## 2. CRUD de Pedidos

Entidad 1: Pedidos.

#### Crear pedido

Solicitud:

```text
POST {{base_url}}/pedidos/
```

Body:

```json
{
  "cliente": 1,
  "monto_total": "150.00",
  "estado": "pendiente"
}
```

Evidencia esperada:

- Status `201 Created`.
- Respuesta con `id`, `cliente`, `fecha`, `monto_total` y `estado`.
- Respuesta personalizada con `cliente_nombre` y `cliente_direccion`.

#### Listar pedidos

Solicitud:

```text
GET {{base_url}}/pedidos/
```

Evidencia esperada:

- Status `200 OK`.
- Lista de pedidos.
- Cada pedido muestra datos del cliente asociado.

#### Buscar pedidos por estado

Solicitud:

```text
GET {{base_url}}/pedidos/?search=pendiente
```

Evidencia esperada:

- Status `200 OK`.
- Lista filtrada por el estado `pendiente`.

#### Buscar pedidos por nombre del cliente

Solicitud:

```text
GET {{base_url}}/pedidos/?search=Juan
```

Evidencia esperada:

- Status `200 OK`.
- Lista filtrada por nombre del cliente.

#### Editar pedido

Solicitud:

```text
PATCH {{base_url}}/pedidos/{{pedido_id}}/
```

Body:

```json
{
  "estado": "entregado"
}
```

Evidencia esperada:

- Status `200 OK`.
- El campo `estado` cambia a `entregado`.

#### Eliminar pedido

Solicitud:

```text
DELETE {{base_url}}/pedidos/{{pedido_id}}/
```

Evidencia esperada:

- Status `204 No Content`.

## Relacion entre entidades

La relacion se demuestra en la respuesta del endpoint de pedidos:

```json
{
  "id": 1,
  "cliente": 1,
  "cliente_nombre": "Juan Perez",
  "cliente_direccion": "Av. Principal 123",
  "fecha": "2026-05-09",
  "monto_total": "150.00",
  "estado": "pendiente"
}
```

Esto prueba que cada pedido esta relacionado con un cliente y que el serializer personaliza la respuesta mostrando informacion de la entidad asociada.

## Tabla de cumplimiento

| Requisito | Endpoint | Evidencia |
| --- | --- | --- |
| Listado de Pedidos | `GET /api/pedidos/` | Status 200 y lista de pedidos |
| Creacion de Pedidos | `POST /api/pedidos/` | Status 201 y JSON del pedido creado |
| Edicion de Pedidos | `PUT/PATCH /api/pedidos/{id}/` | Status 200 y datos actualizados |
| Eliminacion de Pedidos | `DELETE /api/pedidos/{id}/` | Status 204 |
| Busqueda de Pedidos | `GET /api/pedidos/?search=` | Status 200 y resultados filtrados |
| Relacion Pedido-Cliente | `GET /api/pedidos/` | Campos `cliente_nombre` y `cliente_direccion` |
| CRUD de Clientes | `/api/clientes/` | GET, POST, PATCH/PUT y DELETE funcionales |
| Punto extra | `/api/pedidos/` | Respuesta personalizada con datos del cliente |

## Nota sobre Django Admin

El archivo `config/urls.py` no expone la ruta `/admin/`. La gestion se realiza mediante endpoints de Django REST Framework.
