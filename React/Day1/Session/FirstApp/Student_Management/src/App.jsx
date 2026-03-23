import React, { useState } from "react";
import AddStudent from "./components/AddStudent";
import StudentList from "./components/StudentList";

function App() {
  const [students, setStudents] = useState([
    { name: "Alice", marks: 85 },
    { name: "Bob", marks: 90 }
  ]);

  const [editingIndex, setEditingIndex] = useState(null);

  // Add student
  const addStudent = (newStudent) => {
    setStudents([...students, newStudent]);
  };

  // Delete student
  const deleteStudent = (index) => {
    const updated = students.filter((_, i) => i !== index);
    setStudents(updated);
  };

  // Set student for editing
  const editStudent = (student, index) => {
    setEditingIndex(index);
  };

  // Update student
  const updateStudent = (updatedStudent) => {
    const updatedList = students.map((student, index) =>
      index === editingIndex ? updatedStudent : student
    );

    setStudents(updatedList);
    setEditingIndex(null);
  };

  return (
    <div>
      <h2>Student Dashboard</h2>

      <AddStudent
        onAddStudent={addStudent}
        editingStudent={students[editingIndex]}
        updateStudent={updateStudent}
      />

      <h3>Total Students: {students.length}</h3>

      <StudentList
        students={students}
        onDelete={deleteStudent}
        onEdit={editStudent}
      />
    </div>
  );
}

export default App;