import mysql.connector




# Nos conectamos a MySQL
conn = mysql.connector.connect(
    host = "localhost",  # Ingresamos la dirección IP
    user = "root",  # Escribimos nuestro ususario, en este caso es "root" ya que no lo hemos cambiado y es el valor por defecto.
    password = "",  # Escribimos nuestra contraseña, en este caso esta vacio porque no lo hemos configurado y es el valor por defecto.
    port = "3306",  # Ingresamos el puerto, para nuestra pc con xampp es "3306"
    database = "computadoras"  # Escribimos el nombre de la base de datos
)

# print(conn)  # Verificamos que se conecto de manera correcta.




# Creamos un cursor
cursor = conn.cursor()





# Creamos una base de datos
cursor.execute("SHOW DATABASES")  # Verificamos que no exista la base de datos que vamos a crear, mirando todas las bases existentes
for db in cursor:  # Mostramos en consola las bases de datos existentes
    print(db)
    
# cursor.execute("CREATE DATABASE computadoras")  # Este comando solo lo ejecutaremos una vez por cada vez que se cree una nueva base de datos, despues debemos comentarlo sino nos arrojara un error.





# Creamos una tablas
cursor.execute("SHOW TABLES")  # Verificamos que no exista la tabla que vamos a crear, mirando todas las tablas existentes
for tb in cursor:  # Mostramos en consola las tablas existentes
    print(tb)
    
# sql = """CREATE TABLE clientes(nombre VARCHAR(255), dirección VARCHAR(255))"""  # Variable para indicar el comando SQL que usara python para crear nuestra tabla
# cursor.execute(sql)  # Crea una tabla con dos columnas en donde podemos almacenar cadenas de longitud variable con límite de 255 caracteres

# Creamos otra tabla
# sql = """CREATE TABLE empleados(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), puesto VARCHAR(200))"""
# cursor.execute(sql)

# Añadimos una columna a una tabla existente
# sql = """ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"""  # Comando SQL para añadir una columna a una tabla
# cursor.execute(sql)




# Insertar datos en una tabla
sql = """INSERT INTO clientes (nombre, dirección) VALUES (%s, %s)"""  # Comando SQL para insertar datos en una tabla
# valores_1 = ("Bryan", "Quito")  # Almacena los datos que queremos insertar para reemplazarlos en donde esta %s, en el orden especificado
# cursor.execute(sql, valores_1)  

#Para insertar varios datos a la vez creamos una lista con tuplas y usamos el método executemany.
valores_2 = [
    ("Karla", "USA"),
    ("Veronica", "Machala"),
    ("Camila", "Ibarra"),
    ("Antonio", "España"),
    ("Francis", "Quito")
]

# cursor.executemany(sql, valores_2)

# Motramos en pantalla el registro o fila ingresada por cada nueva insercion esto empieza desde cero.
# print(cursor.rowcount, "registros insertados")

# Para insertar un dato de manera directa seria:
# cursor.execute("""INSERT INTO clientes (nombre, dirección) VALUES ("Anderson", "Tulcán")""")

# Para mostrar el ultimo registro ingresado usamos:
print("Se inserto el ID: ", cursor.lastrowid)





    







# Comprometemos nuestra base de datos
conn.commit()

# Cerramos el conector (Nos desconectamos)
conn.close()