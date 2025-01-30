class DevelopmentalAgent:
    def __init__(self):
        self.stage = "sensorimotor"
    
    def learn(self):
        print(f"Learning in {self.stage} stage...")

if __name__ == "__main__":
    agent = DevelopmentalAgent()
    agent.learn()
