import React, { useState, useEffect } from "react";

function AddStudent({ onAddStudent, editingStudent, updateStudent }) {
  const [name, setName] = useState("");
  const [marks, setMarks] = useState("");

  // Fill form when editing
  useEffect(() => {
    if (editingStudent) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setName(editingStudent.name);
      setMarks(editingStudent.marks);
    }
  }, [editingStudent]);

  const handleSubmit = () => {
    const student = {
      name,
      marks: Number(marks)
    };

    if (editingStudent) {
      updateStudent(student);
    } else {
      onAddStudent(student);
    }

    setName("");
    setMarks("");
  };

  return (
    <div>
      <h3>{editingStudent ? "Edit Student" : "Add Student"}</h3>

      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        type="number"
        placeholder="Marks"
        value={marks}
        onChange={(e) => setMarks(e.target.value)}
      />

      <button onClick={handleSubmit}>
        {editingStudent ? "Update" : "Add"}
      </button>
    </div>
  );
}

export default AddStudent;