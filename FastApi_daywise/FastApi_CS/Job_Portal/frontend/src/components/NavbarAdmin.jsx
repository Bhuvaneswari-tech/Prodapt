import React from 'react';
import { Link } from 'react-router-dom';


const NavbarAdmin = () => (
  <nav>
    <h3>Job Portal Admin</h3>
    <Link to="/admin-dashboard">Dashboard</Link> |
    <Link to="/addjob">Add Job</Link> |
    <Link to="/jobs">Job List</Link> |
    <Link to="/users">View Users</Link> |
    <Link to="/applications">Applications</Link>
  </nav>
);

export default NavbarAdmin;
