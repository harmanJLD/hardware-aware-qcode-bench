"""Evaluate all generations and aggregate the paper's Table 1 numbers.

Usage: python run_eval.py            (reads generations/, writes results.csv)
"""
import csv, glob, os
from collections import defaultdict
from tasks import get_task
from harness import evaluate_generation, get_backends, TAU

GEN_DIR = "generations"
OUT_CSV = "results.csv"

def main():
    backends = get_backends()
    rows = []
    for model_dir in sorted(glob.glob(os.path.join(GEN_DIR, "*"))):
        model = os.path.basename(model_dir)
        for path in sorted(glob.glob(os.path.join(model_dir, "*.py"))):
            fname = os.path.basename(path)[:-3]
            task_id, sample = fname.rsplit("__", 1)
            row = evaluate_generation(open(path).read(), get_task(task_id), backends)
            row.update({"model": model, "sample": int(sample)})
            rows.append(row)
            print(f"{model:12s} {task_id:12s} #{sample} "
                  f"C={row['compiled']} F={row['functional_pass']} "
                  f"hex={row.get('hex_esp', '-')} ion={row.get('ion_esp', '-')}")
    if not rows:
        print("no generations found"); return

    keys = sorted({k for r in rows for k in r})
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader(); w.writerows(rows)

    # ---- aggregate: Table 1 of the paper ----
    agg = defaultdict(lambda: defaultdict(float))
    cnt = defaultdict(int)
    for r in rows:
        m = r["model"]; cnt[m] += 1
        agg[m]["C"] += r["compiled"]
        agg[m]["F"] += r["functional_pass"]
        agg[m]["F_hex"] += r.get("hex_hw_pass", False)
        agg[m]["F_ion"] += r.get("ion_hw_pass", False)

    print(f"\n=== Table 1 (tau = {TAU}) ===")
    print(f"{'model':14s} {'C':>6s} {'F':>6s} {'F_hex':>6s} {'F_ion':>6s} {'D_hex':>6s}")
    for m in sorted(agg):
        n = cnt[m]
        C, F = agg[m]["C"] / n, agg[m]["F"] / n
        Fh, Fi = agg[m]["F_hex"] / n, agg[m]["F_ion"] / n
        print(f"{m:14s} {C:6.2f} {F:6.2f} {Fh:6.2f} {Fi:6.2f} {F - Fh:6.2f}")
    print(f"\nwrote {OUT_CSV} ({len(rows)} generations)")

if __name__ == "__main__":
    main()
