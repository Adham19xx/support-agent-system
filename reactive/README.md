# Reactive (Rule-Based) Agent

This directory implements a pure Rule-Based (Reactive) Agent for classifying and handling support tickets using static Python conditions (if/elif/else). It operates without calling any External Large Language Models (LLMs).

# Architecture Summary
Provider / Model: None (Pure Python Logic) 
LLM API Calls: 0 Calls
Token Cost:$0.00 (0 Tokens)
Latency:Near-instant (1-3 s)

# How to Run
Navigate to Visual code and run


# Edge case 
if/elif chains evaluate conditions sequentially, the agent matches the VIP rule first and triggers ESCALATE_TO_MANAGEMENT. Consequently, it completely skips and ignores the critical RESTART_DATABASE action required for the crash.