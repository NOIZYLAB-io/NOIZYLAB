"""NoizySynth UI Generator"""
def generate_ui(prompt):
    return f'''import React from 'react';

export default function Generated() {{
  return (
    <div className="p-4 bg-gradient-to-r from-yellow-500 to-orange-500 text-black rounded-xl">
      <h2 className="text-xl font-bold">{prompt}</h2>
      <p>Auto-generated component</p>
    </div>
  );
}}'''

