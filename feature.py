from story import Story

import yaml
from story import Story

class Feature:
    @staticmethod
    def from_yaml(yaml_file, teams):
        with open(yaml_file, 'r') as file:
            features_data = yaml.safe_load(file)
            features = []
            for feature_data in features_data:
                stories = []
                for story_data in feature_data['stories']:
                    team = next((team for team in teams if team.name == story_data['team']), None)
                    if team:
                        stories.append(Story(name=story_data['name'], team=team))
                features.append(Feature(name=feature_data['name'], stories=stories))
            return features
    def __init__(self, name, stories=None):
        self.name = name
        self.stories = stories if stories is not None else []

    def add_story(self, story):
        if isinstance(story, Story):
            self.stories.append(story)

    def get_stories_by_team(self, team_name):
        return [story for story in self.stories if story.team.name == team_name]
