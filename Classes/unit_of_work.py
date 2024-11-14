from datetime import datetime

class UnitOfWork:
    def __init__(self):
        self.history = []

    def record_query(self, query, result):
        self.history.append({"timestamp": datetime.now(), "query": query, "result": result})

    def get_history(self):
        return self.history
