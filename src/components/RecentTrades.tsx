import React from 'react';
import { ArrowUpRight, ArrowDownRight } from 'lucide-react';

export function RecentTrades() {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <h2 className="text-lg font-semibold text-gray-800 mb-4">Recent Trades</h2>
      <div className="space-y-4">
        {[
          { pair: 'SOL/USDT', type: 'buy', price: 103.45, profit: 2.3, strategy: 'Momentum' },
          { pair: 'SOL/USDT', type: 'sell', price: 102.80, profit: -1.2, strategy: 'Mean Reversion' },
          { pair: 'SOL/USDT', type: 'buy', price: 101.90, profit: 1.8, strategy: 'Volume Spike' },
        ].map((trade, i) => (
          <div key={i} className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              {trade.profit >= 0 ? (
                <ArrowUpRight className="w-5 h-5 text-green-500" />
              ) : (
                <ArrowDownRight className="w-5 h-5 text-red-500" />
              )}
              <div>
                <p className="font-medium">{trade.pair}</p>
                <p className="text-sm text-gray-500">{trade.strategy}</p>
              </div>
            </div>
            <div className="text-right">
              <p className="font-medium">${trade.price}</p>
              <p className={`text-sm ${trade.profit >= 0 ? 'text-green-500' : 'text-red-500'}`}>
                {trade.profit >= 0 ? '+' : ''}{trade.profit}%
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}