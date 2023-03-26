# Testing with Python
## Unit Test
- A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
- with assert you can check a condition and if it is incorrect, it raises an Assertion Error
````python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
````

