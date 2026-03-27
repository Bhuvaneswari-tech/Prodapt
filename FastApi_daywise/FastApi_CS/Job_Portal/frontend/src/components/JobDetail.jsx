import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const JobDetail = () => {
  const { id } = useParams();
  const [job, setJob] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchJob = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/jobs/${id}`);
        setJob(response.data);
      } catch (err) {
        setError('Failed to fetch job');
      } finally {
        setLoading(false);
      }
    };
    fetchJob();
  }, [id]);

  return (
    <div className="container mt-4">
      <h2>Job Detail</h2>
      {loading && <div>Loading...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      {job && (
        <div className="card p-3">
          <h4>{job.title}</h4>
          <p><strong>Description:</strong> {job.description}</p>
          <p><strong>Location:</strong> {job.location}</p>
        </div>
      )}
    </div>
  );
};

export default JobDetail;
