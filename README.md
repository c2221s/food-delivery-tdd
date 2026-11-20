# food-delivery-tdd
TDD assignment for food delivery system, developed for Software Testing course.

## Project Overview
This project is implemented following Test-Driven Development (TDD).
We design test cases first to cover normal business flows, boundary scenarios and invalid operations, then implement the order logic to make all tests pass.
It simulates a food delivery order system with strict state transition constraints.

## File Structure
- `delivery_system.py` : Core business code. Contains the `DeliveryOrder` class and custom exception `InvalidOrderOperationError`.
- `test_delivery.py` : Pytest test suite. Verifies normal workflows and illegal state transitions.

## State Transition Rules
Valid transitions:
- pending → delivering (accept_order)
- delivering → completed (finish_delivery)
- pending → cancelled (cancel_order)

Any other state change is invalid and will raise `InvalidOrderOperationError`.

## How to Run
```bash
pip install pytest
pytest test_delivery.py -v
