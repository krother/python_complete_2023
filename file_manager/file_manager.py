"""
we have some JSON files in a folder. We want to ...
  - check the number of lines in each file
  - move the files to a different folder
  - copy the files to a third folder
  - delete a file
  - check their size
"""
import json
import random


for name in ["deployment", "manifest", "application", "configuration"]:
    filename = name + "_config.json"
    content = {
        "software_version": random.randint(1, 100),
        "client_id": random.choice(["AAA", "BBB", "CCC"]),
        "container_id": str(random.random()),
        "module_list": [
            random.choice(list("abcdefghijk")) for i in range(10)
        ]
    }
    with open(filename, "w") as file:
        json.dump(content, file)
    
    
