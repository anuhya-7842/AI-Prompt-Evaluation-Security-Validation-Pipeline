import json
import sys

# Thresholds
MAX_HALLUCINATION_RATE = 5.0      # %
MAX_P95_LATENCY = 500             # milliseconds

with open("results.json", "r") as f:
    data = json.load(f)

results = data["results"]["results"]

total = len(results)
passed = sum(r["success"] for r in results)
failed = total - passed

hallucination_rate = (failed / total) * 100

latencies = sorted(r["latencyMs"] for r in results)

# Calculate P95 latency
index = int(0.95 * len(latencies)) - 1
index = max(index, 0)
p95_latency = latencies[index]

print(f"Total Tests          : {total}")
print(f"Passed               : {passed}")
print(f"Failed               : {failed}")
print(f"Hallucination Rate   : {hallucination_rate:.2f}%")
print(f"P95 Latency          : {p95_latency} ms")

failed_pipeline = False

if hallucination_rate > MAX_HALLUCINATION_RATE:
    print("\n❌ Hallucination rate exceeded threshold!")
    failed_pipeline = True

if p95_latency > MAX_P95_LATENCY:
    print("\n❌ Latency exceeded SLA!")
    failed_pipeline = True

if failed_pipeline:
    sys.exit(1)

print("\n✅ Evaluation Passed")