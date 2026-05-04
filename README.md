# MiniDev

## Description

Simple 3-Agent Code Pipeline: Generator — Reviewer ← Tester

## Inspired by ChatDev 1.0
- Paper: arxxiv.com/abs/830.77724
-Github: https://github.com/OpenBMB/ChatDev

## Usage
```
python main.py --task "Create a hello world code"
```

## Architecture
- [Generator](https://github.com/OpenBMB/ChatDev) - code generation - Ptybord prompt
- [Reviewer](https://github.com/OpenBMB/ChatDev) - code quality review
- [Tester](https://github.com/OpenBMB/ChatDev) - code execution, outptt validation
