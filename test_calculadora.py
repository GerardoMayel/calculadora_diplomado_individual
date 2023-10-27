import pytest
from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.division import division
from operaciones.fracciones_a_numero import fraccion_a_numero

print('Pruebas Unitarias')


def test_suma():
    assert suma(5, 5) == 10
    assert suma(0, 0) == 0
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(5, 5) == 0
    assert resta(10, 5) == 5
    assert resta(-1, 1) == -2


def test_multiplicacion():
    assert multiplicacion(5, 5) == 25
    assert multiplicacion(0, 10) == 0
    assert multiplicacion(-1, 1) == -1


def test_division():
    assert division(10, 5) == 2
    assert division(0, 10) == 0
    with pytest.raises(ValueError):
        division(5, 0)


def test_fraccion_a_numero():
    assert fraccion_a_numero(5, 2) == 2.5
    assert fraccion_a_numero(7, 5) == 1.4
    assert fraccion_a_numero(0, 10) == 0


print('Pruebas de Integración')


def test_operacion_matematica_1():
    assert suma(5, 5) * resta(1.25, 0.75) == 5


def test_operacion_matematica_2():
    assert suma(8, fraccion_a_numero(7, 5)) * \
        resta(15, fraccion_a_numero(3, 8)) == pytest.approx(137.475)
