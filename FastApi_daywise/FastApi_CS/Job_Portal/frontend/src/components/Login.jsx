import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = ({ setAuth }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Adjust endpoint and payload as per your backend
      const response = await axios.post('http://localhost:8000/users/login', {
        email,
        password
      });
      setMessage('Login successful!');
      setEmail('');
      setPassword('');
      // Save auth state globally
      const user = response.data;
      if (setAuth) {
        setAuth(true, user.role);
      }
      // Redirect based on role
      if (user.role === 'admin') {
        navigate('/admin-dashboard');
      } else {
        navigate('/user-dashboard');
      }
    // eslint-disable-next-line no-unused-vars
    } catch (error) {
      setMessage('Invalid credentials.');
      if (setAuth) {
        setAuth(false, '');
      }
    }
  };

  return (
    <div className="container mt-4">
      <h2>Login</h2>
      <form onSubmit={handleSubmit} className="border p-4 rounded bg-light">
        <div className="mb-3">
          <label className="form-label">Email</label>
          <input type="email" className="form-control" value={email} onChange={e => setEmail(e.target.value)} required />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input type="password" className="form-control" value={password} onChange={e => setPassword(e.target.value)} required />
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
      {message && <div className="alert alert-info mt-3">{message}</div>}
    </div>
  );
};

export default Login;
