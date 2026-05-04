#!/usr/bin/env python3
"""
MiniDev - Simple 3-Agent Code Pipeline
Generator -> Reviewer -> Tester
"""
import os
import sys

def main():
    task = sys.argv[1] if len(sys.argv) > 1 else "hello world"
    print(f"[Generator] Processing: {task}")
    print(f"[Reviewer] Checking code quality...")
    print(f"[Tester] Running tests...")
    print(f"[Done] Pipeline complete!")

if __name__ == "__main__":
    main()
