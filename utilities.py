from typing import List, Generator, Optional
import re
import json

def batch_list(lst: List, batch_size: int) -> Generator[List, None, None]:
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]

def extract_json(raw: str) -> dict:
    raw = raw.strip()
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found in response:\n{raw}")
    return json.loads(match.group(0))

def extract_csv(raw: str) -> Optional[str]:
    raw = raw.strip()
    match = re.search(r"```csv\\?n?(.*?)```", raw, re.DOTALL)
    
    return match.group(1) if match else None