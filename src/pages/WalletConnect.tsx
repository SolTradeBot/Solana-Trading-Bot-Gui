import React from 'react';
import { Bot, Wallet, Plus, Import } from 'lucide-react';
import { WalletButton } from '../components/WalletButton';

export function WalletConnect() {
  const handlePhantomConnect = () => {
    // Phantom wallet connection logic will go here
    console.log('Connecting to Phantom wallet...');
  };

  const handleCreateWallet = () => {
    // New wallet creation logic will go here
    console.log('Creating new wallet...');
  };

  const handleImportWallet = () => {
    // Wallet import logic will go here
    console.log('Importing wallet...');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center">
            <Bot className="w-8 h-8 text-purple-600" />
            <h1 className="ml-2 text-xl font-bold text-gray-900">Sol Trade Bot</h1>
          </div>
        </div>
      </header>

      <main className="max-w-lg mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-8">
          <h2 className="text-2xl font-bold text-gray-900">Connect Your Wallet</h2>
          <p className="mt-2 text-gray-600">Choose how you want to connect to start trading</p>
        </div>

        <div className="space-y-4">
          <WalletButton
            icon={<Wallet className="w-6 h-6 text-purple-600" />}
            title="Connect Wallet"
            description="Connect your existing Phantom wallet etc."
            onClick={handlePhantomConnect}
          />

          <WalletButton
            icon={<Plus className="w-6 h-6 text-purple-600" />}
            title="Create New Wallet"
            description="Generate a new wallet for trading"
            onClick={handleCreateWallet}
          />

          <WalletButton
            icon={<Import className="w-6 h-6 text-purple-600" />}
            title="Import Existing Wallet"
            description="Import using secret recovery phrase"
            onClick={handleImportWallet}
          />
        </div>

        <p className="mt-8 text-center text-sm text-gray-500">
          By connecting a wallet, you agree to our Terms of Service and Privacy Policy
        </p>
      </main>
    </div>
  );
}