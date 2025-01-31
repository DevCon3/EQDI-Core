class SkillMarketplace:
    def __init__(self):
        self.skills = {}
        self.transactions = []
        
    def register_skill(self, agent_id: str, skill: str, cost: float):
        """List a skill in the marketplace"""
        self.skills[agent_id] = {"skill": skill, "cost": cost}
        
    def execute_transaction(self, buyer: str, seller: str):
        """Handle skill exchange"""
        if seller in self.skills:
            self.transactions.append({
                "buyer": buyer,
                "seller": seller,
                "skill": self.skills[seller]["skill"],
                "cost": self.skills[seller]["cost"]
            })
            return True
        return False
