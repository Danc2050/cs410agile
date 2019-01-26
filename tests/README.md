# Automated tests

This folder contains all our automated tests and any helper files used for testing.

## Unit tests

Unit tests for each action test a single function across its range of inputs and verify that they provide the correct outputs in response. All unit tests are in the [unit](unit) folder.

## Integration tests

Integration tests for each action simulate user input and verify that the correct actions take place. Integration tests go in the [integration](integration) folder.


## Helper functions

Helper functions, i.e. functions that may be useful in more than one test, belong in [test_helpers.py](test_helpers.py). Or, if they're a good match for pytest's [fixtures](https://docs.pytest.org/en/latest/fixture.html), add your fixtures to the appropriate file, e.g. [conftest.py](conftest.py).


