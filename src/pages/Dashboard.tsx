import React from 'react';
import { Bot, Settings } from 'lucide-react';
import { PerformanceStats } from '../components/PerformanceStats';
import { StrategyCard } from '../components/StrategyCard';
import { RecentTrades } from '../components/RecentTrades';

const strategies = [
  { name: 'Volume Spike', status: 'active', profit: 12.5, trades: 45, winRate: 67 },
  { name: 'Scalping', status: 'active', profit: 8.3, trades: 128, winRate: 72 },
  { name: 'Reversal', status: 'paused', profit: -2.1, trades: 23, winRate: 48 },
  { name: 'Pair Trading', status: 'active', profit: 5.7, trades: 34, winRate: 65 },
  { name: 'News Sentiment', status: 'active', profit: 15.2, trades: 18, winRate: 78 },
  { name: 'Momentum', status: 'active', profit: 9.8, trades: 56, winRate: 70 },
  { name: 'Mean Reversion', status: 'paused', profit: 4.2, trades: 42, winRate: 62 },
  { name: 'Grid', status: 'active', profit: 7.5, trades: 89, winRate: 69 },
  { name: 'Breakout', status: 'active', profit: 11.3, trades: 37, winRate: 73 },
  { name: 'Arbitrage', status: 'active', profit: 6.4, trades: 94, winRate: 81 },
] as const;

export function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <Bot className="w-8 h-8 text-purple-600" />
              <h1 className="ml-2 text-xl font-bold text-gray-900">Sol Trade Bot Dashboard</h1>
            </div>
            <button className="p-2 text-gray-500 hover:bg-gray-50 rounded-lg">
              <Settings className="w-6 h-6" />
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <PerformanceStats />
        
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">Active Strategies</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {strategies.map((strategy) => (
              <StrategyCard key={strategy.name} {...strategy} />
            ))}
          </div>
        </div>

        <div className="mt-8">
          <RecentTrades />
        </div>
      </main>
    </div>
  );
}