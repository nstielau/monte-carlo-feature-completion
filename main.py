import random
import time

import fire

from rich.console import Console
from rich.live import Live
from rich.table import Table
from feature import Feature
from simulation_result import SimulationResult
from story import Story
from team import Team


results = {}
features = []

def monte_carlo_simulation(feature, desired_completion_duration, num_simulations=1000):
    total_duration = 0
    for story in feature.stories:
        duration = random.uniform(story.team.min_time, story.team.max_time)
        total_duration += duration
    return total_duration

def generate_table(features, results):
    table = Table(title="Simulation Results")
    table.add_column("Feature", justify="right", style="cyan", no_wrap=True)
    table.add_column("Success Rate (%)", style="green")
    table.add_column("Simulations Completed", style="magenta")
    table.add_column("Last Simulation Duration", style="yellow")
    table.add_column("Average Duration", style="yellow")
    table.add_column("Min Duration", style="yellow")
    table.add_column("Max Duration", style="yellow")

    for feature in features:
        result = results[feature.name]
        table.add_row(
            feature.name,
            f"{result.success_rate:.2f}",
            f"{result.total_simulations}",
            f"{result.total_durations[-1]:.2f}" if result.total_durations else "N/A",
            f"{result.average_completion_duration:.2f}",
            f"{result.min_completion_duration:.2f}",
            f"{result.max_completion_duration:.2f}"
        )

    return table

def main(desired_duration=10, num_simulations=1000):
    # Load teams and features from YAML fixtures
    teams = Team.from_yaml('fixtures/teams.yaml')
    features = sorted(Feature.from_yaml('fixtures/features.yaml', teams), key=lambda f: f.rank, reverse=True)

    # Setup
    for feature in features:
        results[feature.name] = SimulationResult()

        # Run the first simulation
        result = results[feature.name]
        total_duration = monte_carlo_simulation(feature, desired_duration)
        result.update(total_duration, desired_duration)

    # Print additional simulation information
    console = Console()
    with Live(generate_table(features, results), console=console, refresh_per_second=4) as live:
        for _ in range(num_simulations-1):
            for feature in features:
                result = results[feature.name]
                total_duration = monte_carlo_simulation(feature, desired_duration)
                result.update(total_duration, desired_duration)
            live.update(generate_table(features, results))
            #time.sleep(2)

if __name__ == "__main__":
    fire.Fire(main)
