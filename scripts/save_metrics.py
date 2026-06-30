import json
import csv
import os
from datetime import datetime

with open("results.json", "r") as f:
    data = json.load(f)

results = data["results"]["results"]

total = len(results)
passed = sum(r["success"] for r in results)
failed = total - passed

hallucination_rate = (failed / total) * 100

latencies = [r["latencyMs"] for r in results]

average_latency = sum(latencies) / len(latencies)

latencies.sort()
p95_latency = latencies[int(0.95 * len(latencies)) - 1]

history_file = "history/metrics_history.csv"

file_exists = os.path.exists(history_file)

with open(history_file, "a", newline="") as csvfile:

    writer = csv.writer(csvfile)

    if not file_exists:
        writer.writerow([
            "Timestamp",
            "TotalTests",
            "Passed",
            "Failed",
            "HallucinationRate",
            "P95Latency",
            "AverageLatency"
        ])

    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        total,
        passed,
        failed,
        round(hallucination_rate,2),
        p95_latency,
        round(average_latency,2)
    ])

print("Metrics saved successfully.")