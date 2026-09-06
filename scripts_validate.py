name=scripts/validate.py
import json
import sys
from jsonschema import validate, ValidationError

def main():
    with open("species.json") as f:
        data = json.load(f)
    with open("schema.json") as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"Validation failed: {e.message}")
        sys.exit(1)

    print(f"OK: version={data['version']}, cards={len(data['species'])}")

if __name__ == "__main__":
    main()