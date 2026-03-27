import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Applications = () => {
  const [applications, setApplications] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchApplications = async () => {
      try {
        const response = await axios.get('http://localhost:8000/applications/');
        setApplications(response.data);
      } catch (err) {
        setError('Failed to fetch applications');
      } finally {
        setLoading(false);
      }
    };
    fetchApplications();
  }, []);

  return (
    <div className="container mt-4">
      <h2>Applications</h2>
      {loading && <div>Loading...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      <table className="table table-striped mt-3">
        <thead>
          <tr>
            <th>Application ID</th>
            <th>Job ID</th>
            <th>User ID</th>
          </tr>
        </thead>
        <tbody>
          {applications.map(app => (
            <tr key={app.id}>
              <td>{app.id}</td>
              <td>{app.job_id}</td>
              <td>{app.user_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Applications;
