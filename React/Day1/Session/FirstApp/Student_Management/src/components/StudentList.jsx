import React from "react";

function StudentList({ students, onDelete, onEdit }) {
  return (
    <div>
      <h3>Student List</h3>

      {students.map((student, index) => (
        <div key={index}>
          <span>
            {student.name} - {student.marks}
          </span>

          <button onClick={() => onEdit(student, index)}>
            Edit
          </button>&nbsp;&nbsp;

          <button onClick={() => onDelete(index)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default StudentList;