import yaml

class Team:
    @staticmethod
    def from_yaml(yaml_file):
        with open(yaml_file, 'r') as file:
            teams_data = yaml.safe_load(file)
            return [Team(**data) for data in teams_data]
    def __init__(self, name, min_time, max_time, avg_time):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.avg_time = avg_time
