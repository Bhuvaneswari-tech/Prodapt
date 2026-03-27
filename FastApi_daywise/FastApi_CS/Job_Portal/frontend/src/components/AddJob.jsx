
import React, { useState } from 'react';
import axios from 'axios';

const AddJob = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/jobs/', {
        title,
        description,
        location
      });
      setMessage('Job added successfully!');
      setTitle('');
      setDescription('');
      setLocation('');
    // eslint-disable-next-line no-unused-vars
    } catch (error) {
      setMessage('Error adding job.');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Add Job</h2>
      <form onSubmit={handleSubmit} className="border p-4 rounded bg-light">
        <div className="mb-3">
          <label className="form-label">Title</label>
          <input type="text" className="form-control" value={title} onChange={e => setTitle(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label className="form-label">Description</label>
          <textarea className="form-control" value={description} onChange={e => setDescription(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label className="form-label">Location</label>
          <input type="text" className="form-control" value={location} onChange={e => setLocation(e.target.value)} required />
        </div>
        <button type="submit" className="btn btn-primary">Add Job</button>
      </form>
      {message && <div className="alert alert-info mt-3">{message}</div>}
    </div>
  );
};

export default AddJob;
