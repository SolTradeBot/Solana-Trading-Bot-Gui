import React from 'react';
import { LineChart, TrendingUp } from 'lucide-react';

export function PriceChart() {
  return (
    <div className="relative h-64 flex items-center justify-center">
      <div className="absolute inset-0 flex items-center justify-center">
        <LineChart className="w-12 h-12 text-gray-300" />
      </div>
      <div className="absolute bottom-4 right-4 flex items-center text-green-500">
        <TrendingUp className="w-4 h-4 mr-1" />
        <span className="text-sm font-medium">+2.45%</span>
      </div>
    </div>
  );
}