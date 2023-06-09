import pytest
from Invoice import Invoice
#Shashank Mondrati
#Student ID: 801026182

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalucateTotalImpurePrice(invoice, products):
     pass #invoice.totalImpurePrice(products)


def test_CanCalucateTotalDiscount(invoice, products):
    pass #invoice.totalDiscount(products)


def test_CanCalucateTotalPurePrice(invoice, products):
    pass #invoice.totalPurePrice(products)
