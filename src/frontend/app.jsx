import React from 'react';
import { createRoot } from 'react-dom/client';

const App = () => {
    return (
        <div>
            <h1>Modular AI App Frontend</h1>
            <p>Ready for development.</p>
        </div>
    );
};

const root = createRoot(document.getElementById('root'));
root.render(<App />);
