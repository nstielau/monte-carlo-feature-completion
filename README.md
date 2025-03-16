# Monte Carlo Feature Completion

## Real-World Goal

The goal of this project is to simulate the completion times of various software features using a Monte Carlo simulation approach. This helps in predicting the likelihood of completing features within a desired timeframe, allowing project managers to make informed decisions about resource allocation and project timelines.

## Technical Details

This project uses a Monte Carlo simulation to estimate the completion duration of software features. Each feature consists of multiple stories, and each story is assigned to a team. The simulation uses the minimum and maximum time estimates for each team to generate random completion times for stories, which are then aggregated to determine the total completion time for each feature.

[![asciicast](https://asciinema.org/a/Hpskwf2ITzJBQsTgobq0Wfolx.svg)](https://asciinema.org/a/Hpskwf2ITzJBQsTgobq0Wfolx)


### Key Components

- **Teams**: Defined in `fixtures/teams.yaml`, each team has a minimum, maximum, and average time for completing a story.
- **Features**: Defined in `fixtures/features.yaml`, each feature consists of multiple stories, each assigned to a team.
- **Simulation**: The `monte_carlo_simulation` function in `main.py` runs the simulation for each feature, calculating the total duration based on random story completion times.
- **Results**: The simulation results are displayed in a table using the `rich` library, showing success rates and duration statistics.

### Example Fixtures

Here is an example of how a Team and a Feature are defined in the YAML fixtures:

#### Team Example

```yaml
- name: Team A
  min_time: 1
  max_time: 10
  avg_time: 5.5
```

#### Feature Example

```yaml
- name: FEAT-2345
  rank: 1
  stories:
    - name: Story 1
      team: Team A
    - name: Story 2
      team: Team B
```

### How to Run

To run the simulation, execute the `main.py` script. You can specify the desired completion duration and the number of simulations to run.

```bash
python main.py --desired_duration=10 --num_simulations=1000
```

### Dependencies

- Python 3.12
- PyYAML
- Rich
- Fire

Install dependencies using:

```bash
pip install -r requirements.txt
```
