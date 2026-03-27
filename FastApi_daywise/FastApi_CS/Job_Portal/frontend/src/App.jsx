import React, { useState, useEffect } from 'react';
import {  Routes, Route } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import Register from './components/Register';
import Login from './components/Login';
import AdminDashboard from './components/AdminDashboard';
import UserDashboard from './components/UserDashboard';
import NavbarAdmin from './components/NavbarAdmin';
import NavbarUser from './components/NavbarUser';
import AddJob from './components/AddJob';
import JobList from './components/JobList';
import JobDetail from './components/JobDetail';
import AddUser from './components/AddUser';
import UserList from './components/UserList';
import UserDetail from './components/UserDetail';
import ApplyJob from './components/ApplyJob';
import Applications from './components/Applications';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  // Auth state: check localStorage for persistence
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    return localStorage.getItem('isAuthenticated') === 'true';
  });
  const [role, setRole] = useState(() => {
    return localStorage.getItem('role') || '';
  });

  // Update localStorage when auth state changes
  useEffect(() => {
    localStorage.setItem('isAuthenticated', isAuthenticated);
    localStorage.setItem('role', role);
  }, [isAuthenticated, role]);

  // Function to update auth state after login
  const setAuth = (auth, userRole) => {
    setIsAuthenticated(auth);
    setRole(userRole);
  };

  return (
    <>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login setAuth={setAuth} />} />
        <Route path="/admin-dashboard" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="admin">
            <>
              <NavbarAdmin />
              <AdminDashboard />
            </>
          </ProtectedRoute>
        } />
        <Route path="/user-dashboard" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="user">
            <>
              <NavbarUser />
              <UserDashboard />
            </>
          </ProtectedRoute>
        } />
        <Route path="/addjob" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="admin">
            <>
              <NavbarAdmin />
              <AddJob />
            </>
          </ProtectedRoute>
        } />
        <Route path="/jobs" element={
          <ProtectedRoute isAuthenticated={isAuthenticated}>
            <>
              {role === 'admin' ? <NavbarAdmin /> : <NavbarUser />}
              <JobList />
            </>
          </ProtectedRoute>
        } />
        <Route path="/jobs/:id" element={
          <ProtectedRoute isAuthenticated={isAuthenticated}>
            <>
              {role === 'admin' ? <NavbarAdmin /> : <NavbarUser />}
              <JobDetail />
            </>
          </ProtectedRoute>
        } />
        <Route path="/adduser" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="admin">
            <>
              <NavbarAdmin />
              <AddUser />
            </>
          </ProtectedRoute>
        } />
        <Route path="/users" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="admin">
            <>
              <NavbarAdmin />
              <UserList />
            </>
          </ProtectedRoute>
        } />
        <Route path="/users/:id" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="admin">
            <>
              <NavbarAdmin />
              <UserDetail />
            </>
          </ProtectedRoute>
        } />
        <Route path="/applyjob/:id" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="user">
            <>
              <NavbarUser />
              <ApplyJob />
            </>
          </ProtectedRoute>
        } />
        <Route path="/applications" element={
          <ProtectedRoute isAuthenticated={isAuthenticated} role={role} requiredRole="user">
            <>
              <NavbarUser />
              <Applications />
            </>
          </ProtectedRoute>
        } />
      </Routes>
    </>
  );
}

export default App;
