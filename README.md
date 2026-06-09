# Catálogo de Productos - Entrega 1

## Descripción
Proyecto de software basado en Docker que implementa un sistema de catálogo de productos.

## Tecnologías
- Python (Flask)
- MySQL
- Docker
- Docker Compose

## Contenedores
- Backend: API REST
- Base de datos: MySQL

## Ejecución
```bash
docker-compose up --build
```

## Pruebas
GET:
http://localhost:5000/productos

POST:
http://localhost:5000/productos
Body:
{
  "nombre": "Ejemplo",
  "precio": 100
}
