*Panel de Administración
*Descripción

Este proyecto es una aplicación web de panel de administración desarrollada con Flask, un framework de Python para aplicaciones web. 
Está diseñado para gestionar usuarios administradores, productos y publicaciones de blog de manera eficiente. La aplicación permite 
a los administradores autenticarse, crear, editar, eliminar y visualizar productos y posts, además de proporcionar una interfaz 
pública para mostrar el contenido. Utiliza una base de datos SQLite para el almacenamiento de datos y sigue un patrón de arquitectura 
MVC (Modelo-Vista-Controlador) para una organización clara del código.

El proyecto incluye funcionalidades de autenticación segura (login, registro y restablecimiento de contraseña), gestión de productos 
(con campos como nombre, precio, descripción y categoría), gestión de posts de blog (título, contenido y fecha), y una sección pública 
para mostrar el contenido al público general. Está configurado para entornos de desarrollo, pruebas y producción, con migraciones de 
base de datos para facilitar el mantenimiento.

*Características

-Autenticación de Administradores: Sistema de login, registro y restablecimiento de contraseña con Flask-Login y hashing de contraseñas.
-Gestión de Productos: CRUD completo (Crear, Leer, Actualizar, Eliminar) para productos, incluyendo validación de formularios con 
Flask-WTF.
-Gestión de Posts de Blog: CRUD para publicaciones, con soporte para contenido de texto largo y fechas automáticas.
-Interfaz de Dashboard: Panel principal para administradores con navegación a secciones clave.
-Sección Pública: Página de inicio que muestra productos y posts disponibles para usuarios no autenticados.
-Protección CSRF: Implementada para prevenir ataques de cross-site request forgery.
-Migraciones de Base de Datos: Uso de Flask-Migrate para gestionar cambios en el esquema de la base de datos.
-Plantillas HTML: Estructura modular con Jinja2, incluyendo layouts base y parciales para reutilización.
-Activos Estáticos: CSS, JavaScript e imágenes organizados para estilos y funcionalidades interactivas.
-Configuración Multi-Entorno: Soporte para desarrollo, pruebas y producción con diferentes configuraciones de base de datos.

*Tecnologías Utilizadas

*Backend:

-Python 3.11
-Flask 3.1.1 (framework web)
-Flask-SQLAlchemy 3.1.1 (ORM para base de datos)
-Flask-Login 0.6.3 (gestión de sesiones de usuario)
-Flask-Migrate 4.1.0 (migraciones de base de datos)
-Flask-WTF 1.2.2 (formularios y validación)
-Werkzeug (seguridad, hashing de contraseñas)
-Alembic (herramienta de migraciones)

*Base de Datos:

-SQLite (para desarrollo y producción por defecto; configurable para otros motores)

*Frontend:

-HTML5 con Jinja2 (plantillas)
-CSS3 (estilos personalizados)
-JavaScript (funcionalidades interactivas)
-Bootstrap o frameworks similares (si se usan en los estilos)

*Herramientas de Desarrollo:

-Virtualenv (entorno virtual)
-Git (control de versiones)

*Prerrequisitos

-Python 3.11 o superior instalado en tu sistema.
-Git para clonar el repositorio.

*Uso

-Acceso Inicial:

Visita http://127.0.0.1:5000/ para la página pública.
Regístrate como administrador en /register o inicia sesión en /login.

-Dashboard:

Después de iniciar sesión, accede al dashboard en dashboard para gestionar productos y posts.
Gestión de Productos:

Agregar: /products/add
Ver/Editar/Eliminar: products (lista) y /products/<id>/edit
Gestión de Posts:

Agregar: /posts/add
Ver/Editar/Eliminar: posts (lista) y /posts/<id>/edit
Restablecimiento de Contraseña:

Usa /reset_password para enviar un enlace de restablecimiento (requiere configuración de email).
