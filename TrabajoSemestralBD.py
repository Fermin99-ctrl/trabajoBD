import psycopg2;

bucle = True
cursor = None
conexion = None

def menu_opciones(opcion):
    if opcion == 1:
        nombres = input("Ingrese los nombres del alumno\n: ")
        apellido_paterno = input("Ingrese el apellido parterno del alumno\n ")
        apellido_materno = input("Ingrese el apellido materno del alumno\n: ")
        fecha_nacimiento = input("Ingrese la fehca de nacimiento del alumno ejemplo 2004-05-06 ")
        direccion = input("Ingrese la direccion: ")
        ciudad = input("Ingrese la ciudad del alumno: ")
        codigo_curso = input("Ingrese el codigo del curso : ")
        cursor.execute("INSERT INTO usuarios (nombres, edad) VALUES ($s, $s, $s, $s, $s, $s, %s)", (nombres,apellido_paterno,apellido_materno,fecha_nacimiento,direccion,ciudad,codigo_curso))

        # 4. Confirmar la inserción
        conexion.commit()

        # 5. Cerrar la conexión
        conexion.close()

        print("Datos insertados correctamente.")
        return True
    elif opcion == 2:
        print("Puede modificar los siguientes datos rut, Nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso")
        id=input("para modificar el alumno debe ingresar el rut de alumno al cual quiere modificar sus componentes")
        cursor.execute("UPDATE alumno SET direccion=%s WHERE rut=%s", (id))
        print(alumno)
        conexion.commit()
        
        cursor.execute("SELECT * FROM alumno;")
        lista_alumno = cursor.fetchall()
        print("\nAlumno DE LA TABLA 'ALUMNO' MODIFICADA: ")
        for alumno in lista_alumno:
            print(alumno)
        return True
    elif opcion == 3:
        print("Has elegido la opción 3")
        return True
    elif opcion >= 4:
        return False            
    else:
        print("Opción inválida vuelva a intentarlo")
        return True
        # Ejemplo de uso
        # menu_opciones (2)

try:
    conexion = psycopg2.connect(
        database='TrabajoSemestralBD',
        user='postgres',
        password='fire323',
        host='localhost',
        port='5432'
    )
    
    # Crear cursor
    cursor = conexion.cursor()
    
    # Ejecutar una consulta (crear tabla)
    ALUMNO = """
    CREATE TABLE IF NOT EXISTS ALUMNO (
        Rut VARCHAR(100) PRIMARY KEY,
        Nombres VARCHAR(100),
        apellido_paterno VARCHAR(100),
        apellido_materno VARCHAR(100),
        fecha_nacimiento DATE,
        direccion VARCHAR(100),
        ciudad VARCHAR(100),
        codigo_curso INT REFERENCES curso(codigo_curso)
    );
    """
    APODERADO = """
    CREATE TABLE IF NOT EXISTS APODERADO (
        Rut VARCHAR(100) PRIMARY KEY,
        Nombres VARCHAR(100),
        apellido_paterno VARCHAR(100),
        apellido_materno VARCHAR(100),
        direccion VARCHAR(100),
        ciudad VARCHAR(100)
    );
    """

    REPRESENTA = """
    CREATE TABLE IF NOT EXISTS REPRESENTA (
        Rut_Alumno VARCHAR(100)  REFERENCES alumno(Rut),
        Rut_apoderado VARCHAR(100) REFERENCES apoderado(Rut),
        fecha_inicio DATE,
        fecha_termino DATE
    );
    """

    CURSO = """
    CREATE TABLE IF NOT EXISTS CURSO (
        codigo_curso INT PRIMARY KEY,
        año INTEGER
    );
    """
    MEDIA = """
    CREATE TABLE IF NOT EXISTS MEDIA (
        Codigo INT PRIMARY KEY REFERENCES curso(codigo_curso),
        orientación VARCHAR(100)
    );
    """
    BASICA = """
    CREATE TABLE IF NOT EXISTS BASICA (
        Codigo INT PRIMARY KEY REFERENCES curso(codigo_curso),
    );
    """

    PROFESOR = """
    CREATE TABLE IF NOT EXISTS PROFESOR (
        Rut VARCHAR(100) PRIMARY KEY,
        Nombres  VARCHAR(100),
        apellido_paterno VARCHAR(100),
        apellido_materno VARCHAR(100),
        direccion VARCHAR(100),
        ciudad VARCHAR(100)
    );
    """

    EXTRAPROGRAMATICA = """
    CREATE TABLE IF NOT EXISTS EXTRAPROGRAMATICA (
        codigo INT PRIMARY KEY,
        nombre VARCHAR(100),
        dia DATE,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        cupos INTEGER,
        lugar VARCHAR(100),
        Rut_profesor VARCHAR(100) PRIMARY KEY REFERENCES profesor(Rut)
    );
    """

    PARTICIPA = """
    CREATE TABLE IF NOT EXISTS PARTICIPA (
        Rut_Alumno VARCHAR(100)  REFERENCES alumno(Rut),
        Codigo INT PRIMARY KEY REFERENCES extraprogramatica(codigo)
    );
    """

    ES_JEFE = """
    CREATE TABLE IF NOT EXISTS ES_JEFE (
        codigo_curso INT PRIMARY KEY,
        rut_profesor_jefe VARCHAR(100) PRIMARY KEY REFERENCES profesor(Rut)
    );
    """

    ES_ASISTENTE = """
    CREATE TABLE IF NOT EXISTS ES_ASISTENTE (
        codigo_curso INT PRIMARY KEY,
        rut_profesor_asistente VARCHAR(100) PRIMARY KEY REFERENCES profesor(Rut)
    );
    """

    ESPECIALIDAD = """
    CREATE TABLE IF NOT EXISTS ESPECIALIDAD (
        codigo_especialidad INT PRIMARY KEY,
        descripcion VARCHAR(100)
    );
    """

    TIENE = """
    CREATE TABLE IF NOT EXISTS TIENE (
        rut_profesor VARCHAR(100) PRIMARY KEY REFERENCES profesor(Rut),
        codigo_especialidad INT PRIMARY KEY REFERENCES especialidad(codigo_especialidad)
    );
    """
    cursor.execute(CURSO)
    cursor.execute(ALUMNO)
    cursor.execute(APODERADO)
    cursor.execute(REPRESENTA)
    cursor.execute(MEDIA)
    cursor.execute(BASICA)
    cursor.execute(PROFESOR)
    cursor.execute(EXTRAPROGRAMATICA)
    cursor.execute(PARTICIPA)
    cursor.execute(ES_JEFE)
    cursor.execute(ES_ASISTENTE)
    cursor.execute(ESPECIALIDAD)
    cursor.execute(TIENE)

    # [C] Crear 4 alumno y 4 apoderado
    # INSERT INTO alumno y apoderado (rut, nombre,apellido_paterno , apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso ) VALUES (1, 'Gabriel Garcia Marquez', 'Colombia', '1927-03-06)
    cursor.execute('INSERT INTO alumno (rut, Nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',('21.570.482-3', 'Gabriel Gamaliel', 'Boric', 'Font', '2004-05-06', 'O-Higgins 914A', 'Punta Arenas', '201'))
    cursor.execute('INSERT INTO alumno (rut, Nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',('21.144.995-k', 'Miguel Juan Sebastián', 'Piñera', 'Echeñique', '2005-05-06', 'Patricio Patrito 210B', 'Punta Arenas', '101'))
    cursor.execute('INSERT INTO alumno (rut, Nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',('22.724.988-2', 'José Antonio', 'Kast', 'Rist', '2003-05-06', 'Pedro Aguirre Cerda 510B', 'Punta Arenas', '201'))
    cursor.execute('INSERT INTO alumno (rut, Nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',('22.724.988-2', 'Pasenos Porfa', 'Plis', 'Plis', '2003-05-06', 'Pedro Aguirre Cerda 1010B', 'Punta lavapies', '301'))
    cursor.execute('INSERT INTO apoderado (rut, Nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s)',('12.553.878-3', 'Eduardo Alberto', 'Piñera', 'Palma', 'Patricio Patrito 210B', 'Punta Arenas'))
    cursor.execute('INSERT INTO apoderado (rut, Nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s)',('15.780.146-7', 'Patricio Pablo', 'Kast', 'McGönagall', 'O-Higgins 914A', 'Punta Arenas'))
    cursor.execute('INSERT INTO apoderado (rut, Nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s)',('16.180.246-2', 'Elba Verónica', 'Lazo', 'Marín', 'O-Higgins 914A', 'Punta Arenas'))
    cursor.execute('INSERT INTO Representa ( Rut_Alumno, Rut_apoderado, fecha_inicio, fecha_termino) VALUES (%s, %s, %s, %s)',('21.144.995-k', '12.553.878-3', '23-07-2025', '28-07-2025'))
    cursor.execute('INSERT INTO Curso (codigo_curso, año) VALUES (%s, %s)',('201', '2025'))
    cursor.execute('INSERT INTO Curso (codigo_curso, año) VALUES (%s, %s)',('101', '2025'))
    cursor.execute('INSERT INTO Curso (codigo_curso, año) VALUES (%s, %s)',('301', '2025'))
    cursor.execute('INSERT INTO Media (Codigo INT, orientación) VALUES (%s, %s)',('2', 'Evaluaciones, Objetivos, Normas'))
    cursor.execute('INSERT INTO Basica (Codigo INT) VALUES (%s)',('2'))
    cursor.execute('INSERT INTO Profesor (rut, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s)',('13.038.082-4', 'Dodoria', 'Caes', 'Mal', '2004-05-06', 'O-Higgins Nana 714A', 'Punta Lago'))
    cursor.execute('INSERT INTO Profesor (rut, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s)',('11.168.832-k', 'Miguel toto', 'Monzalva','Salas', '2005-05-06', 'Patricio Trapito 110B', 'Punta Arenas'))
    cursor.execute('INSERT INTO Profesor (rut, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s )',('5.892.317-6', 'José Mato', 'Sangre', 'Fria', '2003-05-06', 'Pedro Cerda 910B', 'Punta cerro'))
    cursor.execute('INSERT INTO Extraprogramatica (codigo,nombre,dia,hora_inicio,hora_fin,cupos,lugar,Rut_profesor) VALUES (%s, %s, %s, %s, %s, %s, %s. %s )',('77', 'Fisica', 'Lunes', '11:10', '12:30', '20','laboratorio','5.892.317-6')) 
    cursor.execute('INSERT INTO Extraprogramatica (codigo,nombre,dia,hora_inicio,hora_fin,cupos,lugar,Rut_profesor) VALUES (%s, %s, %s, %s, %s, %s, %s. %s )',('77', 'Programacion', 'martes', '11:10', '12:30', '20','laboratorio','5.892.317-6')) 
    cursor.execute('INSERT INTO tiene (rut_profesor, codigo_especialidad) VALUES (%s, %s)',('13.038.082-4', '21'))
    cursor.execute('INSERT INTO tiene (rut_profesor, codigo_especialidad) VALUES (%s, %s)',('11.168.832-k', '22'))
    cursor.execute('INSERT INTO tiene (rut_profesor, codigo_especialidad) VALUES (%s, %s)',('5.892.317-6', '23'))
    cursor.execute('INSERT INTO especialidad (codigo_especialidad, descripcion) VALUES (%s, %s)',('21', 'Matemáticas'))
    cursor.execute('INSERT INTO especialidad (codigo_especialidad, descripcion) VALUES (%s, %s)',('22', 'Lenguaje'))
    cursor.execute('INSERT INTO especialidad (codigo_especialidad, descripcion) VALUES (%s, %s)',('23', 'Ciencias'))
    cursor.execute('INSERT INTO es_asistente (codigo_curso, rut_profesor_asistente) VALUES (%s, %s)',('101', '13.038.082-4'))
    cursor.execute('INSERT INTO es_asistente (codigo_curso, rut_profesor_asistente) VALUES (%s, %s)',('201', '11.168.832-k'))
    cursor.execute('INSERT INTO es_asistente (codigo_curso, rut_profesor_asistente) VALUES (%s, %s)',('301', '5.892.317-6'))
    cursor.execute('INSERT INTO es_jefe (codigo_curso, rut_profesor_jefe) VALUES (%s, %s)',('201', '13.038.082-4'))
    cursor.execute('INSERT INTO es_jefe (codigo_curso, rut_profesor_jefe) VALUES (%s, %s)',('301', '11.168.832-k'))
    cursor.execute('INSERT INTO es_jefe (codigo_curso, rut_profesor_jefe) VALUES (%s, %s)',('101', '5.892.317-6'))
    cursor.execute('INSERT INTO participa (rut_alumno, codigo) VALUES (%s, %s)',('201', '13.038.082-4'))
    cursor.execute('INSERT INTO participa (rut_alumno, codigo) VALUES (%s, %s)',('301', '11.168.832-k'))
    cursor.execute('INSERT INTO participa (rut_alumno, codigo) VALUES (%s, %s)',('101', '5.892.317-6'))

    
    conexion.commit()
    print("Registros insertados correctamente")

    while bucle:
        print("Bienvenido le sirvo un cafecito ")
        print("debe elegir entre matarse o elegir una opcion:\n ")
        print("1.Ingresar datos a la tabla alumno\n ")
        print("2.modificar la tabla alumno\n")
        print("ssss")
        print("salir\n")
        opcion=input()
        bucle =menu_opciones(opcion)

except psycopg2.Error as error:
    print("Error al conectar a la base de datos: ", error)
finally:
    #Cerrar cursor y conexion
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()

