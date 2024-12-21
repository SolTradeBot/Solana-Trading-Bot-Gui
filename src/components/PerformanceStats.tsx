import React from 'react';
import { DollarSign, TrendingUp, Activity, Clock } from 'lucide-react';

export function PerformanceStats() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-500">Total Profit</p>
            <p className="text-2xl font-bold text-green-500">+$12,458</p>
          </div>
          <DollarSign className="w-8 h-8 text-green-500" />
        </div>
      </div>
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-500">Win Rate</p>
            <p className="text-2xl font-bold text-gray-900">68.5%</p>
          </div>
          <TrendingUp className="w-8 h-8 text-purple-500" />
        </div>
      </div>
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-500">Active Trades</p>
            <p className="text-2xl font-bold text-gray-900">14</p>
          </div>
          <Activity className="w-8 h-8 text-blue-500" />
        </div>
      </div>
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-500">Uptime</p>
            <p className="text-2xl font-bold text-gray-900">15d 4h</p>
          </div>
          <Clock className="w-8 h-8 text-orange-500" />
        </div>
      </div>
    </div>
  );
}