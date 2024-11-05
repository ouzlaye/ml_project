import { render, screen } from '@testing-library/react';
import HomePage from './HomePage';

test('affiche le titre de la page', () => {
    render(<HomePage />);
    const titleElement = screen.getByText(/Bienvenue sur l'application de prédiction/i);
    expect(titleElement).toBeInTheDocument();
});
