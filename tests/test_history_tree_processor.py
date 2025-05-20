import pytest
from browser_use.dom.history_tree_processor.service import HistoryTreeProcessor


def test_attributes_hash_deterministic_order():
    attrs1 = {"id": "value", "class": "foo"}
    attrs2 = {"class": "foo", "id": "value"}
    hash1 = HistoryTreeProcessor._attributes_hash(attrs1)
    hash2 = HistoryTreeProcessor._attributes_hash(attrs2)
    assert hash1 == hash2
