from dataclasses import dataclass

import pytest

@dataclass
class Customer:
    name: str
    orders: list

    def destroy(self):
        print(f"Object {self.name} has been destroyed")

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}
    return _make_customer_record

@pytest.fixture
def make_manageable_customer_record():
    created_records = []

    def _make_customer_record(name):
        rec = Customer(name=name, orders=[])
        created_records.append(rec)
        return rec

    yield _make_customer_record

    for record in created_records:
        record.destroy()

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    assert customer_1.get("name") == "Lisa"
    assert customer_2.get("name") == "Mike"
    assert customer_3.get("name") == "Meredith"


def test_customer_manageable_records(make_manageable_customer_record):
    customer_1 = make_manageable_customer_record("Lisa")
    customer_2 = make_manageable_customer_record("Mike")
    customer_3 = make_manageable_customer_record("Meredith")
    assert customer_1.name == "Lisa"
    assert customer_2.name == "Mike"
    assert customer_3.name == "Meredith1"