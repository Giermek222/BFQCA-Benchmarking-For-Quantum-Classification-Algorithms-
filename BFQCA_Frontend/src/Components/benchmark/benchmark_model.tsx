const BenchmarkModel = new Map([
  ["algorithm_name", "Algorithm"],
  ["problem_name", "Problem"],
  ["training_accuracy", "Training Accuracy"],
  ["training_precision", "Training Precision"],
  ["training_recall", "Training Recall"],
  ["training_f1_score", "Training F1 Score"],
  ["training_loss", "Learning Loss"],
  ["test_accuracy", "Test Accuracy"],
  ["test_loss", "Test Loss"],
  ["test_precision", "Test Precision"],
  ["test_recall", "Test Recall"],
  ["test_f1_score", "Test F1 Score"],
  ["time", "Time"],
  ["max_latency_ms", "Max Latency"],
  ["min_latency_ms", "Min Latency"],
  ["avg_latency_ms", "Avg Latency"],
  ["percentile_latency_ms", "Latency Percentile"],
]);

export default BenchmarkModel;
