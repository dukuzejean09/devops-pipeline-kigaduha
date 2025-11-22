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

test('renders task form section', () => {
  render(
    <AuthProvider>
      <App />
    </AuthProvider>
  );
  // Test for the form inputs instead of heading text
  const titleInput = screen.getByPlaceholderText(/task title/i);
  const descriptionInput = screen.getByPlaceholderText(/task description/i);
  const submitButton = screen.getByRole('button', { name: /add task/i });

  expect(titleInput).toBeInTheDocument();
  expect(descriptionInput).toBeInTheDocument();
  expect(submitButton).toBeInTheDocument();
});
