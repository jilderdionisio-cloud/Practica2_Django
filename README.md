# Orderflow API

API REST creada con Django y Django REST Framework para gestionar clientes y pedidos.

## Tecnologias

- Python
- Django 6.0.5
- Django REST Framework 3.17.1
- SQLite

## Requisitos

- Python 3
- pip
- PowerShell o terminal compatible

## Instalacion

Clona el proyecto y entra a la carpeta:

```powershell
cd C:\orderflow_api
```

Crea y activa un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
pip install -r requirements.txt
```

Aplica las migraciones:

```powershell
python manage.py migrate
```

Ejecuta el servidor:

```powershell
python manage.py runserver
```

La API queda disponible en:

```text
http://127.0.0.1:8000/api/
```

## Modelos

### Cliente

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| id | AutoField | Identificador del cliente |
| nombre | CharField | Nombre del cliente |
| direccion | CharField | Direccion del cliente |

### Pedido

| Campo | Tipo | Descripcion |
| --- | --- | --- |
| id | AutoField | Identificador del pedido |
| cliente | ForeignKey | Cliente asociado al pedido |
| fecha | DateField | Fecha creada automaticamente |
| monto_total | DecimalField | Monto total del pedido |
| estado | CharField | Estado del pedido |

Estados disponibles para un pedido:

- `pendiente`
- `en_proceso`
- `entregado`
- `cancelado`

## Endpoints

### Clientes

| Metodo | Endpoint | Descripcion |
| --- | --- | --- |
| GET | `/api/clientes/` | Listar clientes |
| POST | `/api/clientes/` | Crear cliente |
| GET | `/api/clientes/{id}/` | Obtener cliente por ID |
| PUT | `/api/clientes/{id}/` | Actualizar cliente completo |
| PATCH | `/api/clientes/{id}/` | Actualizar cliente parcialmente |
| DELETE | `/api/clientes/{id}/` | Eliminar cliente |

### Pedidos

| Metodo | Endpoint | Descripcion |
| --- | --- | --- |
| GET | `/api/pedidos/` | Listar pedidos |
| POST | `/api/pedidos/` | Crear pedido |
| GET | `/api/pedidos/{id}/` | Obtener pedido por ID |
| PUT | `/api/pedidos/{id}/` | Actualizar pedido completo |
| PATCH | `/api/pedidos/{id}/` | Actualizar pedido parcialmente |
| DELETE | `/api/pedidos/{id}/` | Eliminar pedido |

## Busqueda de pedidos

Los pedidos se pueden buscar por estado o por nombre del cliente usando el parametro `search`.

Ejemplos:

```text
GET /api/pedidos/?search=pendiente
GET /api/pedidos/?search=Juan
```

## Ejemplos de JSON

Crear cliente:

```json
{
  "nombre": "Juan Perez",
  "direccion": "Av. Principal 123"
}
```

Crear pedido:

```json
{
  "cliente": 1,
  "monto_total": "150.00",
  "estado": "pendiente"
}
```

Respuesta de pedido:

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

## Comandos utiles

Crear migraciones:

```powershell
python manage.py makemigrations
```

Aplicar migraciones:

```powershell
python manage.py migrate
```

Verificar el proyecto:

```powershell
python manage.py check
```
