from abc import ABC, abstractmethod


# 1. Clase abstracta Persona
class Persona(ABC):
    # 2. __init__ con los atributos nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # 3. Dos métodos abstractos obligatorios para las clases hijas
    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def actividad_diaria(self):
        pass

    # 4. Método normal (no abstracto): lo heredan tal cual las hijas
    def cumplir_anios(self):
        self.edad += 1
        return f"{self.nombre} ha cumplido años y ahora tiene {self.edad} años."


# 5.1 Clase hija Alumno con atributo extra curso
class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    # 6. Implementación propia de los métodos abstractos
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.curso}."

    def actividad_diaria(self):
        return f"{self.nombre} va a clase, toma apuntes y estudia {self.curso}."


# 5.2 Clase hija Profesor con atributo extra asignatura
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    # 6. Implementación propia de los métodos abstractos
    def presentarse(self):
        return f"Buenos días, soy {self.nombre}, tengo {self.edad} años e imparto {self.asignatura}."

    def actividad_diaria(self):
        return f"{self.nombre} prepara lecciones, da clase de {self.asignatura} y corrige exámenes."


# 7. Programa principal: crear 1 alumno y 1 profesor y ejecutar sus métodos
alumno = Alumno("Carlos", 19, "2.º de Business Analytics")
profesor = Profesor("Elena", 42, "Programación I")

for persona in [alumno, profesor]:
    print(persona.presentarse())
    print(persona.actividad_diaria())
    print(persona.cumplir_anios())
    print("-" * 45)

# 8. Intento de crear un objeto de la clase abstracta Persona directamente
try:
    pepe = Persona("Pepe", 30)
except TypeError as error:
    print("Error:", error)

# ¿Qué pasa?
# Python impide crear el objeto y lanza una excepción TypeError:
# "Can't instantiate abstract class Persona without an implementation for abstract methods 'actividad_diaria', 'presentarse'".
#
# ¿Por qué?
# Porque Persona es una clase abstracta (hereda de ABC) y contiene métodos obligatorios
# marcados con @abstractmethod ('presentarse' y 'actividad_diaria') que están sin implementar.
# Las clases abstractas funcionan como un contrato y están pensadas únicamente para que otras
# clases hereden de ellas; Python prohíbe instanciarlas directamente para evitar crear objetos
# incompletos que no tienen definidos esos métodos.