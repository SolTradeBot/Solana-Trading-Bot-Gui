import React from 'react';
import { WalletIcon } from 'lucide-react';

interface WalletButtonProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  onClick: () => void;
}

export function WalletButton({ icon, title, description, onClick }: WalletButtonProps) {
  return (
    <button
      onClick={onClick}
      className="w-full p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow flex items-center space-x-4 border border-transparent hover:border-purple-100"
    >
      <div className="p-3 bg-purple-50 rounded-lg">
        {icon}
      </div>
      <div className="text-left">
        <h3 className="font-semibold text-gray-900">{title}</h3>
        <p className="text-sm text-gray-500">{description}</p>
      </div>
    </button>
  );
}