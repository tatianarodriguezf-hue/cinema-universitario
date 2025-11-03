from usuario import Usuario

class GestorUsuarios:
    """Clase para gestionar usuarios del sistema"""
    
    def __init__(self):
        self.usuarios = {}  # Diccionario con documento como clave
    
    def registrar_usuario(self, nombre, apellido, documento, tipo_vinculo):
        """Registra un nuevo usuario en el sistema"""
        errores = []
        
        # Validar nombre
        valido, mensaje = Usuario.validar_nombre(nombre)
        if not valido:
            errores.append(f"Nombre: {mensaje}")
        
        # Validar apellido
        valido, mensaje = Usuario.validar_apellido(apellido)
        if not valido:
            errores.append(f"Apellido: {mensaje}")
        
        # Validar documento
        valido, mensaje = Usuario.validar_documento(documento)
        if not valido:
            errores.append(f"Documento: {mensaje}")
        
        # Verificar si el usuario ya existe
        if documento in self.usuarios:
            errores.append("Documento: Ya existe un usuario con este documento")
        
        # Validar tipo de vínculo
        valido, tipo_nombre = Usuario.validar_tipo_vinculo(tipo_vinculo)
        if not valido:
            errores.append(f"Tipo de vínculo: {tipo_nombre}")
        
        if errores:
            return None, errores
        
        # Crear usuario
        usuario = Usuario(nombre.title(), apellido.title(), documento, tipo_nombre)
        self.usuarios[documento] = usuario
        
        return usuario, []
    
    def buscar_usuario(self, documento):
        """Busca un usuario por su documento"""
        return self.usuarios.get(documento)
    
    def obtener_todos_usuarios(self):
        """Retorna lista de todos los usuarios"""
        return list(self.usuarios.values())
    
    def mostrar_tipos_vinculo(self):
        """Muestra los tipos de vínculo disponibles con precios"""
        print("\nTipos de vínculo disponibles:")
        print("1. Estudiantes → $8,000")
        print("2. Docentes → $10,000") 
        print("3. Administrativos → $10,000")
        print("4. Oficiales internos → $8,000")
        print("5. Público externo → $15,000")
    
    def exportar_usuarios_csv(self, nombre_archivo="usuarios.csv"):
        """Exporta la lista de usuarios a un archivo CSV"""
        try:
            import csv
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(['Documento', 'Nombre', 'Apellido', 'Tipo_Vinculo', 'Num_Reservas'])
                
                for usuario in self.usuarios.values():
                    writer.writerow([
                        usuario.documento,
                        usuario.nombre,
                        usuario.apellido,
                        usuario.tipo_vinculo,
                        len(usuario.obtener_reservas_activas())
                    ])
            
            return True, f"Usuarios exportados exitosamente a {nombre_archivo}"
        except Exception as e:
            return False, f"Error al exportar usuarios: {str(e)}"
