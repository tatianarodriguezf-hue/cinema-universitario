class Cinema:
    """Clase principal para gestionar el cinema universitario"""
    
    def __init__(self):
        self.filas = 11  # 11 filas
        self.asientos_por_fila = 11  # 11 asientos por fila = 121 total
        self.total_asientos = 121
    
    def mostrar_asientos(self, pelicula):
        """Muestra el mapa visual de asientos para una película"""
        print(f"\n{'='*60}")
        print(f"           SELECCIÓN DE ASIENTOS")
        print(f"           {pelicula.nombre}")
        print(f"{'='*60}")
        print("                    PANTALLA")
        print("    " + "-" * 40)
        print()
        
        # Mostrar numeración de columnas
        print("     ", end="")
        for col in range(1, 12):
            print(f"{col:2}", end=" ")
        print()
        print()
        
        # Mostrar filas con asientos
        numero_asiento = 1
        for fila in range(1, 12):
            print(f"  {chr(64 + fila)} ", end="")  # A, B, C, etc.
            
            for col in range(1, 12):
                if pelicula.esta_asiento_ocupado(numero_asiento):
                    print(" X", end=" ")  # Ocupado
                else:
                    print(" O", end=" ")  # Disponible
                numero_asiento += 1
            print()
        
        print()
        print("  Leyenda: O = Disponible, X = Ocupado")
        print(f"  Asientos disponibles: {pelicula.obtener_asientos_disponibles()}")
        print("="*60)
    
    def convertir_posicion_a_numero(self, fila_letra, columna):
        """Convierte posición (A1, B5, etc.) a número de asiento"""
        try:
            fila_num = ord(fila_letra.upper()) - ord('A') + 1
            if fila_num < 1 or fila_num > 11:
                return None
            if columna < 1 or columna > 11:
                return None
            
            numero_asiento = (fila_num - 1) * 11 + columna
            return numero_asiento
        except:
            return None
    
    def convertir_numero_a_posicion(self, numero_asiento):
        """Convierte número de asiento a posición (A1, B5, etc.)"""
        if numero_asiento < 1 or numero_asiento > 121:
            return None
        
        fila = (numero_asiento - 1) // 11 + 1
        columna = (numero_asiento - 1) % 11 + 1
        fila_letra = chr(ord('A') + fila - 1)
        
        return f"{fila_letra}{columna}"
    
    def validar_seleccion_asiento(self, entrada):
        """Valida la entrada del usuario para selección de asiento"""
        try:
            # Formato esperado: A1, B5, etc.
            if len(entrada) < 2:
                return None, "Formato inválido. Use formato como A1, B5, etc."
            
            fila_letra = entrada[0]
            columna_str = entrada[1:]
            
            if not fila_letra.isalpha():
                return None, "La fila debe ser una letra (A-K)"
            
            if not columna_str.isdigit():
                return None, "La columna debe ser un número (1-11)"
            
            columna = int(columna_str)
            numero_asiento = self.convertir_posicion_a_numero(fila_letra, columna)
            
            if numero_asiento is None:
                return None, "Posición inválida. Use filas A-K y columnas 1-11"
            
            return numero_asiento, ""
            
        except Exception as e:
            return None, "Formato inválido. Use formato como A1, B5, etc."


class Administrador:
    """Clase para gestionar funciones administrativas"""
    
    def __init__(self):
        self.usuarios_admin = {
            "admin": "123456",
            "cinema": "udea2025",
            "profesor": "algoritmia"
        }
    
    def validar_credenciales(self, usuario, contraseña):
        """Valida las credenciales de administrador"""
        return self.usuarios_admin.get(usuario) == contraseña
    
    def generar_reporte_completo(self, gestor_usuarios, gestor_reservas):
        """Genera un reporte completo del sistema"""
        estadisticas = gestor_reservas.obtener_estadisticas()
        usuarios = gestor_usuarios.obtener_todos_usuarios()
        
        # Calcular usuario con más y menos reservas
        usuario_mas_reservas = None
        usuario_menos_reservas = None
        max_reservas = 0
        min_reservas = float('inf')
        
        for usuario in usuarios:
            num_reservas = len(usuario.obtener_reservas_activas())
            if num_reservas > max_reservas:
                max_reservas = num_reservas
                usuario_mas_reservas = usuario
            if num_reservas < min_reservas and num_reservas > 0:
                min_reservas = num_reservas
                usuario_menos_reservas = usuario
        
        reporte = f"""
{'='*60}
                REPORTE ADMINISTRATIVO
                  CINEMA UNIVERSITARIO
{'='*60}

ESTADÍSTICAS GENERALES:
- Total de reservas registradas: {estadisticas['total_reservas']}
- Total de tiquetes vendidos: {estadisticas['tiquetes_vendidos']}
- Reservas activas: {estadisticas['reservas_activas']}
- Total de ingresos: ${estadisticas['total_ingresos']:,}
- Promedio por venta: ${estadisticas['promedio_venta']:,.2f}

USUARIOS REGISTRADOS: {len(usuarios)}

USUARIOS DESTACADOS:
- Mayor cantidad de reservas: {usuario_mas_reservas.nombre if usuario_mas_reservas else 'N/A'} ({max_reservas} reservas)
- Menor cantidad de reservas: {usuario_menos_reservas.nombre if usuario_menos_reservas else 'N/A'} ({min_reservas if min_reservas != float('inf') else 0} reservas)

{'='*60}
        """
        
        return reporte
