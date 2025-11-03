# 📖 Manual de Usuario - Cinema Universitario UdeA

## Índice
1. [Introducción](#introducción)
2. [Inicio del Sistema](#inicio-del-sistema)
3. [Registro de Usuario](#registro-de-usuario)
4. [Realizar una Reserva](#realizar-una-reserva)
5. [Cancelar una Reserva](#cancelar-una-reserva)
6. [Consultar Cartelera](#consultar-cartelera)
7. [Panel Administrativo](#panel-administrativo)
8. [Solución de Problemas](#solución-de-problemas)

## Introducción

Cinema Universitario UdeA es un sistema de gestión cinematográfica diseñado para la comunidad universitaria. Este manual le guiará paso a paso para utilizar todas las funcionalidades del sistema.

### Características del Cinema
- **Capacidad:** 121 asientos (11 filas x 11 columnas)
- **Distribución:** Filas A-K, Columnas 1-11
- **Horarios:** Funciones de fin de semana
- **Tipos de usuario:** 5 categorías con precios diferenciados

## Inicio del Sistema

### Requisitos Previos
- Python 3.7 o superior instalado
- Acceso a terminal/consola de comandos

### Ejecutar el Programa
1. Abra la terminal/consola
2. Navegue hasta la carpeta `src` del proyecto
3. Ejecute el comando:
   ```bash
   python main.py
   ```

### Menú Principal
Al iniciar, verá el menú principal con las siguientes opciones:

```
              CINEMA UNIVERSITARIO UdeA
============================================================
1. Registrar Usuario
2. Registrar Reserva
3. Cancelar Reserva
4. Consultar Funciones del Fin de Semana
5. Administrador
6. Salir
============================================================
```

## Registro de Usuario

### Paso a Paso
1. Seleccione la opción **1** del menú principal
2. Complete los siguientes datos:

#### Nombre
- **Requisitos:** Mínimo 3 letras, solo caracteres alfabéticos
- **Ejemplo válido:** "Juan Carlos"
- **Ejemplo inválido:** "Jo" (muy corto), "Juan123" (contiene números)

#### Apellido
- **Requisitos:** Mínimo 3 letras, solo caracteres alfabéticos
- **Ejemplo válido:** "García López"
- **Ejemplo inválido:** "Go" (muy corto), "García2" (contiene números)

#### Documento
- **Requisitos:** Entre 3 y 15 dígitos, solo números
- **Ejemplo válido:** "1234567890"
- **Ejemplo inválido:** "12" (muy corto), "123ABC" (contiene letras)

#### Tipo de Vínculo
Seleccione el número correspondiente a su vinculación:

| Opción | Tipo de Usuario | Precio |
|--------|----------------|--------|
| 1 | Estudiantes | $8,000 |
| 2 | Docentes | $10,000 |
| 3 | Administrativos | $10,000 |
| 4 | Oficiales internos | $8,000 |
| 5 | Público externo | $15,000 |

### Mensajes de Error Comunes
- **"El nombre debe tener al menos 3 letras":** Ingrese un nombre más largo
- **"El documento solo puede contener números":** Elimine letras o caracteres especiales
- **"Ya existe un usuario con este documento":** Use un documento diferente

## Realizar una Reserva

### Requisitos Previos
- Debe estar registrado en el sistema
- Conocer su número de documento

### Proceso de Reserva

#### 1. Identificación
- Seleccione la opción **2** del menú principal
- Ingrese su número de documento
- El sistema verificará su registro

#### 2. Selección de Película
- Se mostrará la cartelera disponible
- Ingrese el número de la película deseada

Ejemplo de cartelera:
```
           CARTELERA DEL FIN DE SEMANA
============================================================
1. Avatar: El Camino del Agua - Sábado 14:00 (121 asientos disponibles)
2. Top Gun: Maverick - Sábado 17:00 (121 asientos disponibles)
3. Black Panther: Wakanda Forever - Sábado 20:00 (121 asientos disponibles)
============================================================
```

#### 3. Selección de Asiento
Se mostrará el mapa visual de asientos:

```
           SELECCIÓN DE ASIENTOS
           Avatar: El Camino del Agua
============================================================
                    PANTALLA
    ----------------------------------------

      1  2  3  4  5  6  7  8  9 10 11

  A   O  O  O  O  O  O  O  O  O  O  O
  B   O  O  X  O  O  O  O  O  X  O  O
  C   O  O  O  O  O  O  O  O  O  O  O
  ...

  Leyenda: O = Disponible, X = Ocupado
  Asientos disponibles: 119
============================================================
```

**Formato de selección:** Ingrese la fila (letra) seguida del número de columna
- **Ejemplos válidos:** A1, B5, K11
- **Ejemplos inválidos:** 1A, Z1, A15

#### 4. Confirmación y Factura
- El sistema confirmará la reserva
- Se generará automáticamente una factura
- Opción de exportar la factura a CSV

### Ejemplo de Factura
```
==================================================
              CINEMA UNIVERSITARIO UdeA
                    FACTURA
==================================================
ID Reserva: ABC12345
Fecha: 2025-11-02 21:30:15

Cliente: Juan Carlos García López
Documento: 1234567890
Tipo: Estudiantes

Película: Avatar: El Camino del Agua
Día: Sábado
Hora: 14:00
Asiento: A5

Precio: $8,000
Estado: ACTIVA
==================================================
```

## Cancelar una Reserva

### Proceso de Cancelación

#### 1. Identificación
- Seleccione la opción **3** del menú principal
- Ingrese su número de documento

#### 2. Selección de Reserva
- El sistema mostrará sus reservas activas
- Seleccione el número de la reserva a cancelar

Ejemplo:
```
           CANCELAR RESERVA
==================================================
👤 Juan Carlos García López

Sus reservas activas:
1. Avatar: El Camino del Agua - Asiento A5 (ID: ABC12345)
2. Top Gun: Maverick - Asiento B3 (ID: DEF67890)

Seleccione la reserva a cancelar (número):
```

#### 3. Confirmación
- El sistema confirmará la cancelación
- El asiento quedará disponible nuevamente

### Casos Especiales
- **Sin reservas activas:** El sistema ofrecerá realizar una nueva reserva
- **Usuario no encontrado:** Verificar el número de documento ingresado

## Consultar Cartelera

### Funciones del Fin de Semana
- Seleccione la opción **4** del menú principal
- Se mostrará la programación completa organizada por día

Ejemplo de visualización:
```
         FUNCIONES DEL FIN DE SEMANA
============================================================

🗓️  SÁBADO:
   14:00 - Avatar: El Camino del Agua
            Duración: 192 min
            Asientos disponibles: 119

   17:00 - Top Gun: Maverick
            Duración: 131 min
            Asientos disponibles: 121

🗓️  DOMINGO:
   14:00 - Spider-Man: No Way Home
            Duración: 148 min
            Asientos disponibles: 121
============================================================
```

## Panel Administrativo

### Acceso al Panel
- Seleccione la opción **5** del menú principal
- Ingrese credenciales de administrador:

| Usuario | Contraseña |
|---------|------------|
| admin | 123456 |
| cinema | udea2025 |
| profesor | algoritmia |

### Funciones Administrativas

#### 1. Ver Reporte Completo
Muestra estadísticas detalladas:
- Total de reservas registradas
- Total de tiquetes vendidos
- Total de ingresos
- Promedio por venta
- Usuario con mayor/menor cantidad de reservas

#### 2. Lista de Usuarios
Tabla completa de usuarios registrados con:
- Documento de identidad
- Nombre completo
- Tipo de vinculación
- Número de reservas activas

#### 3. Exportar Datos a CSV
Opciones de exportación:
- **Usuarios:** Archivo `usuarios.csv`
- **Reservas:** Archivo `reservas.csv`
- **Ambos:** Genera ambos archivos

### Ejemplo de Reporte Administrativo
```
                REPORTE ADMINISTRATIVO
                  CINEMA UNIVERSITARIO
============================================================

ESTADÍSTICAS GENERALES:
- Total de reservas registradas: 25
- Total de tiquetes vendidos: 23
- Reservas activas: 23
- Total de ingresos: $215,000
- Promedio por venta: $9,347.83

USUARIOS REGISTRADOS: 18

USUARIOS DESTACADOS:
- Mayor cantidad de reservas: María González (3 reservas)
- Menor cantidad de reservas: Carlos Ruiz (1 reservas)
============================================================
```

## Solución de Problemas

### Errores Comunes y Soluciones

#### Error: "Usuario no encontrado"
**Causa:** Documento no registrado en el sistema
**Solución:** Verificar el número de documento o registrarse primero

#### Error: "El asiento ya está ocupado"
**Causa:** Otro usuario reservó el asiento seleccionado
**Solución:** Seleccionar un asiento diferente (marcado con "O")

#### Error: "Formato inválido de asiento"
**Causa:** Formato incorrecto en la selección de asiento
**Solución:** Usar formato correcto (ej: A1, B5, K11)

#### Error: "Credenciales incorrectas"
**Causa:** Usuario o contraseña de administrador incorrectos
**Solución:** Verificar las credenciales en la tabla de acceso

#### Error: "Opción inválida"
**Causa:** Selección de menú no válida
**Solución:** Ingresar solo los números mostrados en el menú

### Consejos de Uso

#### Para una Mejor Experiencia
1. **Mantenga su documento a mano** al usar el sistema
2. **Revise la cartelera** antes de hacer una reserva
3. **Anote el ID de su reserva** para futuras referencias
4. **Exporte las facturas** como respaldo de sus compras

#### Navegación Eficiente
- Use **Ctrl+C** para cancelar una operación en cualquier momento
- Presione **Enter** para continuar después de leer mensajes
- Los menús siempre regresan al menú principal

### Contacto y Soporte

Para asistencia técnica o consultas:
- **Desarrolladora:** Tatiana Rodriguez Fajardo
- **Correo:** tatiana.rodriguezf@udea.edu.co
- **Curso:** Algoritmia y Programación
- **Universidad:** Universidad de Antioquia

---

**¡Disfrute su experiencia en Cinema Universitario UdeA! 🎬**
