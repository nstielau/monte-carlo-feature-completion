from typing import List

class SimulationResult:
    def __init__(self, num_successful=0, num_unsuccessful=0, total_simulations=0,
                 total_durations: List[float] = None):
        self.num_successful = num_successful
        self.num_unsuccessful = num_unsuccessful
        self.total_simulations = total_simulations
        self.total_durations = total_durations if total_durations is not None else []

    @property
    def success_rate(self):
        if self.total_simulations == 0:
            return 0
        return (self.num_successful / self.total_simulations) * 100

    def update(self, duration, desired_completion_duration):
        self.total_simulations += 1
        self.total_durations.append(duration)
        if duration < desired_completion_duration:
            self.num_successful += 1
        else:
            self.num_unsuccessful += 1

    @property
    def average_completion_duration(self):
        return sum(self.total_durations) / self.total_simulations if self.total_simulations > 0 else 0

    @property
    def median_completion_duration(self):
        sorted_durations = sorted(self.total_durations)
        mid = self.total_simulations // 2
        if self.total_simulations % 2 == 0:
            return (sorted_durations[mid - 1] + sorted_durations[mid]) / 2
        else:
            return sorted_durations[mid]

    @property
    def min_completion_duration(self):
        return min(self.total_durations) if self.total_durations else 0

    @property
    def max_completion_duration(self):
        return max(self.total_durations) if self.total_durations else 0
