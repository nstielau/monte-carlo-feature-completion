import random
import fire
from feature import Feature
from simulation_result import SimulationResult
from story import Story
from team import Team

def monte_carlo_simulation(feature, desired_completion_duration, num_simulations=1000):
    total_durations = []
    for _ in range(num_simulations):
        total_duration = 0
        for story in feature.stories:
            # Simulate a random duration based on the team's min and max time
            duration = random.uniform(story.team.min_time, story.team.max_time)
            total_duration += duration
        total_durations.append(total_duration)
    num_successful = sum(1 for duration in total_durations if duration < desired_completion_duration)
    num_unsuccessful = num_simulations - num_successful
    average_completion_duration = sum(total_durations) / num_simulations
    median_completion_duration = sorted(total_durations)[num_simulations // 2]
    min_completion_duration = min(total_durations)
    max_completion_duration = max(total_durations)

    return SimulationResult(
        num_successful=num_successful,
        num_unsuccessful=num_unsuccessful,
        total_simulations=num_simulations,
        average_completion_duration=average_completion_duration,
        median_completion_duration=median_completion_duration,
        min_completion_duration=min_completion_duration,
        max_completion_duration=max_completion_duration
    )

def main(desired_duration=10, num_simulations=1000):
    # Load teams and features from YAML fixtures
    teams = Team.from_yaml('fixtures/teams.yaml')
    features = Feature.from_yaml('fixtures/features.yaml', teams)

    # Run simulations

    for feature in features:
        result = monte_carlo_simulation(feature, desired_duration, num_simulations)
        print(f"Results for {feature.name}:")
        print(f"  Desired completion time: {desired_duration}")
        print(f"  Success rate: {result.num_successful / result.total_simulations * 100:.2f}%")
        print(f"  Average duration: {result.average_completion_duration:.2f}")
        print(f"  Median duration: {result.median_completion_duration:.2f}")
        print(f"  Min duration: {result.min_completion_duration:.2f}")
        print(f"  Max duration: {result.max_completion_duration:.2f}")

if __name__ == "__main__":
    fire.Fire(main)
