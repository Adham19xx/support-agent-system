# Support-Agent-System

This project compares four different AI agent architectures for solving customer support requests.

## Approaches

- Reactive
- Deterministic Routing
- Unconstrained LLM
- Constrained ReAct

  ## AI Agent Approaches
  
   ### 1. Reactive System
Uses hard-coded if/else rules.
Fast and simple, but less flexible.

  ### 2. Deterministic Routing
Uses AI classification followed by fixed logic execution.
Provides predictable and consistent results.

  ### 3. Unconstrained LLM Agent
Uses LLM reasoning without strict limitations.
Highly flexible, but may be slower and more expensive.

  ### 4. Constrained ReAct Agent
Uses tools, schemas, and maximum steps to control reasoning.
More reliable and structured while maintaining flexibility.

## Project Structure
```
project/
├── reactive/
│   ├── main.py
│   ├── README.md
├── deterministic/
│   ├── main.py
│   └── README.md
├── unconstrained/
│   ├── main.py
│   ├── prompt.py
│   ├── tools.py
│   ├── .env
│   ├── agent.py
│   └── requirements.txt
├── constrained/
│   ├── main.py
│   ├── prompt.py
│   └── tools.py
├── README.md
└── .gitignore
```

## How to Run

### Reactive System

Navigate to Visual code and run

### Deterministic Routing

1. Ensure your `.env` file exists in the root directory and contains `GEMINI_API_KEY`.
2. Install google-genai and python-dotenv in python
3. 
### Unconstrained LLM Agent

Install dependencies, add your API key to the .env file, then run:

`bash
pip install -r requirements.txt
cd unconstrained
python main.py

### Constrained ReAct Agent

cd constrained
python main.py
