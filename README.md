# 🎬 Cinema Universitario UdeA

Sistema de gestión para el Cinema Universitario de la Universidad de Antioquia, desarrollado en Python con interfaz de consola.

## 👥 Integrante del Proyecto

- **Tatiana Rodriguez Fajardo** - Desarrolladora Principal

## 🎓 Vínculos Académicos y Descripción

### Tatiana Rodriguez Fajardo
- **Programa:** Ingeniería Industrial - Universidad de Antioquia
- **Correo:** tatiana.rodriguezf@udea.edu.co
- **Habilidades:** Programación en Python, análisis de sistemas, desarrollo de software, algoritmos y estructuras de datos
- **Fortalezas:** Resolución de problemas complejos, programación orientada a objetos, diseño de interfaces de usuario, documentación técnica

## 📽️ Nombre del Proyecto y Detalles

**Cinema UdeA** es un sistema integral de gestión cinematográfica diseñado específicamente para la comunidad universitaria. El sistema permite la administración completa de usuarios, reservas, facturación y reportes para un cinema con capacidad de 121 asientos.

![Cinema UdeA Logo](https://via.placeholder.com/400x200/2E8B57/FFFFFF?text=Cinema+UdeA)

### Características Principales:
- 🎫 Gestión de reservas en tiempo real
- 👤 Sistema de usuarios con diferentes tipos de vinculación
- 💺 Selección visual de asientos (11x11 = 121 asientos)
- 💰 Sistema de facturación diferenciado por tipo de usuario
- 📊 Panel administrativo con reportes detallados
- 📁 Exportación de datos a formato CSV

## 📄 Licencia del Software

Este proyecto está licenciado bajo la **Licencia MIT**.

```
MIT License

Copyright (c) 2025 Tatiana Rodriguez Fajardo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🚀 Instalación y Uso

### Requisitos del Sistema
- Python 3.7 o superior
- Sistema operativo: Windows, macOS, o Linux
- Terminal/Consola de comandos

### Instalación
1. Clone o descargue el repositorio
2. Navegue hasta la carpeta del proyecto
3. Ejecute el programa principal:

```bash
cd src
python main.py
```

### Estructura del Proyecto
```
ProyectoIntegrador/
├── src/                           # Código fuente
│   ├── main.py                   # Archivo principal
│   ├── usuario.py                # Gestión de usuarios
│   ├── pelicula.py               # Gestión de películas
│   ├── reserva.py                # Gestión de reservas
│   ├── cinema.py                 # Lógica del cinema
│   └── gestor_usuarios.py        # Administración de usuarios
├── doc/                          # Documentación
│   ├── manual_usuario.md         # Manual de usuario
│   ├── especificaciones_tecnicas.md # Documentación técnica
│   ├── acta_entendimiento.md     # Acta de entendimiento
│   ├── acta_colaboracion.md      # Acta de colaboración
│   └── acta_responsabilidad.md   # Acta de responsabilidad
├── README.md                     # Este archivo
├── requirements.txt              # Requisitos del sistema
└── Trabajo.md                   # Especificaciones del proyecto
```

## 🎯 Funcionalidades

### Para Usuarios
- **Registro de Usuario:** Validación completa de datos personales
- **Reserva de Asientos:** Selección visual e intuitiva
- **Consulta de Cartelera:** Horarios y disponibilidad del fin de semana
- **Cancelación de Reservas:** Gestión flexible de reservas
- **Facturación:** Generación automática de facturas

### Para Administradores
- **Reportes Completos:** Estadísticas detalladas del sistema
- **Gestión de Usuarios:** Lista completa de usuarios registrados
- **Exportación de Datos:** Archivos CSV para análisis externo
- **Monitoreo de Ingresos:** Seguimiento financiero en tiempo real

### Tipos de Usuario y Precios
| Tipo de Usuario | Precio del Tiquete |
|----------------|-------------------|
| Estudiantes | $8,000 |
| Docentes | $10,000 |
| Administrativos | $10,000 |
| Oficiales Internos | $8,000 |
| Público Externo | $15,000 |

## 🔐 Credenciales de Administrador

Para acceder al panel administrativo, use una de las siguientes credenciales:

| Usuario | Contraseña |
|---------|------------|
| admin | 123456 |
| cinema | udea2025 |
| profesor | algoritmia |

## 📊 Reportes y Exportación

El sistema genera automáticamente:
- **usuarios.csv:** Lista completa de usuarios registrados
- **reservas.csv:** Todas las reservas activas del sistema
- **factura_[ID].csv:** Facturas individuales por reserva

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Paradigma:** Programación Orientada a Objetos
- **Librerías:** 
  - `csv` (exportación de datos)
  - `datetime` (manejo de fechas)
  - `uuid` (generación de IDs únicos)
  - `os` (operaciones del sistema)

## 📈 Versiones del Software

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| v1.0.0 | 2025-11-02 | Versión inicial completa |
| v0.9.0 | 2025-10-30 | Sistema de reservas implementado |
| v0.8.0 | 2025-10-25 | Gestión de usuarios completada |
| v0.7.0 | 2025-10-20 | Estructura base del proyecto |

## 📋 Entregables Formales

### Actas de Proyecto
Según las especificaciones del curso, se han creado las siguientes actas formales:

- **[Acta de Entendimiento](doc/acta_entendimiento.md):** Objetivos, expectativas y compromisos del proyecto
- **[Acta de Colaboración](doc/acta_colaboracion.md):** Metodologías de trabajo y estándares de calidad
- **[Acta de Responsabilidad](doc/acta_responsabilidad.md):** Distribución de tareas, cronograma y compromisos específicos

### Documentación Técnica
- **[Manual de Usuario](doc/manual_usuario.md):** Guía completa para el uso del sistema
- **[Especificaciones Técnicas](doc/especificaciones_tecnicas.md):** Reporte de visión, requisitos y plan de proyecto

## 🤝 Contribuciones

Este proyecto es parte del curso de Algoritmia y Programación de la Universidad de Antioquia, desarrollado individualmente por Tatiana Rodriguez Fajardo.

## 📞 Soporte

Para soporte técnico o consultas sobre el proyecto, contacte a:
- **Desarrolladora:** Tatiana Rodriguez Fajardo
- **Correo:** tatiana.rodriguezf@udea.edu.co
- **Curso:** Algoritmia y Programación 2025-2
- **Universidad:** Universidad de Antioquia

---

**Desarrollado con ❤️ por Tatiana Rodriguez Fajardo**
