**Introduction**

K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique. KNN algorithm stores all the available data and classifies a new data point based on the similarity. KNN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems. It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of classification, it performs an action on the dataset.

**Key Concepts** 

1.	Distance Metric: KNN often uses Euclidean distance to find the distance between data points.
   
3.	K-Value: The number of neighbors to consider (K). Choosing an optimal K value is essential for the algorithm's accuracy.
    
5.	Voting Mechanism: For classification, each neighbor votes for the class label, and the label with the most votes is selected.

**How KNN Works**

- **Step 1**: Load the labeled dataset.

- 	**Step 2**: Select the number K of the neighbors.
- 	Always use an odd number as the value of K.

- **Step 3**: For each data point in the dataset, calculate the distance to the new data point using a distance metric (e.g., Euclidean distance).

- **Step 4**: Sort all distances and select the K-nearest neighbors as per the calculated Euclidean distance.

- **Step 5**: For classification, each of the K neighbors votes for their class label, and the majority label is assigned to the new data point.

- **Step 6**: Return the predicted label or value for the query point.

**UNDERSTANDING HOW KNN WORKS**

**Step 1 :** To Load the data.

![step2](https://github.com/user-attachments/assets/1c777c73-fe57-4d30-a9ed-ab6807a9ad34)


**Step 2:** We will choose the number of neighbors, so we will choose the k=3.

**Step 3:** We will calculate the Euclidean distance between the data points. 

![step3](https://github.com/user-attachments/assets/2ceb6256-4331-4176-b0cf-1758b9aec764)

​![step3](https://github.com/user-attachments/assets/22e756cf-61bc-4ddc-99d6-fd4a0b0a008f)

**Step 4:** Sort all distances and select the K-nearest neighbors as per the calculated Euclidean distance.

By calculating the Euclidean distance we got the nearest neighbors, as Two nearest neighbors in Orange  color and one nearest neighbors in green color . Consider the below image:

![Step5](https://github.com/user-attachments/assets/507f4225-df39-41ff-a0a5-8a5b8f49d7f0)

-  As we can see the 2 nearest neighbors are from  orange color , hence this new data point must belong to orange color.

![step4](https://github.com/user-attachments/assets/2d692009-7866-4c09-a428-8050e3852062)

**Step 5:** Choosing the best k value
- The choice of k is crucial:A small value of k (e.g., 1 or 2) can lead to overfitting, as the model may be too sensitive to noise in the training data.

- A larger value of k smooths out the decision boundary but may overlook local patterns.

![step6](https://github.com/user-attachments/assets/739d183e-9b6a-4454-b54e-e6f1b728d054)

- In this we can see 4 nearest neighbors are from green color and three nearest neighbors in orange color,hence this new data point must belong to green color.

**Adavantages of KNN**

- **Simple and intuitive:** Easy to understand and implement.

- **No training phase:** Can be very fast in scenarios with small datasets.

- **Versatile:** Can handle multi-class classification problems.

**Disadvantages of KNN**

- **Computationally expensive**: Especially with large datasets, since the algorithm needs to calculate the distance to every training data point for each prediction.
- **Storage requirements:** It requires storing the entire dataset.
- Always needs to determine the value of K which may be complex some time.


**Acoknowledgements**

[KNN_Algorithm](https://www.javatpoint.com/k-nearest-neighbor-algorithm-for-machine-learning)











