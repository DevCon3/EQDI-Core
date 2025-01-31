class DevelopmentalStageController:
    STAGES = [
        "sensorimotor",
        "pre_operational", 
        "concrete_operational",
        "formal_operational"
    ]
    
    def __init__(self):
        self.current_stage = 0
        self.validation_history = []
        
    def advance_stage(self, validation_result: bool):
        """Progress to next stage if validated"""
        if validation_result and not self.is_final_stage():
            self.current_stage += 1
            
    def current_stage_name(self) -> str:
        return self.STAGES[self.current_stage]
    
    def is_final_stage(self) -> bool:
        return self.current_stage >= len(self.STAGES) - 1
