import os
import sys
from gestor_usuarios import GestorUsuarios
from pelicula import GestorPeliculas
from reserva import GestorReservas
from cinema import Cinema, Administrador

class CinemaUdeA:
    """Clase principal del sistema Cinema UdeA"""
    
    def __init__(self):
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_peliculas = GestorPeliculas()
        self.gestor_reservas = GestorReservas()
        self.cinema = Cinema()
        self.administrador = Administrador()
        self.usuario_actual = None
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*60)
        print("              CINEMA UNIVERSITARIO UdeA")
        print("="*60)
        print("1. Registrar Usuario")
        print("2. Registrar Reserva")
        print("3. Cancelar Reserva")
        print("4. Consultar Funciones del Fin de Semana")
        print("5. Administrador")
        print("6. Salir")
        print("="*60)
    
    def registrar_usuario(self):
        """Proceso de registro de usuario"""
        print("\n" + "="*50)
        print("           REGISTRO DE USUARIO")
        print("="*50)
        
        try:
            nombre = input("Ingrese el nombre: ").strip()
            apellido = input("Ingrese el apellido: ").strip()
            documento = input("Ingrese el documento: ").strip()
            
            self.gestor_usuarios.mostrar_tipos_vinculo()
            tipo_vinculo = input("Seleccione el tipo de vínculo (1-5): ").strip()
            
            usuario, errores = self.gestor_usuarios.registrar_usuario(
                nombre, apellido, documento, tipo_vinculo
            )
            
            if errores:
                print("\n❌ ERRORES ENCONTRADOS:")
                for error in errores:
                    print(f"  • {error}")
            else:
                print(f"\n✅ Usuario registrado exitosamente:")
                print(f"   {usuario}")
                precio = usuario.obtener_precio_por_tipo(usuario.tipo_vinculo)
                print(f"   Precio por tiquete: ${precio:,}")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
        
        input("\nPresione Enter para continuar...")
    
    def registrar_reserva(self):
        """Proceso de registro de reserva"""
        print("\n" + "="*50)
        print("           REGISTRO DE RESERVA")
        print("="*50)
        
        try:
            # Solicitar documento del usuario
            documento = input("Ingrese su documento: ").strip()
            usuario = self.gestor_usuarios.buscar_usuario(documento)
            
            if not usuario:
                print("❌ Usuario no encontrado. Debe registrarse primero.")
                input("Presione Enter para continuar...")
                return
            
            print(f"\n👤 Bienvenido, {usuario.nombre} {usuario.apellido}")
            
            # Mostrar cartelera
            self.gestor_peliculas.mostrar_cartelera()
            
            # Seleccionar película
            try:
                opcion = int(input("\nSeleccione una película (número): ")) - 1
                pelicula = self.gestor_peliculas.obtener_pelicula_por_indice(opcion)
                
                if not pelicula:
                    print("❌ Opción inválida.")
                    input("Presione Enter para continuar...")
                    return
                
            except ValueError:
                print("❌ Debe ingresar un número válido.")
                input("Presione Enter para continuar...")
                return
            
            # Mostrar mapa de asientos
            self.cinema.mostrar_asientos(pelicula)
            
            # Seleccionar asiento
            while True:
                entrada_asiento = input("\nIngrese la posición del asiento (ej: A1, B5): ").strip().upper()
                
                numero_asiento, mensaje_error = self.cinema.validar_seleccion_asiento(entrada_asiento)
                
                if numero_asiento is None:
                    print(f"❌ {mensaje_error}")
                    continue
                
                if pelicula.esta_asiento_ocupado(numero_asiento):
                    print("❌ El asiento ya está ocupado. Seleccione otro.")
                    continue
                
                break
            
            # Crear reserva
            reserva, mensaje = self.gestor_reservas.crear_reserva(usuario, pelicula, numero_asiento)
            
            if reserva:
                print("\n✅ Reserva creada exitosamente!")
                print(reserva.generar_factura())
                
                # Preguntar si desea exportar la factura
                exportar = input("¿Desea exportar la factura a CSV? (s/n): ").strip().lower()
                if exportar == 's':
                    self.exportar_factura_csv(reserva)
            else:
                print(f"❌ Error al crear la reserva: {mensaje}")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
        
        input("\nPresione Enter para continuar...")
    
    def cancelar_reserva(self):
        """Proceso de cancelación de reserva"""
        print("\n" + "="*50)
        print("           CANCELAR RESERVA")
        print("="*50)
        
        try:
            documento = input("Ingrese su documento: ").strip()
            usuario = self.gestor_usuarios.buscar_usuario(documento)
            
            if not usuario:
                print("❌ Usuario no encontrado.")
                input("Presione Enter para continuar...")
                return
            
            reservas_activas = usuario.obtener_reservas_activas()
            
            if not reservas_activas:
                print("❌ No tiene reservas activas para cancelar.")
                respuesta = input("¿Desea realizar una nueva reserva? (s/n): ").strip().lower()
                if respuesta == 's':
                    self.registrar_reserva()
                return
            
            print(f"\n👤 {usuario.nombre} {usuario.apellido}")
            print("\nSus reservas activas:")
            for i, reserva in enumerate(reservas_activas, 1):
                posicion = self.cinema.convertir_numero_a_posicion(reserva.numero_asiento)
                print(f"{i}. {reserva.pelicula.nombre} - Asiento {posicion} (ID: {reserva.id})")
            
            try:
                opcion = int(input("\nSeleccione la reserva a cancelar (número): ")) - 1
                
                if 0 <= opcion < len(reservas_activas):
                    reserva_seleccionada = reservas_activas[opcion]
                    exito, mensaje = self.gestor_reservas.cancelar_reserva(reserva_seleccionada.id)
                    
                    if exito:
                        print(f"✅ {mensaje}")
                    else:
                        print(f"❌ {mensaje}")
                else:
                    print("❌ Opción inválida.")
                    
            except ValueError:
                print("❌ Debe ingresar un número válido.")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
        
        input("\nPresione Enter para continuar...")
    
    def consultar_funciones(self):
        """Muestra las funciones del fin de semana"""
        print("\n" + "="*60)
        print("         FUNCIONES DEL FIN DE SEMANA")
        print("="*60)
        
        peliculas = self.gestor_peliculas.obtener_peliculas()
        
        # Agrupar por día
        sabado = [p for p in peliculas if p.dia == "Sábado"]
        domingo = [p for p in peliculas if p.dia == "Domingo"]
        
        print("\n🗓️  SÁBADO:")
        for pelicula in sabado:
            print(f"   {pelicula.hora} - {pelicula.nombre}")
            print(f"            Duración: {pelicula.duracion}")
            print(f"            Asientos disponibles: {pelicula.obtener_asientos_disponibles()}")
            print()
        
        print("🗓️  DOMINGO:")
        for pelicula in domingo:
            print(f"   {pelicula.hora} - {pelicula.nombre}")
            print(f"            Duración: {pelicula.duracion}")
            print(f"            Asientos disponibles: {pelicula.obtener_asientos_disponibles()}")
            print()
        
        input("Presione Enter para continuar...")
    
    def menu_administrador(self):
        """Menú del administrador"""
        print("\n" + "="*50)
        print("           ACCESO ADMINISTRADOR")
        print("="*50)
        
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()
        
        if not self.administrador.validar_credenciales(usuario, contraseña):
            print("❌ Credenciales incorrectas.")
            input("Presione Enter para continuar...")
            return
        
        while True:
            print("\n" + "="*50)
            print("           PANEL ADMINISTRATIVO")
            print("="*50)
            print("1. Ver reporte completo")
            print("2. Lista de usuarios")
            print("3. Exportar datos a CSV")
            print("4. Volver al menú principal")
            print("="*50)
            
            try:
                opcion = input("Seleccione una opción: ").strip()
                
                if opcion == "1":
                    reporte = self.administrador.generar_reporte_completo(
                        self.gestor_usuarios, self.gestor_reservas
                    )
                    print(reporte)
                    input("Presione Enter para continuar...")
                
                elif opcion == "2":
                    self.mostrar_lista_usuarios()
                
                elif opcion == "3":
                    self.exportar_datos_csv()
                
                elif opcion == "4":
                    break
                
                else:
                    print("❌ Opción inválida.")
                    input("Presione Enter para continuar...")
            
            except KeyboardInterrupt:
                print("\n\nVolviendo al menú principal...")
                break
    
    def mostrar_lista_usuarios(self):
        """Muestra la lista de usuarios registrados"""
        usuarios = self.gestor_usuarios.obtener_todos_usuarios()
        
        if not usuarios:
            print("\n❌ No hay usuarios registrados.")
        else:
            print(f"\n📋 USUARIOS REGISTRADOS ({len(usuarios)}):")
            print("-" * 80)
            print(f"{'Documento':<15} {'Nombre':<20} {'Apellido':<20} {'Tipo':<15} {'Reservas':<10}")
            print("-" * 80)
            
            for usuario in usuarios:
                num_reservas = len(usuario.obtener_reservas_activas())
                print(f"{usuario.documento:<15} {usuario.nombre:<20} {usuario.apellido:<20} {usuario.tipo_vinculo:<15} {num_reservas:<10}")
        
        input("\nPresione Enter para continuar...")
    
    def exportar_datos_csv(self):
        """Exporta datos del sistema a archivos CSV"""
        print("\n📊 EXPORTAR DATOS A CSV")
        print("1. Exportar usuarios")
        print("2. Exportar reservas")
        print("3. Exportar ambos")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion in ["1", "3"]:
            exito, mensaje = self.gestor_usuarios.exportar_usuarios_csv()
            print(f"{'✅' if exito else '❌'} {mensaje}")
        
        if opcion in ["2", "3"]:
            exito, mensaje = self.exportar_reservas_csv()
            print(f"{'✅' if exito else '❌'} {mensaje}")
        
        input("\nPresione Enter para continuar...")
    
    def exportar_reservas_csv(self, nombre_archivo="reservas.csv"):
        """Exporta las reservas a un archivo CSV"""
        try:
            import csv
            reservas = self.gestor_reservas.obtener_reservas_activas()
            
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(['ID_Reserva', 'Usuario', 'Documento', 'Pelicula', 'Dia', 'Hora', 'Asiento', 'Precio', 'Fecha_Reserva'])
                
                for reserva in reservas:
                    writer.writerow([
                        reserva.id,
                        f"{reserva.usuario.nombre} {reserva.usuario.apellido}",
                        reserva.usuario.documento,
                        reserva.pelicula.nombre,
                        reserva.pelicula.dia,
                        reserva.pelicula.hora,
                        self.cinema.convertir_numero_a_posicion(reserva.numero_asiento),
                        reserva.precio,
                        reserva.fecha_reserva.strftime('%Y-%m-%d %H:%M:%S')
                    ])
            
            return True, f"Reservas exportadas exitosamente a {nombre_archivo}"
        except Exception as e:
            return False, f"Error al exportar reservas: {str(e)}"
    
    def exportar_factura_csv(self, reserva):
        """Exporta una factura individual a CSV"""
        try:
            import csv
            nombre_archivo = f"factura_{reserva.id}.csv"
            
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(['Campo', 'Valor'])
                writer.writerow(['ID_Reserva', reserva.id])
                writer.writerow(['Cliente', f"{reserva.usuario.nombre} {reserva.usuario.apellido}"])
                writer.writerow(['Documento', reserva.usuario.documento])
                writer.writerow(['Tipo_Usuario', reserva.usuario.tipo_vinculo])
                writer.writerow(['Pelicula', reserva.pelicula.nombre])
                writer.writerow(['Dia', reserva.pelicula.dia])
                writer.writerow(['Hora', reserva.pelicula.hora])
                writer.writerow(['Asiento', self.cinema.convertir_numero_a_posicion(reserva.numero_asiento)])
                writer.writerow(['Precio', reserva.precio])
                writer.writerow(['Fecha_Reserva', reserva.fecha_reserva.strftime('%Y-%m-%d %H:%M:%S')])
            
            print(f"✅ Factura exportada a {nombre_archivo}")
        except Exception as e:
            print(f"❌ Error al exportar factura: {str(e)}")
    
    def ejecutar(self):
        """Método principal para ejecutar el sistema"""
        print("🎬 Iniciando Cinema Universitario UdeA...")
        
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = input("Seleccione una opción: ").strip()
                
                if opcion == "1":
                    self.registrar_usuario()
                elif opcion == "2":
                    self.registrar_reserva()
                elif opcion == "3":
                    self.cancelar_reserva()
                elif opcion == "4":
                    self.consultar_funciones()
                elif opcion == "5":
                    self.menu_administrador()
                elif opcion == "6":
                    print("\n👋 ¡Gracias por usar Cinema Universitario UdeA!")
                    break
                else:
                    print("❌ Opción inválida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
            
            except KeyboardInterrupt:
                print("\n\n👋 ¡Gracias por usar Cinema Universitario UdeA!")
                break
            except Exception as e:
                print(f"\n❌ Error inesperado: {str(e)}")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
    cinema = CinemaUdeA()
    cinema.ejecutar()
