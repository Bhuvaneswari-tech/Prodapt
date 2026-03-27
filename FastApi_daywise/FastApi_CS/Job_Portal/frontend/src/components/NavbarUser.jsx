import React from 'react';
import { Link, useNavigate } from 'react-router-dom';



const NavbarUser = () => {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem('isAuthenticated');
    localStorage.removeItem('role');
    localStorage.removeItem('userId');
    navigate('/');
    window.location.reload(); // Ensures state is reset
  };
  return (
    <nav>
      <h3>Job Portal User</h3>
      <Link to="/user-dashboard">Dashboard</Link> |
      <span>Applied Job</span> |
      <Link to="/jobs">View Jobs</Link> |
      <button onClick={handleLogout} style={{border: 'none', background: 'none', color: 'blue', cursor: 'pointer', textDecoration: 'underline', padding: 0}}>Logout</button>
    </nav>
  );
};

export default NavbarUser;
