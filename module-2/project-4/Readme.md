# Context Engineering — Persona-Based LLM CLI

A simple command-line tool that lets you interact with an LLM using different expert personas, tones, and response styles.

---

## Features

- Choose from 4 expert personas (Software Engineer, Cloud Architect, AI Engineer, Cybersecurity Engineer)
- Customise tone, response format, and length per query
- Displays token usage after every response
- Continuous interaction loop until you exit

---

## Project Structure

```
├── main.py               # Entry point — CLI loop and orchestration
├── context_persona.py    # PERSONA dictionary with persona definitions
├── connect_llm.py        # LLM connection setup
└── README.md
```

---

## Setup

1. **Clone the repo**

   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Install dependencies**

   ```bash
   pip install langchain-core
   ```

3. **Configure your LLM** in `connect_llm.py` (add your API key / model settings)

---

## Usage

```bash
python main.py
```

You'll be prompted to enter:

| Input           | Options                                                                         |
| --------------- | ------------------------------------------------------------------------------- |
| Persona         | `software_engineer`, `cloud_architect`, `ai_engineer`, `cybersecurity_engineer` |
| Tone            | `friendly`, `professional`, `straight`                                          |
| Response format | `JSON`, `Bullet Points`, `Free Text`, etc.                                      |
| Length          | `short`, `medium`, `long`                                                       |
| Query           | Any question                                                                    |

Type `exit` or `quit` to stop.

---

## Personas

| Persona                  | Description                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `software_engineer`      | Senior SWE with 10+ years at Google, Microsoft, Amazon, Facebook                       |
| `cloud_architect`        | Principal Cloud Architect with 12+ years on AWS, Azure, GCP                            |
| `ai_engineer`            | Senior AI/ML Engineer specialising in LLMs, RAG, and MLOps                             |
| `cybersecurity_engineer` | Certified ethical hacker (CISSP, CEH) with 10+ years in offensive & defensive security |

---

## Example

```
Welcome back, Enter to interact with llm or `exit`, `quit` to exit
Select Your Persona: software_engineer
Enter the Tone: professional
Enter the way of response: Bullet Points
Enter the Length: short
Enter Your Query: What is the difference between SQL and NoSQL?
```

---
