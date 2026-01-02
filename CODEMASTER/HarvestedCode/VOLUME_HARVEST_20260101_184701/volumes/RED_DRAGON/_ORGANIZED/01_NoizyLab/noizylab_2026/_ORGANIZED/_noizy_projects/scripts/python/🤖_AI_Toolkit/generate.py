#!/usr/bin/env python3
"""
Distributed Text Generation Script
Example script for torchrun distributed processing
"""

import torch
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
import os
import argparse
from datetime import datetime

def setup(rank, world_size):
    """Initialize the distributed environment."""
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    
    # Initialize the process group
    dist.init_process_group("nccl" if torch.cuda.is_available() else "gloo", 
                           rank=rank, world_size=world_size)

def cleanup():
    """Clean up the distributed environment."""
    dist.destroy_process_group()

class SimpleGenerator(torch.nn.Module):
    """Simple text/sequence generator model"""
    def __init__(self, vocab_size=1000, embed_dim=256, hidden_dim=512):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embed_dim)
        self.lstm = torch.nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.output = torch.nn.Linear(hidden_dim, vocab_size)
        
    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        output = self.output(lstm_out)
        return output

def generate_sequences(rank, world_size, args):
    """Generate sequences using distributed processing"""
    print(f"Running on rank {rank}/{world_size}")
    
    # Setup distributed processing
    setup(rank, world_size)
    
    # Create model
    device = torch.device(f"cuda:{rank}" if torch.cuda.is_available() else "cpu")
    model = SimpleGenerator(
        vocab_size=args.vocab_size,
        embed_dim=args.embed_dim,
        hidden_dim=args.hidden_dim
    ).to(device)
    
    # Wrap model with DDP
    if torch.cuda.is_available():
        model = DDP(model, device_ids=[rank])
    else:
        model = DDP(model)
    
    # Generate some sample sequences
    model.eval()
    with torch.no_grad():
        # Create random input sequences
        batch_size = args.batch_size // world_size  # Distribute batch across processes
        seq_length = args.seq_length
        
        input_ids = torch.randint(0, args.vocab_size, (batch_size, seq_length)).to(device)
        
        print(f"Rank {rank}: Generating {batch_size} sequences of length {seq_length}")
        
        # Generate outputs
        outputs = model(input_ids)
        generated_ids = torch.argmax(outputs, dim=-1)
        
        # Save results for this rank
        output_file = f"generated_rank_{rank}.pt"
        torch.save({
            'rank': rank,
            'input_ids': input_ids.cpu(),
            'generated_ids': generated_ids.cpu(),
            'timestamp': datetime.now().isoformat()
        }, output_file)
        
        print(f"Rank {rank}: Saved results to {output_file}")
        print(f"Rank {rank}: Generated shape: {generated_ids.shape}")
    
    # Cleanup
    cleanup()

def main():
    parser = argparse.ArgumentParser(description='Distributed Generation Script')
    parser.add_argument('--vocab_size', type=int, default=1000, help='Vocabulary size')
    parser.add_argument('--embed_dim', type=int, default=256, help='Embedding dimension')
    parser.add_argument('--hidden_dim', type=int, default=512, help='Hidden dimension')
    parser.add_argument('--batch_size', type=int, default=32, help='Total batch size')
    parser.add_argument('--seq_length', type=int, default=128, help='Sequence length')
    parser.add_argument('--output_dir', type=str, default='./outputs', help='Output directory')
    
    args = parser.parse_args()
    
    # Get distributed info from torchrun
    rank = int(os.environ.get("RANK", 0))
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    
    print(f"Starting generation on rank {rank}/{world_size} (local_rank: {local_rank})")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Run generation
    generate_sequences(rank, world_size, args)
    
    # If rank 0, collect and summarize results
    if rank == 0:
        print("\n" + "="*60)
        print("DISTRIBUTED GENERATION COMPLETE")
        print("="*60)
        
        total_files = 0
        for r in range(world_size):
            file_path = f"generated_rank_{r}.pt"
            if os.path.exists(file_path):
                data = torch.load(file_path)
                total_files += 1
                print(f"Rank {r}: Generated {data['generated_ids'].shape[0]} sequences")
        
        print(f"\nTotal ranks completed: {total_files}/{world_size}")
        print("Generated files:")
        for r in range(world_size):
            file_path = f"generated_rank_{r}.pt"
            if os.path.exists(file_path):
                print(f"  - {file_path}")

if __name__ == "__main__":
    main()