import React, { useState, useEffect } from 'react';
import axios from 'axios';

import { useParams, useNavigate } from 'react-router-dom';

const ApplyJob = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [job, setJob] = useState(null);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (!id) {
      setMessage('No job ID provided.');
      setLoading(false);
      return;
    }
    const fetchJob = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/jobs/${id}`);
        setJob(response.data);
      // eslint-disable-next-line no-unused-vars
      } catch (err) {
        setMessage('Failed to fetch job details.');
      } finally {
        setLoading(false);
      }
    };
    fetchJob();
  }, [id]);

  const handleApply = async () => {
    try {
      // You may want to get userId from auth context or localStorage
      // For now, assume userId is available as localStorage.getItem('userId')
      const userId = localStorage.getItem('userId');
      const payload = {
        job_id: Number(id),
        user_id: Number(userId)
      };
      console.log('Submitting application:', payload);
      await axios.post('http://localhost:8000/applications/', payload);
      setMessage('Applied to job successfully!');
      setTimeout(() => {
        navigate('/applications');
      }, 1000);
    // eslint-disable-next-line no-unused-vars
    } catch (error) {
      setMessage('Error applying to job.');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Apply Job</h2>
      {loading && <div>Loading...</div>}
      {message && <div className="alert alert-info mt-3">{message}</div>}
      {!loading && !id && (
        <div className="alert alert-warning mt-3">No job ID provided in the URL.</div>
      )}
      {job && (
        <div className="card p-3">
          <h4>{job.title}</h4>
          <p><strong>Description:</strong> {job.description}</p>
          <button className="btn btn-primary" onClick={handleApply}>Apply</button>
        </div>
      )}
    </div>
  );
};

export default ApplyJob;
