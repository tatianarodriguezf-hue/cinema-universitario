from datetime import datetime
import uuid

class Reserva:
    """Clase para gestionar reservas del cinema"""
    
    def __init__(self, usuario, pelicula, numero_asiento):
        self.id = str(uuid.uuid4())[:8]  # ID único de 8 caracteres
        self.usuario = usuario
        self.pelicula = pelicula
        self.numero_asiento = numero_asiento
        self.fecha_reserva = datetime.now()
        self.activa = True
        self.precio = usuario.obtener_precio_por_tipo(usuario.tipo_vinculo)
    
    def cancelar(self):
        """Cancela la reserva"""
        self.activa = False
        self.pelicula.liberar_asiento(self.numero_asiento)
    
    def generar_factura(self):
        """Genera la factura de la reserva"""
        factura = f"""
{'='*50}
              CINEMA UNIVERSITARIO UdeA
                    FACTURA
{'='*50}
ID Reserva: {self.id}
Fecha: {self.fecha_reserva.strftime('%Y-%m-%d %H:%M:%S')}

Cliente: {self.usuario.nombre} {self.usuario.apellido}
Documento: {self.usuario.documento}
Tipo: {self.usuario.tipo_vinculo}

Película: {self.pelicula.nombre}
Día: {self.pelicula.dia}
Hora: {self.pelicula.hora}
Asiento: {self.numero_asiento}

Precio: ${self.precio:,}
Estado: {'ACTIVA' if self.activa else 'CANCELADA'}
{'='*50}
        """
        return factura
    
    def __str__(self):
        estado = "ACTIVA" if self.activa else "CANCELADA"
        return f"[{self.id}] {self.pelicula.nombre} - Asiento {self.numero_asiento} ({estado})"


class GestorReservas:
    """Clase para gestionar todas las reservas del sistema"""
    
    def __init__(self):
        self.reservas = []
    
    def crear_reserva(self, usuario, pelicula, numero_asiento):
        """Crea una nueva reserva"""
        # Verificar si el asiento está disponible
        exito, mensaje = pelicula.reservar_asiento(numero_asiento)
        if not exito:
            return None, mensaje
        
        # Crear la reserva
        reserva = Reserva(usuario, pelicula, numero_asiento)
        self.reservas.append(reserva)
        usuario.agregar_reserva(reserva)
        
        return reserva, "Reserva creada exitosamente"
    
    def cancelar_reserva(self, reserva_id):
        """Cancela una reserva por su ID"""
        for reserva in self.reservas:
            if reserva.id == reserva_id and reserva.activa:
                reserva.cancelar()
                return True, "Reserva cancelada exitosamente"
        return False, "Reserva no encontrada o ya cancelada"
    
    def obtener_reservas_activas(self):
        """Retorna todas las reservas activas"""
        return [reserva for reserva in self.reservas if reserva.activa]
    
    def obtener_reservas_usuario(self, documento_usuario):
        """Retorna las reservas de un usuario específico"""
        return [reserva for reserva in self.reservas 
                if reserva.usuario.documento == documento_usuario and reserva.activa]
    
    def obtener_estadisticas(self):
        """Retorna estadísticas del sistema de reservas"""
        reservas_activas = self.obtener_reservas_activas()
        total_reservas = len(self.reservas)
        total_activas = len(reservas_activas)
        total_ingresos = sum(reserva.precio for reserva in reservas_activas)
        
        return {
            'total_reservas': total_reservas,
            'reservas_activas': total_activas,
            'tiquetes_vendidos': total_activas,
            'total_ingresos': total_ingresos,
            'promedio_venta': total_ingresos / max(1, total_activas)
        }
