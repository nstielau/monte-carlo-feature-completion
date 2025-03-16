from team import Team

class Story:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def get_estimated_duration(self):
        # This method could be expanded to use Monte Carlo simulation
        return (self.team.min_time + self.team.max_time) / 2
