from datetime import datetime

class Round:
    def __init__(self, name, start_date, end_date, matches=None, status=""):
        self.name = name
        self.start_date = start_date or datetime.now().strftime("%Y-%m-%d")
        self.end_date = end_date
        self.matches = matches or []
        self.status = status


    def serialize(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.serialize()  for match in self.matches],
            "status": self.status
        }
    

 


