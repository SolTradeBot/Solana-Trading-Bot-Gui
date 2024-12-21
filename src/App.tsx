import React, { useState } from 'react';
import { Dashboard } from './pages/Dashboard';
import { WalletConnect } from './pages/WalletConnect';

function App() {
  const [isConnected, setIsConnected] = useState(false);

  return isConnected ? <Dashboard /> : <WalletConnect />;
}

export default App;