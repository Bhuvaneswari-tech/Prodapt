Pydantic is a Python Library for:
Data Validation
Serialization
Parsing
Runtime type enforcement

pip install pydantic

Visual Understanding
❌ Without **
User(
   data = {
     id: 1,
     name: "Bhuvana",
     ...
   }
)
✅ With **
User(
   id=1,
   name="Bhuvana",
   age=30,
   email="bhuvana@example.com",
   address=[...]
)

BaseModel allows you to define structured data with type validation, parsing, and serialization.

@field_validator('salary') tells Pydantic:
“Run this function to validate the salary field before creating the object.”

@classmethod means:
“This method belongs to the class, not the instance”

Difference
@field_validator	Runs validation logic on a field
@classmethod	Makes method accessible at class level (no object needed)

cls → refers to the Employee class