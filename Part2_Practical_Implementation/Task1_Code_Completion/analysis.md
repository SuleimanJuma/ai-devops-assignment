## Task 1: Analysis

We implemented a function to sort a list of dictionaries by a key using both manual coding and AI-assisted code generation.

### Manual Implementation  
- **Approach**: Used `sorted()` with a lambda function for the key.  
- **Assumption**: Assumes the key exists in all dictionaries.  
- **Pros**: Simple and straightforward.  
- **Cons**: Prone to errors if the data is inconsistent (missing keys).  

### Copilot Implementation  
- **Approach**: Suggested using `d.get(sort_key, 0)` to handle missing keys by defaulting to `0`.  
- **Pros**: More robust for messy or incomplete data.  
- **Cons**: Slightly slower due to additional checks.  

### Efficiency Comparison  
- **Manual**: Slightly faster (no extra checks).  
- **Copilot**: More resilient in real-world scenarios.  

### Key Takeaways  
- Using Copilot saved development time and highlighted edge cases (e.g., missing keys).  
- Reviewing AI-generated code is essential to ensure alignment with project requirements and logic.  
