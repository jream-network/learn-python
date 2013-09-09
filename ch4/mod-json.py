# JSON - JavaScript Object Notation
# Think of this as Serialization (Compacting Data)
import json
"""
@Example:
    Array
    ------
    [1, "dog", "cat"]

    Object
    ------
    {
        "key": "value",
        "name": "teddy"
    }
"""

data = """
{
    "name": "Jesse",
    "age": 28,
    "hobbies": [
        "programming",
        "guitar"
    ]
}
"""

# Turns a String into an Object (In Py)
# Incoming Data
loaded = json.loads(data)
print loaded
print loaded["age"]
print loaded["hobbies"][0]

data = {
    "color": "red",
    "rainbow": True
}

# Turns an Object into a String (In Py)
# Outgoing Data
output = json.dumps(data)
print output

