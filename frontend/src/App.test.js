import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome message', () => {
  render(<App />);
  const heading = screen.getByText(/DevOps Pipeline Application/i);
  expect(heading).toBeInTheDocument();
});

test('renders content section', () => {
  render(<App />);
  const content = screen.getByText(/Frontend is running successfully!/i);
  expect(content).toBeInTheDocument();
});
