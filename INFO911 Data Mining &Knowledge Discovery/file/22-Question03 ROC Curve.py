import numpy as np
from sklearn.metrics import roc_curve

# 表格数据，包含样本ID、预测概率和真实标签（正类为1，负类为0）
table_data = [
    {"id": 1, "probability_for_positive_class": 0.19, "true_label": 0},
    {"id": 2, "probability_for_positive_class": 0.75, "true_label": 1},
    {"id": 3, "probability_for_positive_class": 0.99, "true_label": 1},
    {"id": 4, "probability_for_positive_class": 0.07, "true_label": 0},
    {"id": 5, "probability_for_positive_class": 0.52, "true_label": 1},
    {"id": 6, "probability_for_positive_class": 0.11, "true_label": 0},
    {"id": 7, "probability_for_positive_class": 0.06, "true_label": 0},
    {"id": 8, "probability_for_positive_class": 0.61, "true_label": 1},
    {"id": 9, "probability_for_positive_class": 0.67, "true_label": 0},
    {"id": 10, "probability_for_positive_class": 0.34, "true_label": 1}
]

# 从表格数据中提取实际标签和预测概率
y_true = np.array([data["true_label"] for data in table_data])
y_scores = np.array([data["probability_for_positive_class"] for data in table_data])

# 确保阈值从0开始，到1结束，并包含所有提到的probability_for_positive_class的概率点
thresholds = np.sort(np.unique(np.concatenate(([0], y_scores, [1]))))

# 打印表格的列标题
header = "Class      " + "  ".join([f"{'+':<3} {'-':<3}"] * len(thresholds))
print(header)

thresholds_line = "Threshold " + "  ".join([f"{threshold:.2f}" for threshold in thresholds])
print(thresholds_line)

# 计算每个阈值对应的TP、FP、TN、FN、TPR、FPR并打印出来
for metric in ["TP", "FP", "TN", "FN", "TPR", "FPR"]:
    metric_values = [f"{metric:<10}"]
    for threshold in thresholds:
        predicted_positive = y_scores >= threshold
        tp = np.sum((predicted_positive == 1) & (y_true == 1))
        fp = np.sum((predicted_positive == 1) & (y_true == 0))
        tn = np.sum((predicted_positive == 0) & (y_true == 0))
        fn = np.sum((predicted_positive == 0) & (y_true == 1))
        if metric == "TP":
            metric_values.append(f"{tp:<3}")
        elif metric == "FP":
            metric_values.append(f"{fp:<3}")
        elif metric == "TN":
            metric_values.append(f"{tn:<3}")
        elif metric == "FN":
            metric_values.append(f"{fn:<3}")
        elif metric == "TPR":
            tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
            metric_values.append(f"{tpr:.2f}")
        elif metric == "FPR":
            fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
            metric_values.append(f"{fpr:.2f}")
    print("  ".join(metric_values))
