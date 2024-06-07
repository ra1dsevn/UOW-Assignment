- - ### Question 1

    (A) **In data mining, tasks can be categorised as predictive tasks or descriptive tasks. Describe their differences and name one algorithm for each of the two kinds of tasks.**

    - Predictive tasks involve predicting a specific outcome based on input data. Example: Decision Tree.
    - 预测任务涉及根据输入数据预测特定结果。示例：决策树。
    - Descriptive tasks involve summarizing or describing the data to identify patterns. Example: Apriori algorithm.
    - 描述任务涉及总结或描述数据以识别模式。示例：Apriori算法。
    
    Additional algorithms:
    - Predictive: Random Forest, Support Vector Machine (SVM), Neural Networks
    - 预测：随机森林，支持向量机（SVM），神经网络
    - Descriptive: k-means Clustering, DBSCAN, Hierarchical Clustering
    - 描述：k均值聚类，DBSCAN，层次聚类
    
    (B) **In data mining algorithms, a sample is often interpreted as a point in a multi-dimensional space. Explain how this interpretation is made and what the space is.**
    
    - Each attribute of the sample represents a dimension in this space. 
    - The sample's attribute values correspond to coordinates in the multi-dimensional space, forming a point.
    - 样本的每个属性代表此空间中的一个维度。样本的属性值对应于多维空间中的坐标，形成一个点。
    
    (C) **What are outliers in data mining? And when shall outliers be removed or kept?**
    
    - Outliers are data points that differ significantly from others. They should be removed if they result from data errors or noise but should be kept if they represent true variability in the data.
    - 离群点是与其他数据显著不同的数据点。如果它们是由于数据错误或噪音而引起的，应予以删除；但如果它们代表数据的真实变异性，则应保留。
    
    Additional considerations:
    - If outliers influence results significantly, re-evaluation should be done.
    - 如果离群点显著影响结果，则应重新评估。
    - Use domain knowledge to decide on outlier treatment.
    - 使用领域知识决定离群点处理。
    - Analyze the cause of outliers before deciding on removal.
    - 在决定删除之前，分析离群点的原因。
    
    (D) **Name two ways that can be used to deal with missing values and discuss their strengths and weaknesses.**
    
    1. **Imputation (mean/median/mode)**: Strength - Easy to implement; Weakness - Can introduce bias.
    2. **插补（均值/中位数/众数）**：优势 - 易于实现；劣势 - 可能引入偏差。
    3. **Deletion (listwise/pairwise)**: Strength - Simplifies analysis; Weakness - Reduces data size, possibly losing valuable information.
    4. **删除（列表法/成对法）**：优势 - 简化分析；劣势 - 减少数据量，可能会丢失有价值的信息。
    
    Additional methods:
    - **Imputation using predictive models (e.g., regression imputation)**: Strength - More accurate imputation; Weakness - More complex, computationally intensive.
    - **使用预测模型的插补（例如，回归插补）**：优势 - 更准确的插补；劣势 - 更复杂，计算密集。
    - **Multiple Imputation**: Strength - Accounts for uncertainty; Weakness - Computationally intensive.
    - **多重插补**：优势 - 考虑到不确定性；劣势 - 计算密集。
    - **Using algorithms that handle missing values inherently (e.g., Random Forests)**: Strength - No need for explicit imputation; Weakness - May not be applicable to all models.
    - **使用固有处理缺失值的算法（例如，随机森林）**：优势 - 不需要显式插补；劣势 - 可能不适用于所有模型。
    
    (E) **Dimensionality reduction and feature subset selection are two techniques of data pre-processing. Discuss their differences.**
    
    - Dimensionality reduction transforms data into a lower-dimensional form (e.g., PCA), while feature subset selection involves selecting a subset of original features without transforming them.
    - 降维将数据转换为低维形式（如PCA），而特征子集选择涉及选择原始特征的一个子集而不进行转换。
    
    Additional techniques:
    - **Principal Component Analysis (PCA)**: Dimensionality reduction by transforming data.
    - **主成分分析（PCA）**：通过变换数据进行降维。
    - **Linear Discriminant Analysis (LDA)**: Dimensionality reduction with a focus on maximizing class separability.
    - **线性判别分析（LDA）**：以最大化类别可分离性为重点的降维。
    - **Feature Importance Ranking (e.g., using Random Forest importance scores)**: Feature subset selection based on importance scores.
    - **特征重要性排名（例如，使用随机森林重要性评分）**：基于重要性评分的特征子集选择。
    
    (F) **List three important factors that drive the development of mining of big data.**
    
    1. Advances in computing power.
    2. Increased data generation from various sources.
    3. Improved data storage technologies.
    4. 计算能力的进步。
    5. 各种来源的数据生成增加。
    6. 数据存储技术的改进。
    
    Additional factors:
    - Development of sophisticated data mining algorithms.
    - 复杂数据挖掘算法的发展。
    - Growth of the internet and IoT devices.
    - 互联网和物联网设备的增长。
    - Enhanced data integration and interoperability.
    - 增强的数据集成和互操作性。
    
    ### Question 2
    
    (A) **Clustering is a commonly used technique in data mining. Explain the purpose of conducting clustering and provide an example application of clustering.**
    
    - Purpose: To group similar data points into clusters. 
    - Example: Market segmentation in customer data analysis.
    - 目的：将相似的数据点分组为集群。
    - 示例：客户数据分析中的市场细分。
    
    Additional applications:
    - **Image segmentation**: Grouping pixels in images to identify objects or regions.
    - **图像分割**：将图像中的像素分组以识别对象或区域。
    - **Anomaly detection**: Identifying unusual patterns that do not fit the expected behavior.
    - **异常检测**：识别不符合预期行为的异常模式。
    - **Document clustering**: Organizing a large collection of documents into clusters for easier retrieval.
    - **文档聚类**：将大量文档分组以便于检索。
    
    (B) **Suppose five clusters C1, C2, C3, C4 and C5 are formed during the process of hierarchical clustering.**
    
    a. The proximity matrix would be a 5x5 matrix, with each entry representing the distance between clusters.
    b. After merging C3 and C4, update entries involving these clusters to reflect the new cluster's distance to others.
    c. 近邻矩阵将是一个5x5的矩阵，每个条目代表集群之间的距离。
    d. 合并C3和C4后，更新涉及这些集群的条目以反映新集群与其他集群的距离。
    
    Additional considerations:
    - **Single linkage**: Distance between clusters defined by the closest points.
    - **单链法**：集群之间的距离由最近的点定义。
    - **Complete linkage**: Distance defined by the farthest points.
    - **全链法**：距离由最远的点定义。
    - **Average linkage**: Distance defined by the average of all pairwise distances.
    - **平均链法**：距离由所有成对距离的平均值定义。
    
    ### Question 3
    
     **(A)The performance of k-nearest neighbour (k-NN) classifier significantly depends on the value of k.  Suppose you are given a set of M samples and the class label of each sample is also provided to you. Describe the procedure that you will use to select the best k value such that the k-NN classifier can expect to achieve the highest classification accuracy on a future test set.**
    
    - Procedure: Split the dataset into training and validation sets, 
    - train k-NN with various k values, 
    - evaluate performance on the validation set, 
    - and select the k that provides the best accuracy.
    - 步骤：将数据集分为训练集和验证集，使用不同的k值训练k-NN，评估验证集上的性能，并选择提供最佳准确度的k值。
    
    Additional considerations:
    - **Cross-validation**: Use k-fold cross-validation to evaluate different k values.
    - **交叉验证**：使用k折交叉验证评估不同的k值。
    - **Grid search**: Systematically search through a range of k values.
    - **网格搜索**：系统地搜索一系列k值。
    - **Distance weighting**: Consider weighting the votes of neighbors by their distance.
    - **距离加权**：考虑按距离加权邻居的投票。
    
    (B) **The key step to train a multi-layer perceptron (MLP) network is to adjust the weight of connections. Answer the following questions related to this step:**
    
    a. Commonly used cost function: **Mean Squared Error (MSE)** – measures the average squared difference between observed and predicted values.
    b. 常用的成本函数：均方误差（MSE）——测量观测值和预测值之间的平均平方差。
    c. Common algorithm: **Backpropagation. Key steps: Forward pass, compute error, backpropagation to update weights.**
    d. 常用算法：反向传播。关键步骤：前向传播，计算误差，反向传播以更新权重。
    
    Additional cost functions:
    - **Cross-Entropy Loss**: Used for classification tasks.
    - **交叉熵损失**：用于分类任务。
    - **Hinge Loss**: Used for support vector machines.
    - **铰链损失**：用于支持向量机。
    - **Huber Loss**: Combines MSE and MAE, used for robust regression.
    - **Huber损失**：结合MSE和MAE，用于鲁棒回归。
    
    (C) **Suppose you are going to train an MLP network with the five properties shown below. Calculate the total number of weights (i.e., weight parameters) that will be adjusted during the training process. Show and explain how you derive your answer. Note that you may not need to use all the properties provided.**
    
    - Total weights = (Input neurons * neurons in first hidden layer) + (first hidden layer neurons * second hidden layer neurons) + (second hidden layer neurons * output neurons) + biases.
    - 总权重=（输入神经元*第一隐藏层的神经元）+（第一隐藏层神经元*第二隐藏层神经元）+（第二隐藏层神经元*输出神经元）+偏置。
    
    Additional considerations:
    - **Number of biases**: Each neuron in hidden and output layers typically has a bias.
    - **偏置的数量**：隐藏层和输出层的每个神经元通常都有一个偏置。
    - **Activation functions**: Influence the number of computations but not the number of weights.
    - **激活函数**：影响计算数量但不影响权重数量。
    - **Layer connections**: Ensure all layers are fully connected unless specified otherwise.
    - **层连接**：确保所有层完全连接，除非另有说明。
    
    (D) **A student designs a binary (i.e., positive class vs. negative class) classifier and evaluates it on a test set consisting of 10 samples. The result is recorded in the following table.**
    
    a. Construct a Receiver Operating Characteristic (ROC) curve based on the result in the table. Steps: Sort samples by predicted probability, compute TPR and FPR, plot TPR vs. FPR.
    b. Compute the Area Under the ROC curve (AUC): Calculate the area under the plotted ROC curve.
    c. 根据表中的结果构建接收器操作特性（ROC）曲线。步骤：按预测概率排序样本，计算TPR和FPR，绘制TPR与FPR。
    d. 计算ROC曲线下的面积（AUC）：计算绘制的ROC曲线下的面积。
    
    Additional metrics:
    - **Precision-Recall Curve**: Useful for imbalanced datasets.
    - **精确率-召回率曲线**：对不平衡数据集有用。
    - **Confusion Matrix**: Provides a summary of prediction results.
    - **混淆矩阵**：提供预测结果的总结。
    - **F1 Score**: Harmonic mean of precision and recall.
    - **F1评分**：精确率和召回率的调和平均值。
    
    ### Question 4
    
    (A) **Describe the main steps of the Apriori algorithm for mining association rules. Explain how the algorithm generates the candidate itemsets and how the algorithm prunes the candidate itemsets.**
    
    - Main steps: Identify frequent itemsets, generate candidate itemsets by joining frequent itemsets, prune candidate itemsets that do not meet minimum support.
    - 主要步骤：识别频繁项集，通过连接频繁项集生成候选项集，修剪不满足最小支持度的候选项集。
    
    Additional steps:
    - **Support counting**: Count occurrences of itemsets in the dataset.
    - **支持计数**：统计数据集中项集的出现次数。
    - **Generating association rules**: From frequent itemsets, generate rules meeting minimum confidence.
    - **生成关联规则**：从频繁项集中生成满足最小置信度的规则。
    - **Pruning rules**: Remove rules that do not meet the desired metrics.
    - **修剪规则**：删除不符合期望指标的规则。
    
    (B) **Let L = {A,B,C,D} denote a frequent itemset. Use it to mathematically show that “confidence of rules generated from the same itemset has an anti-monotone property.”**
    
    - For any frequent itemset L, the confidence of a rule generated from L will be at least as large as the confidence of a rule generated from any subset of L, showing an anti-monotone property.
    - 对于任何频繁项集L，从L生成的规则的置信度至少与从L的任何子集生成的规则的置信度一样大，显示出反单调性。
    
    Additional proofs:
    - **Lift**: Confidence(X → Y) / Support(Y).
    - **提升度**：置信度(X → Y) / 支持度(Y)。
    - **Conviction**: (1 - Support(Y)) / (1 - Confidence(X → Y)).
    - **确信度**： (1 - 支持度(Y)) / (1 - 置信度(X → Y))。
    - **Leverage**: Support(X ∪ Y) - Support(X) * Support(Y).
    - **杠杆度**： 支持度(X ∪ Y) - 支持度(X) * 支持度(Y)。
    
    ### Question 5
    
    #### (A)
    
    **Explanation:**
    
    - The points represented by **o** and **x** in the plot are observations from two different classes: versicolor and virginica.
    - The **o** points correspond to observations of the versicolor class, while the **x** points correspond to observations of the virginica class.
    - The important difference between them is their class membership. In the context of a Support Vector Machine (SVM) classification task, these points are separated by a decision boundary. The SVM aims to find the hyperplane that best separates the two classes with the maximum margin.
    
    #### (B)
    
    **Differences between Soft Margin Classifier and Maximal Margin Classifier:**
    
    - **Maximal Margin Classifier**: It finds the hyperplane that separates the data into two classes with the largest possible margin. However, it is very sensitive to outliers because it does not allow any misclassification or overlap in the margin.
    - **Soft Margin Classifier**: It allows some misclassifications or overlaps in the margin to handle non-separable data and outliers better. It introduces slack variables (ε_i) to permit some margin violations, controlled by a tuning parameter C that balances the margin width and the penalty for misclassifications.
    
    #### (C)
    
    **Relationships between Slack Variables and Tuning Parameter C:**
    
    - **Slack Variables (ε_i)**: These variables measure the degree of misclassification or how much each data point violates the margin. For correctly classified points, ε_i = 0; for misclassified points, ε_i > 0.
    - **Tuning Parameter (C)**: This parameter controls the trade-off between maximizing the margin and minimizing the classification error. A larger value of C puts more emphasis on correctly classifying all training examples, resulting in a smaller margin. A smaller value of C allows more misclassifications, leading to a wider margin.
    - 在支持向量机（Support Vector Machine，SVM）模型中，松弛变量（Slack Variables，记为ε_i）和调优参数（Tuning Parameter，记为C）之间的关系是相互影响的。
    
      松弛变量ε_i用于度量第i个数据点违反间隔的程度。也就是说，对于正确分类并且位于正确边界之外的点，其ε_i等于0；对于位于边界之内或者被错误分类的点，其ε_i大于0。
    
      调优参数C则是一个控制误分类率与间隔大小之间权衡的参数。C的值越大，意味着我们更强调正确地分类所有训练样本，这可能会导致间隔变小。反之，如果C的值较小，那么模型会容忍更多的误分类点，从而可能获得更大的间隔。
    
      ε_i和C之间的关系可以理解为：_
    
      _ε_i反映了数据点违反分类间隔的程度，C则是我们对这种违反程度的容忍度。
    
      
    
    #### (D)
    
    **Classification of a New Observation Using SVM:**
    
    - The SVM classifier uses the decision boundary (hyperplane) defined during training. For a new observation with predictors \((x_1^*, x_2^*, x_3^*)\), the SVM calculates the decision function, which is a weighted sum of the predictor values plus a bias term.
    - The new observation is classified based on which side of the hyperplane it falls. If the decision function's value is positive, the observation is classified into one class (e.g., virginica), and if negative, into the other class (e.g., versicolor).
    - 在使用支持向量机（SVM）对新的观测值y*进行分类时，我们不需要构建新的决策函数。我们会使用在训练阶段确定的决策边界（决策函数）来对新的观测值进行分类。
    
      具体来说，对于新的观测值，我们将计算其在决策函数中的值，然后根据这个值的正负来决定新的观测值应该被分类到哪一个类别。如果决策函数的值为正，我们将观测值分类为一个类别；如果为负，我们将其分类为另一个类别。
    
      因此，对于新的观测值，我们是沿用旧的决策函数，并通过判断其在决策面的哪一侧来进行分类。
    
    #### (E)
    
    **Explanation of the Overfitting Problem:**
    
    - Overfitting occurs when a model learns the noise and details in the training data to the extent that it negatively impacts its performance on new data. It happens when the model is too complex, having too many parameters relative to the number of observations.
    - In the context of SVM, using a very high value of C can lead to overfitting, as the model will attempt to correctly classify every training example, capturing noise and outliers instead of general patterns.
    
    #### (F)
    
    **Reason Linear Regression is Not Appropriate for Binary/Categorical Response Variable:**
    
    - Linear regression assumes that the response variable is continuous and can take any value. However, in binary or categorical response settings, the response variable is discrete, often taking values such as 0 or 1.
    - Linear regression can predict values outside the range of 0 and 1, which do not make sense for probabilities or class labels. This violates the assumption of a binary/categorical response and leads to poor and misleading predictions. Logistic regression or other classification methods are more appropriate as they are designed to handle discrete outcomes.
    
    1. 输出范围问题：线性回归预测的结果是连续的，其范围通常是负无穷大到正无穷大。然而，对于二元或分类响应变量，其值通常是有限的（比如0和1），这使得线性回归的预测结果可能会超出合理范围。
    2. 类别间距离问题：线性回归假设响应变量的值反映了其间的相对距离，但是对于分类变量来说，类别间没有这样的顺序或距离关系。
    3. 非线性关系问题：对于二元或分类响应变量，其与预测变量之间的关系往往是非线性的，而线性回归模型无法很好地捕捉到这种非线性关系。
    
    Linear regression is not appropriate for binary/categorical response variables for several reasons:
    
    1. Output Range Issue: Linear regression predicts continuous outputs, typically ranging from negative infinity to positive infinity. However, for binary or categorical response variables, values are usually finite (e.g., 0 and 1), which could lead to predictions from linear regression that fall outside of a sensible range.
    2. Category Distance Issue: Linear regression assumes that the values of the response variable reflect relative distances between them. But for categorical variables, there's no such order or distance relationship between categories.
    3. Non-linearity Issue: For binary or categorical response variables, the relationship with the predictor variables is often non-linear, and linear regression models can't capture this non-linear relationship well.
    
    ### 问题5的答案
    
    #### (A)
    
    **解释:**
    
    - 图中用 **o** 和 **x** 表示的点是来自两个不同类别的观测值：versicolor 和 virginica。
    - **o** 点对应的是 versicolor 类别的观测值，而 **x** 点对应的是 virginica 类别的观测值。
    - 它们之间的重要区别在于它们的类别归属。在支持向量机（SVM）分类任务的背景下，这些点被一个决策边界分开。SVM 旨在找到一个最佳分隔两个类别的超平面，并使其间距最大化。
    
    #### (B)
    
    **软边界分类器和最大边界分类器的区别:**
    
    - **最大边界分类器**：它找到一个将数据分为两类的超平面，并使这个边界的间距尽可能大。然而，它对异常值非常敏感，因为它不允许任何分类错误或边界重叠。
    - **软边界分类器**：它允许一些分类错误或边界重叠，以更好地处理不可分数据和异常值。它引入了松弛变量 (ε_i) 来允许一些边界违反，由一个调节参数 C 控制，该参数平衡了边界宽度和分类错误的惩罚。
    
    #### (C)
    
    **松弛变量和调节参数 C 之间的关系:**
    
    - **松弛变量 (ε_i)**：这些变量度量了分类错误的程度或每个数据点违反边界的程度。对于正确分类的点，ε_i = 0；对于错误分类的点，ε_i > 0。
    - **调节参数 (C)**：该参数控制了最大化边界和最小化分类错误之间的权衡。较大的 C 值更注重于正确分类所有训练样本，导致较小的边界。较小的 C 值允许更多的分类错误，从而产生更宽的边界。
    
    #### (D)
    
    **使用 SVM 分类新观测值:**
    
    - SVM 分类器使用训练期间定义的决策边界（超平面）。对于具有预测变量 \((x_1^*, x_2^*, x_3^*)\) 的新观测值，SVM 计算决策函数，该函数是预测变量值的加权和加上一个偏置项。
    - 新观测值根据其落在超平面哪一侧来分类。如果决策函数的值为正，则观测值分类为一类（例如 virginica），如果为负，则分类为另一类（例如 versicolor）。
    
    #### (E)
    
    **过拟合问题的解释:**
    
    - 过拟合发生在模型学习了训练数据中的噪声和细节，以至于它对新数据的性能产生负面影响。它发生在模型过于复杂，即相对于观测值的数量，参数过多时。
    - 在 SVM 的背景下，使用非常大的 C 值可能导致过拟合，因为模型会试图正确分类每一个训练样本，捕捉噪声和异常值，而不是一般模式。
    
    #### (F)
    
    **线性回归不适用于二元/分类响应变量的一个明显原因:**
    
    - 线性回归假设响应变量是连续的，可以取任何值。然而，在二元或分类响应设置中，响应变量是离散的，通常取值为 0 或 1。
    - 线性回归可能预测出 0 和 1 范围之外的值，这对概率或类别标签来说是没有意义的。这违反了二元/分类响应的假设，导致糟糕且误导的预测。逻辑回归或其他分类方法更适合，因为它们设计用于处理离散结果。