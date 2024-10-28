# Load spec
import json
from yaml import safe_load

with open("product.yml", "r", encoding="utf-8") as file:
    spec = safe_load(file)

# Export as JSON for evaluation
print(json.dumps(spec))