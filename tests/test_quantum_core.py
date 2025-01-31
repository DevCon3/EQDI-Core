import pytest
from src.eqdi.quantum_core import QuantumDevelopmentalUnit

@pytest.fixture
def qdu():
    return QuantumDevelopmentalUnit(qubits=4)

def test_sensorimotor_entanglement(qdu):
    qdu.entangle_weights()
    assert qdu.circuit.depth() == 2, "Should create basic entanglement"

def test_stage_validation(qdu):
    qdu.stage = "formal_operational"
    qdu.entangle_weights()
    assert qdu.validate_stage(), "Should pass formal stage validation"
