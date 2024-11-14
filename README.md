**Introduction**

K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique. KNN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using KNN algorithm. KNN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems. It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of classification, it performs an action on the dataset.

**Key Concepts** 

1.	Distance Metric: KNN often uses Euclidean distance to find the distance between data points.
   
3.	K-Value: The number of neighbors to consider (K). Choosing an optimal K value is essential for the algorithm's accuracy.
    
5.	Voting Mechanism: For classification, each neighbor votes for the class label, and the label with the most votes is selected.

**How KNN Works**

- **Step 1**: Load the labeled dataset.

- 	**Step 2**: Select the number K of the neighbors.

- **Step 3**: For each data point in the dataset, calculate the distance to the new data point using a distance metric (e.g., Euclidean distance).

- **Step 4**: Sort all distances and select the K-nearest neighbors as per the calculated Euclidean distance.

- **Step 5**: For classification, each of the K neighbors votes for their class label, and the majority label is assigned to the new data point.

- **Step 6**: Return the predicted label or value for the query point.

**UNDERSTANDING HOW KNN WORKS**

**Step 1 :** To Load the data.

![step2](https://github.com/user-attachments/assets/1c777c73-fe57-4d30-a9ed-ab6807a9ad34)




**Step 2:** Firstly, we will choose the number of neighbors, so we will choose the k=5.










