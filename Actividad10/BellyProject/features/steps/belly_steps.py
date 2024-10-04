from behave import given, when, then
from belly import Belly
import re

# Crear una instancia de Belly
belly = Belly()

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    # Diccionario extendido para números
    numeros = {
        "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
        "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
        "veinte": 20,"veinticinco":25, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
        "cien": 100, "mil": 1000, "un monton":11, "un":1
    }
    numeros_en_ingles = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "thirty":30
    }
    if palabra in numeros:
        return numeros[palabra]
    elif palabra in numeros_en_ingles:
        return numeros_en_ingles[palabra]
    return int(palabra)
# Dado que he comido {cukes:d} pepinos
@given('que he comido {cukes}')
def step_given_eaten_cukes(context, cukes):
    pattern = re.compile(r"(?:\"?(\w+\s*\w+|-\d)\"?)\s*(?:de)?\s*pepinos?")
    groups = pattern.match(cukes.lower())
    n_cukes = convertir_palabra_a_numero(groups.group(1))
    belly.comer(n_cukes)

# Cuando espero "{time_description}"
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    # Expresión regular actualizada para horas, minutos y segundos
    pattern = re.compile(r'(?:(\w+)\s*(?:horas?|hours?))?(?:\,|and|y)?\s*(?:(\w+)\s*(?:minutos?|minutes?))?\s*(?:y|and)?\s*(?:(\w+)\s*(?:segundos?|seconds?))?')
    match = pattern.match(time_description.lower())
    # Si se encuentra coincidencia, convertir palabras o números a horas, minutos y segundos
    if match:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        seconds_word = match.group(3) if match.group(3) else "0"
        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)
        print(hours,minutes,seconds)
        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        belly.esperar(total_time_in_hours)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

# Entonces mi estómago debería gruñir
@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

# Entonces mi estómago no debería gruñir
@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."