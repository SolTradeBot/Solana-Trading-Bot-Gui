import React from 'react';
import { Play, Pause, Settings } from 'lucide-react';

interface StrategyCardProps {
  name: string;
  status: 'active' | 'paused';
  profit: number;
  trades: number;
  winRate: number;
}

export function StrategyCard({ name, status, profit, trades, winRate }: StrategyCardProps) {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold text-gray-800">{name}</h3>
        <div className="flex space-x-2">
          {status === 'active' ? (
            <button className="p-2 text-red-500 hover:bg-red-50 rounded-lg">
              <Pause className="w-4 h-4" />
            </button>
          ) : (
            <button className="p-2 text-green-500 hover:bg-green-50 rounded-lg">
              <Play className="w-4 h-4" />
            </button>
          )}
          <button className="p-2 text-gray-500 hover:bg-gray-50 rounded-lg">
            <Settings className="w-4 h-4" />
          </button>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-4 text-sm">
        <div>
          <p className="text-gray-500">Profit</p>
          <p className={`font-semibold ${profit >= 0 ? 'text-green-500' : 'text-red-500'}`}>
            {profit >= 0 ? '+' : ''}{profit}%
          </p>
        </div>
        <div>
          <p className="text-gray-500">Trades</p>
          <p className="font-semibold">{trades}</p>
        </div>
        <div>
          <p className="text-gray-500">Win Rate</p>
          <p className="font-semibold">{winRate}%</p>
        </div>
      </div>
    </div>
  );
}