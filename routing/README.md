# Deterministic Routing Agent

This directory implements a Deterministic Routing Agent. It uses a single LLM call to classify an incoming support ticket into a predefined category, then routes the output to execute standard, deterministic Python functions.

# Architecture Summary
Provider / Model:** gemini-3.6-flash (via Google GenAI SDK)
Temperature:0.0
LLM API Calls:1 Call per request
Token Cost:100 Tokens (< $0.0001 per request)
Latency:Very Fast (1sec – 5sec)

# How to Run
1. Ensure your `.env` file exists in the root directory and contains `GEMINI_API_KEY`.
2. Install google-genai and python-dotenv in python


# edge case 
   The agent relies on a single LLM classification call without historical memory or external lookup tools. It accepts the user's claim at face value and escalates immediately, without verifying if previous complaints actually exist in the database.