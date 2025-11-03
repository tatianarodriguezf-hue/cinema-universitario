# 📋 Especificaciones Técnicas - Cinema Universitario UdeA

## Reporte de Visión

### Descripción General
Cinema Universitario UdeA es un sistema de gestión cinematográfica desarrollado específicamente para la comunidad universitaria de la Universidad de Antioquia. El software proporciona una solución integral para la administración de reservas, usuarios, facturación y reportes de un cinema con capacidad de 121 asientos.

### Objetivos del Software
- **Objetivo Principal:** Facilitar la gestión completa del Cinema Universitario mediante un sistema automatizado y eficiente
- **Objetivos Específicos:**
  - Automatizar el proceso de registro de usuarios y validación de datos
  - Proporcionar un sistema visual e intuitivo para la selección de asientos
  - Generar facturación automática diferenciada por tipo de usuario
  - Ofrecer herramientas administrativas para el monitoreo y control del sistema
  - Exportar datos en formato CSV para análisis externos

### Beneficios
- **Para Usuarios:** Proceso de reserva rápido y visual, facturación transparente
- **Para Administradores:** Reportes detallados, control total del sistema, exportación de datos
- **Para la Universidad:** Gestión eficiente de recursos, seguimiento de ingresos, servicio mejorado

## Especificación de Requisitos

### Requisitos Funcionales

#### RF001 - Registro de Usuarios
- **Descripción:** El sistema debe permitir el registro de nuevos usuarios con validación completa de datos
- **Entradas:** Nombre, apellido, documento, tipo de vínculo
- **Validaciones:**
  - Nombre y apellido: mínimo 3 caracteres, solo letras
  - Documento: 3-15 dígitos, solo números, único en el sistema
  - Tipo de vínculo: debe ser una opción válida (1-5)
- **Salidas:** Confirmación de registro exitoso o lista de errores

#### RF002 - Gestión de Reservas
- **Descripción:** El sistema debe permitir crear, consultar y cancelar reservas de asientos
- **Funcionalidades:**
  - Crear reserva: selección visual de asiento, validación de disponibilidad
  - Consultar reservas: mostrar reservas activas del usuario
  - Cancelar reserva: liberar asiento y actualizar estado
- **Restricciones:** Solo usuarios registrados pueden hacer reservas

#### RF003 - Selección Visual de Asientos
- **Descripción:** Interfaz visual para mostrar disponibilidad de asientos en formato 11x11
- **Representación:** 
  - "O" = Asiento disponible
  - "X" = Asiento ocupado
- **Formato de entrada:** Combinación letra-número (A1, B5, etc.)

#### RF004 - Sistema de Facturación
- **Descripción:** Generación automática de facturas con precios diferenciados
- **Precios por tipo de usuario:**
  - Estudiantes: $8,000
  - Docentes: $10,000
  - Administrativos: $10,000
  - Oficiales internos: $8,000
  - Público externo: $15,000
- **Información incluida:** ID reserva, datos del usuario, película, asiento, precio, fecha

#### RF005 - Consulta de Cartelera
- **Descripción:** Mostrar películas disponibles para el fin de semana
- **Información mostrada:** Nombre, día, hora, duración, asientos disponibles
- **Organización:** Agrupado por día (Sábado/Domingo)

#### RF006 - Panel Administrativo
- **Descripción:** Acceso restringido para administradores del sistema
- **Funcionalidades:**
  - Autenticación con usuario y contraseña
  - Reportes estadísticos completos
  - Lista de usuarios registrados
  - Exportación de datos a CSV

#### RF007 - Exportación de Datos
- **Descripción:** Generar archivos CSV con información del sistema
- **Tipos de exportación:**
  - Usuarios: datos personales y número de reservas
  - Reservas: información completa de reservas activas
  - Facturas individuales: datos específicos por reserva

### Requisitos No Funcionales

#### RNF001 - Usabilidad
- **Interfaz intuitiva:** Menús claros y navegación simple
- **Mensajes informativos:** Errores y confirmaciones descriptivas
- **Formato visual:** Representación clara del mapa de asientos

#### RNF002 - Rendimiento
- **Tiempo de respuesta:** Operaciones básicas en menos de 2 segundos
- **Capacidad:** Soporte para hasta 1000 usuarios registrados
- **Eficiencia:** Uso mínimo de memoria del sistema

#### RNF003 - Fiabilidad
- **Validación de datos:** Verificación exhaustiva en todas las entradas
- **Manejo de errores:** Recuperación elegante de errores sin pérdida de datos
- **Consistencia:** Estado coherente del sistema en todo momento

#### RNF004 - Seguridad
- **Autenticación:** Credenciales seguras para acceso administrativo
- **Validación:** Prevención de inyección de datos maliciosos
- **Privacidad:** Protección de datos personales de usuarios

#### RNF005 - Mantenibilidad
- **Código modular:** Separación clara de responsabilidades por clases
- **Documentación:** Comentarios y documentación técnica completa
- **Extensibilidad:** Facilidad para agregar nuevas funcionalidades

#### RNF006 - Portabilidad
- **Multiplataforma:** Compatible con Windows, macOS y Linux
- **Dependencias mínimas:** Solo librerías estándar de Python
- **Instalación simple:** Ejecución directa sin configuración compleja

#### RNF007 - Compatibilidad
- **Python:** Versión 3.7 o superior
- **Formato de datos:** CSV estándar para exportación
- **Codificación:** UTF-8 para soporte de caracteres especiales

## Plan de Proyecto

### Cronograma de Desarrollo

#### Fase 1: Análisis y Diseño (Semanas 1-2)
- Análisis de requisitos
- Diseño de arquitectura del sistema
- Definición de clases y métodos
- Creación de diagramas UML

#### Fase 2: Desarrollo Core (Semanas 3-6)
- Implementación de clases base (Usuario, Película, Reserva)
- Sistema de validaciones
- Lógica de negocio principal
- Pruebas unitarias básicas

#### Fase 3: Interfaz y Funcionalidades (Semanas 7-10)
- Desarrollo de interfaz de consola
- Sistema de menús y navegación
- Implementación de funcionalidades avanzadas
- Integración de módulos

#### Fase 4: Administración y Reportes (Semanas 11-13)
- Panel administrativo
- Sistema de reportes
- Exportación de datos CSV
- Pruebas de integración

#### Fase 5: Testing y Documentación (Semanas 14-15)
- Pruebas exhaustivas del sistema
- Corrección de errores
- Documentación técnica y manual de usuario
- Preparación para entrega

#### Fase 6: Entrega y Sustentación (Semana 16)
- Entrega final del proyecto
- Sustentación ante el profesor
- Demostración del sistema funcionando

### Presupuesto del Proyecto

#### Recursos Humanos
- **Desarrolladora:** Tatiana Rodriguez Fajardo
- **Tiempo total estimado:** 50 horas de desarrollo
- **Total horas proyecto:** 50 horas
- **Valor hora práctica profesional:** $15,000 (basado en 1 SMLV)
- **Costo total del proyecto:** $750,000

#### Recursos Técnicos
- **Hardware:** Computador personal de la estudiante
- **Software:** Python (gratuito), editores de código (gratuitos)
- **Herramientas:** Git/GitHub (gratuito)
- **Costo adicional:** $0

#### Presupuesto Total: $750,000

## Plan de Versionado

### Estrategia de Versionado
El proyecto utiliza versionado semántico (SemVer): MAJOR.MINOR.PATCH

### Historial de Versiones

| Versión | Fecha | Descripción | Cambios Principales |
|---------|-------|-------------|-------------------|
| v0.1.0 | 2025-10-15 | Inicio del proyecto | Estructura inicial, clases base |
| v0.2.0 | 2025-10-20 | Sistema de usuarios | Registro y validación de usuarios |
| v0.3.0 | 2025-10-25 | Gestión de películas | Cartelera y gestión de funciones |
| v0.4.0 | 2025-10-30 | Sistema de reservas | Reserva y cancelación de asientos |
| v0.5.0 | 2025-11-01 | Interfaz de consola | Menús y navegación completa |
| v0.6.0 | 2025-11-02 | Panel administrativo | Reportes y gestión administrativa |
| v0.7.0 | 2025-11-02 | Exportación CSV | Sistema de exportación de datos |
| v0.8.0 | 2025-11-02 | Testing y debugging | Corrección de errores y optimización |
| v0.9.0 | 2025-11-02 | Documentación | Manual de usuario y documentación técnica |
| **v1.0.0** | **2025-11-02** | **Versión final** | **Sistema completo y funcional** |

### Próximas Versiones (Futuras Mejoras)
- v1.1.0: Interfaz gráfica con tkinter
- v1.2.0: Base de datos SQLite
- v1.3.0: Sistema de notificaciones
- v2.0.0: Aplicación web con Flask

## Arquitectura del Sistema

### Patrón de Diseño
El sistema utiliza el patrón **Modelo-Vista-Controlador (MVC)** adaptado:
- **Modelo:** Clases de datos (Usuario, Película, Reserva)
- **Vista:** Interfaz de consola (main.py)
- **Controlador:** Gestores (GestorUsuarios, GestorReservas, etc.)

### Diagrama de Clases Principal

```
CinemaUdeA
├── GestorUsuarios
├── GestorPeliculas
├── GestorReservas
├── Cinema
└── Administrador

Usuario
├── nombre: str
├── apellido: str
├── documento: str
├── tipo_vinculo: str
└── reservas: List[Reserva]

Pelicula
├── nombre: str
├── dia: str
├── hora: str
├── duracion: str
└── asientos_ocupados: Set[int]

Reserva
├── id: str
├── usuario: Usuario
├── pelicula: Pelicula
├── numero_asiento: int
├── fecha_reserva: datetime
├── activa: bool
└── precio: int
```

### Flujo de Datos
1. **Entrada:** Usuario interactúa con menús de consola
2. **Procesamiento:** Gestores validan y procesan datos
3. **Almacenamiento:** Datos se mantienen en memoria durante ejecución
4. **Salida:** Resultados mostrados en consola o exportados a CSV

---

**Documento técnico desarrollado por Tatiana Rodriguez Fajardo**  
**Universidad de Antioquia - Algoritmia y Programación 2025-2**
