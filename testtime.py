import json
from uuid import uuid4
from datetime import datetime

data = [{
    "id": str(uuid4()),
    "created_at": datetime.utcnow().isoformat(),
    "updated_at": datetime.utcnow().isoformat(),
    "__class__": "Place"
}]

json_str = json.dumps(data)
print(json_str)

