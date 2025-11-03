from datetime import datetime

class Pelicula:
    """Clase para gestionar películas del cinema"""
    
    def __init__(self, nombre, dia, hora, duracion):
        self.nombre = nombre
        self.dia = dia
        self.hora = hora
        self.duracion = duracion
        self.asientos_ocupados = set()  # Conjunto de asientos ocupados
    
    def obtener_asientos_disponibles(self):
        """Retorna el número de asientos disponibles"""
        return 121 - len(self.asientos_ocupados)
    
    def reservar_asiento(self, numero_asiento):
        """Reserva un asiento específico"""
        if numero_asiento in self.asientos_ocupados:
            return False, "El asiento ya está ocupado"
        if numero_asiento < 1 or numero_asiento > 121:
            return False, "Número de asiento inválido"
        
        self.asientos_ocupados.add(numero_asiento)
        return True, "Asiento reservado exitosamente"
    
    def liberar_asiento(self, numero_asiento):
        """Libera un asiento específico"""
        if numero_asiento in self.asientos_ocupados:
            self.asientos_ocupados.remove(numero_asiento)
            return True, "Asiento liberado exitosamente"
        return False, "El asiento no estaba ocupado"
    
    def esta_asiento_ocupado(self, numero_asiento):
        """Verifica si un asiento está ocupado"""
        return numero_asiento in self.asientos_ocupados
    
    def __str__(self):
        return f"{self.nombre} - {self.dia} {self.hora} ({self.obtener_asientos_disponibles()} asientos disponibles)"


class GestorPeliculas:
    """Clase para gestionar el catálogo de películas"""
    
    def __init__(self):
        self.peliculas = []
        self._cargar_peliculas_ejemplo()
    
    def _cargar_peliculas_ejemplo(self):
        """Carga películas de ejemplo para el fin de semana"""
        peliculas_ejemplo = [
            ("Avatar: El Camino del Agua", "Sábado", "14:00", "192 min"),
            ("Top Gun: Maverick", "Sábado", "17:00", "131 min"),
            ("Black Panther: Wakanda Forever", "Sábado", "20:00", "161 min"),
            ("Spider-Man: No Way Home", "Domingo", "14:00", "148 min"),
            ("Doctor Strange 2", "Domingo", "17:00", "126 min"),
            ("Thor: Love and Thunder", "Domingo", "20:00", "119 min")
        ]
        
        for nombre, dia, hora, duracion in peliculas_ejemplo:
            self.peliculas.append(Pelicula(nombre, dia, hora, duracion))
    
    def obtener_peliculas(self):
        """Retorna la lista de películas"""
        return self.peliculas
    
    def obtener_pelicula_por_indice(self, indice):
        """Retorna una película por su índice"""
        if 0 <= indice < len(self.peliculas):
            return self.peliculas[indice]
        return None
    
    def mostrar_cartelera(self):
        """Muestra la cartelera del fin de semana"""
        print("\n" + "="*60)
        print("           CARTELERA DEL FIN DE SEMANA")
        print("="*60)
        
        for i, pelicula in enumerate(self.peliculas, 1):
            print(f"{i}. {pelicula}")
        
        print("="*60)
