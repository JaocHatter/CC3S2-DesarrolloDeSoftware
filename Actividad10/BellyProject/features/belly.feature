Feature: Característica del Estómago

  Scenario: Comer muchos pepinos y gruñir
    Given que he comido 42 pepinos
    When espero 2 horas
    Then mi estómago debería gruñir

  Scenario: Comer pocos pepinos y no gruñir
    Given que he comido 10 pepinos
    When espero 2 horas
    Then mi estómago no debería gruñir

  Scenario: Comer muchos pepinos y esperar menos de una hora
    Given que he comido 50 pepinos
    When espero 30 minutos
    Then mi estómago no debería gruñir

  Scenario: Comer pepinos y esperar en minutos
    Given que he comido 30 pepinos
    When espero 90 minutos
    Then mi estómago debería gruñir

  Scenario: Comer pepinos y esperar en diferentes formatos
    Given que he comido 25 pepinos
    When espero "2 horas y 30 minutos"
    Then mi estómago debería gruñir



  Scenario: Comer diferentes cantidades de pepinos en varios tiempos
    Given que he comido 30 pepinos
    When espero "una hora y 30 minutos"
    Then mi estómago debería gruñir

  Scenario: Comer pepinos sin especificar cantidad exacta
    Given que he comido "un monton" de pepinos
    When espero 3 horas
    Then mi estómago debería gruñir

  Scenario: Comer pepinos y esperar un tiempo exacto en minutos
    Given que he comido 20 pepinos
    When espero 120 minutos
    Then mi estómago debería gruñir

  Scenario: Comer pepinos en palabras y esperar en minutos
    Given que he comido "veinticinco pepinos" 
    When espero 90 minutos
    Then mi estómago debería gruñir



  Scenario: Manejar tiempos complejos
    Given que he comido 50 pepinos
    When espero "1 hora, 30 minutos y 45 segundos"
    Then mi estómago debería gruñir



  Scenario: Manejar una cantidad no válida de pepinos
    Given que he comido -5 pepinos
    When espero "1 hora, 30 minutos y 45 segundos"
    Then mi estómago debería gruñir



  Scenario: Comer pepinos y esperar en inglés
    Given que he comido 15 pepinos
    When espero "two hours and thirty minutes"
    Then mi estómago debería gruñir