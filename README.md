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
- HTML5, CSS3 y JavaScript

---

## 🧪 Instalación local (sin Docker)

### 1. Clona el repositorio

```zsh
    git clone https://github.com/carloschxble/showcontrol.git
    cd showcontrol
```
### 2. Crea y activa un entorno virtual

```zsh
    python3 -m venv env # "python3" en Mac/Linux, "python" en Windows
    source env/bin/activate  # En Mac/Linux
```

### 3. Instala dependencias

```zsh
    pip3 install -r requirements.txt # "pip3" en Mac/Linux, "pip" en Windows
```

### 4. Configura la base de datos PostgreSQL

```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '*****',
        'USER': '*****',
        'PASSWORD': '*****',
        'HOST': 'localhost',
        'PORT': '5432',
        }
    }

    # Pedir las credenciales de la db al administrador
```

### 5. Aplica las migraciones

```zsh
    python3 manage.py makemigrations
    python3 manage.py migrate
```

### 6. Crea un superusuario (opcional)

```zsh
    python3 manage.py createsuperuser
```

### 7. Corre el servidor

```zsh
    python3 manage.py runserver
```
    Accede a la app en: http://127.0.0.1:8000/
    Panel admin: http://127.0.0.1:8000/admin/

---

## 📂 Estructura básica del proyecto
showcontrol/
├── core/                  # App principal
│   ├── models.py          # Modelos: Emprendedor, Venta, etc.
│   ├── views.py
│   └── ...
├── showcontrol/           # Configuración general del proyecto
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md

---

## 🐘 Comandos útiles con PostgreSQL

### 1. Entrar al cliente psql

```zsh
    psql -U nombre_de_usuario -d nombre_de_la_base_de_datos
```
### 2. Ver las tablas

```zsh
    \dt
```

### 3. Salir del cliente

```zsh
    \q
```

## 🐳 Entorno de desarrollo con Docker (próximamente)

🚧 Esta sección está en construcción. A futuro se incluirá configuración con Docker para facilitar la ejecución local y la implementación en producción.

## 🔜 Próximamente

- Integración de Docker
- Interfaz de usuario para reportes y consultas
- Tests automatizados
- Panel personalizado para emprendedores

## 📄 Licencia
Este proyecto se encuentra en desarrollo. La licencia será definida una vez se concluya la versión estable.
