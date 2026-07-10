"""Generate k samples per task per model via OpenRouter."""
import os, re, time
from tasks import TASKS, STYLE

K_SAMPLES = 5
TEMPERATURE = 0.8
OUT_DIR = "generations"

SYSTEM = ("You are a quantum programming assistant. " + STYLE +
          " Wrap the code in a single ```python code block.")

def extract_code(text):
    m = re.findall(r"```(?:python)?\s*(.*?)```", text, re.DOTALL)
    return m[0].strip() if m else text.strip()

def call_openrouter(model, prompt):
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.environ["OPENROUTER_API_KEY"])
    r = client.chat.completions.create(
        model=model, temperature=TEMPERATURE,
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": prompt}])
    return r.choices[0].message.content

MODELS = {
    "gpt4o":      (call_openrouter, "openai/gpt-4o"),
    "claude":     (call_openrouter, "anthropic/claude-sonnet-4.5"),
    "gemini":     (call_openrouter, "google/gemini-2.5-pro"),
    "qwen_coder": (call_openrouter, "qwen/qwen-2.5-coder-32b-instruct"),
    "deepseek":   (call_openrouter, "deepseek/deepseek-chat"),
}

def main():
    for tag, (fn, model) in MODELS.items():
        os.makedirs(os.path.join(OUT_DIR, tag), exist_ok=True)
        for task in TASKS:
            for s in range(K_SAMPLES):
                path = os.path.join(OUT_DIR, tag, f"{task['id']}__{s}.py")
                if os.path.exists(path):
                    continue
                try:
                    code = extract_code(fn(model, task["prompt"]))
                    open(path, "w").write(code)
                    print(f"[ok] {tag} {task['id']} #{s}")
                except Exception as e:
                    print(f"[fail] {tag} {task['id']} #{s}: {type(e).__name__}: {e}")
                    time.sleep(5)
                time.sleep(0.3)

if __name__ == "__main__":
    main()
