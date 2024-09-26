import datetime
# Clase
class clase_cliente1289:
    id_cliente1289=0
    nombre1289=""
    email1289=""
    telefono1289=""
    direccion1289=""
    activo1289=bool
    fecha_registro1289=""
    def mostrar_datos1289(self):
        print("Datos del cliente:")
        print(f"Tu id es:{self.id_cliente1289}")
        print(f"Tu nombre es:{self.nombre1289}")
        print(f"Tu email es:{self.email1289}")
        print(f"Tu telefono es:{self.telefono1289}")
        print(f"Tu direccion es:{self.direccion1289}")
        print(f"Tu eres un cliente:{self.activo1289}")
        print(f"Tu fecha de registro es:{self.fecha_registro1289}")

    def Lista_clientes1289(self):
        print("\nLista de clientes:")
        clientes=["Martin","Cesar","Jesus","Gael","Matias","brisa","Sofia"]
        for lista in clientes:
            print(lista)
    
    def Tupla_empleados1289(self):
        print("\nTupla de empleados:")
        empleados=("Joaquin","Ramiro","Fernando","Angel","Gabriel","Alexis","Mateo")
        for tupla in empleados:
            print(tupla)
        
    def Dicccionario_estrellas1289(self):
        print("\nDiccionario de estrellas:")
        estrellas={
            "Comida":"5 estrellas",
            "Servicio":"4 estrellas",
            "Limpieza":"4 estrellas",
            "Costo":"3 estrellas",
            "Reservacion":"4 estrellas",
            "Amabilidad":"5 estrellas",
            "Tiempo de espera":"4 estrellas"
        }
        for x,y in estrellas.items():
            print(x,y)

    
    def altas1289(self):
        print("\nEl producto se guardo correctamente de la base de datos")

    def bajas1289(self):
        print("El producto se borro correctamente de la base de datos")

# creacion del objeto
objetocliente1289=clase_cliente1289()
# asignacion de datos
objetocliente1289.id_cliente1289=8954084361289
objetocliente1289.nombre1289="Reyes"
objetocliente1289.email1289="a.22308051281289@cbtis128.edu.mx"
objetocliente1289.telefono1289="656-834-9512"
objetocliente1289.direccion1289="Calle saturno 12-89"
objetocliente1289.activo1289=bool(1)
objetocliente1289.fecha_registro1289=datetime.datetime(2007, 1, 6)
# Resultado
objetocliente1289.mostrar_datos1289()
objetocliente1289.Lista_clientes1289()
objetocliente1289.Tupla_empleados1289()
objetocliente1289.Dicccionario_estrellas1289()
objetocliente1289.altas1289()
objetocliente1289.bajas1289()