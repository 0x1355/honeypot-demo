import pytest, math
from tx import Tx


tx_hash = '0x18ec2c2e5720c6d332a0f308f8803e834e06c78dcebdc255178891ead56c6d73'
fail_hash = '0xfef3de902c39c2e06b8ed9de31db37becf3809b419201890623672a7841bdd97'

@pytest.fixture(scope="module")
def new_tx():
    yield Tx(tx_hash)

    
def test_address(new_tx):
    assert(new_tx.hash == tx_hash)

    
@pytest.fixture(scope="module")
def tx(new_tx):
    new_tx.fetch_data()
    yield new_tx


@pytest.fixture(scope="module")
def failed_tx():
    tx = Tx(fail_hash)
    tx.fetch_data()
    yield tx
    
    
def test_tx_block_number(tx):
    assert(tx.block_number == 13710082)


def test_failed_block_number(failed_tx):
    assert(failed_tx.block_number == 13694858)


def test_tx_status(tx):
    assert(tx.status == 1)


def test_failed_status(failed_tx):
    assert(failed_tx.status == 0)


def test_tx_gas(tx):
    assert(tx.gas_used == 52048)


def test_failed_gas(failed_tx):
    assert(failed_tx.gas_used == 634017)


def test_tx_gas_price(tx):
    assert(tx.gas_price == 126961080916)


def test_failed_gas_price(failed_tx):
    assert(failed_tx.gas_price == 96452256058)


def test_tx_gas_cost(tx):
    assert math.isclose(tx.gas_cost, 0.00660807033, rel_tol=1e-07)


def test_tx_index(tx):
    assert(tx.index == 0)


def test_failed_index(failed_tx):
    assert(failed_tx.index == 36)
