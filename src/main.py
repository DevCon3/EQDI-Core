from eqdi.quantum_core import QuantumDevelopmentalUnit
from eqdi.energy_manager import EnergyHarvester, PowerAllocator
from eqdi.stage_manager import DevelopmentalStageController

def main():
    # Initialize components
    qdu = QuantumDevelopmentalUnit()
    harvester = EnergyHarvester()
    allocator = PowerAllocator()
    stage_controller = DevelopmentalStageController()
    
    # Developmental loop
    while not stage_controller.is_final_stage():
        harvester.update_readings()
        power_budget = harvester.solar_power + harvester.vibration_power
        allocations = allocator.dynamic_allocate(power_budget)
        
        qdu.entangle_weights()
        validation = qdu.validate_stage()
        stage_controller.advance_stage(validation)
        
        print(f"Stage: {stage_controller.current_stage_name()}")
        print(f"Power Allocations: {allocations}")

if __name__ == "__main__":
    main()
