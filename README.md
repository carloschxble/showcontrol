# ShowControl

**Sistema administrativo para showroom de emprendedores.**

Este proyecto es una aplicación web construida con **Python, Django y PostgreSQL**, diseñada para llevar el control de los cortes de ventas quincenales y los pagos correspondientes a cada emprendedor que renta un espacio en el showroom. Además, permite registrar los pagos de renta mensuales de forma clara y ordenada.

---

## 🧾 Funcionalidades

- Registro de cortes de ventas diarios asignados a cada emprendedor.
- Cálculo automático del total a pagar en cada corte quincenal.
- Control de pagos mensuales de renta por parte de cada emprendedor.
- Filtros por fecha, rango de corte y tipo de operación (ventas o renta).
- Autenticación mediante login.
- Panel administrativo para gestionar la información de forma sencilla.

---

## ⚙️ Tecnologías utilizadas

- [Python 3.x](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- HTML5, CSS3 y JavaScript

---

## 🐳 Entorno de desarrollo con Docker

> Se incluye configuración con Docker para facilitar la ejecución local y futura implementación en producción.

```bash
# Levantar el entorno de desarrollo
docker-compose up --build

