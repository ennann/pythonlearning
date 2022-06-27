import json

obj = """
{"name": "Wes",
  "places_lived": ["United States", "Spain", "Germany"],
  "pet": null,
  "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                {"name": "Katie", "age": 38,
                "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

result = json.loads(obj)
print(result)

asjson = json.dumps(result)
print(asjson)
