import pytest
from ..day1 import SearchParty

TESTFILE = "test/day1-1-input"

@pytest.fixture
def search_party():
    sp = SearchParty(TESTFILE)
    return sp

def test_first_elf(search_party):
    totals = search_party.data.groupby("elf").sum()
    assert totals.loc[0]["calories"] == 6000
    assert totals.loc[1]["calories"] == 4000
    assert totals.loc[2]["calories"] == 11000
    assert totals.loc[3]["calories"] == 24000
    assert totals.loc[4]["calories"] == 10000

