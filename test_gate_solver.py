import unittest
from unittest.mock import MagicMock, mock_open, patch

from .gate_solver import GateSolver


def test_get_gates_from_file():
    with patch("builtins.open",
            mock_open(read_data="lw AND lz -> a"),
            create=False):
        solver = GateSolver("fake_file_name")
        gates = solver.get_gates_from_file()
        assert gates == {"a": ["lw", "AND", "lz"]}

def test_get_wire_short():
    solver = GateSolver("fake_file_name")
    solver.get_gates_from_file = MagicMock()
    solver.get_gates_from_file.return_value = {}

    wire = solver.get_wire("a")
    assert wire is None

    solver.get_gates_from_file.return_value = {"a": ["lw", "AND", "lz"]}
    wire = solver.get_wire("42")
    assert wire == 42


def test_get_wire_full():
    solver = GateSolver("fake_file_name")
    solver.get_gates_from_file = MagicMock()
    solver.get_gates_from_file.return_value = {"a": ["42"]}
    wire = solver.get_wire("a")
    assert solver.wire_outputs == {"a": 42}
