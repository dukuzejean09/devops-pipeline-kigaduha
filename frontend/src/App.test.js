import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';
import { AuthProvider } from './AuthContext';

test('renders task management heading', () => {
  render(
    <AuthProvider>
      <App />
    </AuthProvider>
  );
  const heading = screen.getByText(/Task Management App/i);
  expect(heading).toBeInTheDocument();
});

test('renders create new task section', () => {
  render(
    <AuthProvider>
      <App />
    </AuthProvider>
  );
  const createSection = screen.getByText(/Add New Task/i);
  expect(createSection).toBeInTheDocument();
});
