import yaml
import os

def load_lesson(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def validate_lesson(lesson, schema_path):
    import jsonschema
    import json
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)
    jsonschema.validate(instance=lesson, schema=schema)

if __name__ == "__main__":
    lesson = load_lesson('../courses/vocal_gain_air_v1.yaml')
    print("Lesson loaded:", lesson['title'])
    validate_lesson(lesson, '../schemas/lesson_schema.yaml')
    print("Lesson validated!")
