import requests, sys

prompt = " ".join(sys.argv[1:]) or "Ping"
res = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3", "prompt": prompt, "stream": False}
)
print(res.json()["response"])
