import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

test('renders task management heading', () => {
  render(<App />);
  const heading = screen.getByText(/Task Management App/i);
  expect(heading).toBeInTheDocument();
});

test('renders create new task section', () => {
  render(<App />);
  const createSection = screen.getByText(/Create New Task/i);
  expect(createSection).toBeInTheDocument();
});
