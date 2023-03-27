# Testing with Python
## Unit Test
- A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
- with assert you can check a condition and if it is incorrect, it raises an Assertion Error
````python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
````

## UnitTest (framework)
- La biblioteca de pruebas "unittest" ha sido incorporada en la librería estándar de Python desde la versión 2.1. Es muy común encontrarla en aplicaciones comerciales y proyectos de código abierto.
- "unittest" contiene tanto un framework como un runner para pruebas. Tiene algunos requisitos importantes para escribir y ejecutar pruebas. Por ejemplo, "unittest" requiere que las pruebas sean colocadas en clases como métodos, y que se usen una serie de métodos de aserción especiales en la clase "unittest.TestCase" en lugar del comando "assert"
