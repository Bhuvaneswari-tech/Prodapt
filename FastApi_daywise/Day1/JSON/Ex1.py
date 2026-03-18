import json

student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"],
    "is_graduated": False
}

print('Python Dictionary Values:')
print(student)

#json.dumps()   → Python dict  →  JSON string
json_str = json.dumps(student)
print('JSON String value:')
print(json_str)

# Pretty print with indentation
print('JSON with indentation:')
print(json.dumps(student, indent=2))


print(type(json_str))

#json.loads()   → JSON string  →  Python dict
print('Convert back into dictionary:')
print(json.loads(json_str))