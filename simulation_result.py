class SimulationResult:
    def __init__(self, num_successful, num_unsuccessful, total_simulations, 
                 average_completion_duration, median_completion_duration, 
                 min_completion_duration, max_completion_duration):
        self.num_successful = num_successful
        self.num_unsuccessful = num_unsuccessful
        self.total_simulations = total_simulations
        self.average_completion_duration = average_completion_duration
        self.median_completion_duration = median_completion_duration
        self.min_completion_duration = min_completion_duration
        self.max_completion_duration = max_completion_duration
