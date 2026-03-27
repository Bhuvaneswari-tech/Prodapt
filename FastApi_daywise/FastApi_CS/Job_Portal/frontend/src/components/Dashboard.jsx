import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = ({ role }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        // Adjust endpoint as per your backend
        const response = await axios.get(`http://localhost:8000/dashboard/${role}`);
        setData(response.data);
      // eslint-disable-next-line no-unused-vars
      } catch (err) {
        setError('Failed to fetch dashboard data');
      } finally {
        setLoading(false);
      }
    };
    fetchDashboard();
  }, [role]);

  return (
    <div className="container mt-4">
      <h2>{role === 'admin' ? 'Admin' : 'User'} Dashboard</h2>
      {loading && <div>Loading...</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      {data && (
        <div className="card p-3 mt-3">
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
