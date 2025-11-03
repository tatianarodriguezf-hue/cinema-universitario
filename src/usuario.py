class Usuario:
    """Clase para gestionar usuarios del cinema universitario"""
    
    def __init__(self, nombre, apellido, documento, tipo_vinculo):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.tipo_vinculo = tipo_vinculo
        self.reservas = []
    
    @staticmethod
    def validar_nombre(nombre):
        """Valida que el nombre tenga al menos 3 letras y no contenga números"""
        if len(nombre) < 3:
            return False, "El nombre debe tener al menos 3 letras"
        if any(char.isdigit() for char in nombre):
            return False, "El nombre no puede contener números"
        if not nombre.replace(" ", "").isalpha():
            return False, "El nombre solo puede contener letras"
        return True, ""
    
    @staticmethod
    def validar_apellido(apellido):
        """Valida que el apellido tenga al menos 3 letras y no contenga números"""
        if len(apellido) < 3:
            return False, "El apellido debe tener al menos 3 letras"
        if any(char.isdigit() for char in apellido):
            return False, "El apellido no puede contener números"
        if not apellido.replace(" ", "").isalpha():
            return False, "El apellido solo puede contener letras"
        return True, ""
    
    @staticmethod
    def validar_documento(documento):
        """Valida que el documento tenga entre 3 y 15 dígitos"""
        if not documento.isdigit():
            return False, "El documento solo puede contener números"
        if len(documento) < 3 or len(documento) > 15:
            return False, "El documento debe tener entre 3 y 15 dígitos"
        return True, ""
    
    @staticmethod
    def validar_tipo_vinculo(tipo_vinculo):
        """Valida que el tipo de vínculo sea válido"""
        tipos_validos = {
            "1": "Estudiantes",
            "2": "Docentes", 
            "3": "Administrativos",
            "4": "Oficiales internos",
            "5": "Publico externo"
        }
        if tipo_vinculo not in tipos_validos:
            return False, "Tipo de vínculo inválido"
        return True, tipos_validos[tipo_vinculo]
    
    @staticmethod
    def obtener_precio_por_tipo(tipo_vinculo):
        """Retorna el precio del tiquete según el tipo de vínculo"""
        precios = {
            "Estudiantes": 8000,
            "Docentes": 10000,
            "Administrativos": 10000,
            "Oficiales internos": 8000,
            "Publico externo": 15000
        }
        return precios.get(tipo_vinculo, 15000)
    
    def agregar_reserva(self, reserva):
        """Agrega una reserva al usuario"""
        self.reservas.append(reserva)
    
    def obtener_reservas_activas(self):
        """Retorna las reservas activas del usuario"""
        return [reserva for reserva in self.reservas if reserva.activa]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento} ({self.tipo_vinculo})"
