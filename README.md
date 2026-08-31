# 🛍️ Customer Segmentation using K-Means

## 📌 Project Overview

**Customer Segmentation** is a Machine Learning project that groups customers into meaningful segments based on their **Income** and **Spending Score**.

This project uses the **K-Means Clustering** algorithm, an unsupervised learning technique, to identify groups of customers with similar purchasing behavior.

The goal is to help businesses better understand their customers and make data-driven decisions for marketing, customer targeting, and business strategy.

---

## 🎯 Project Objectives

* Analyze customer income and spending behavior
* Preprocess and prepare customer data
* Determine an appropriate number of clusters
* Apply the K-Means clustering algorithm
* Visualize customer segments
* Interpret the characteristics of each customer group

---

## 🧠 Machine Learning Approach

This project uses **Unsupervised Learning** because the dataset does not contain predefined labels.

### Algorithm

**K-Means Clustering**

K-Means divides customers into `K` different clusters by assigning each customer to the cluster with the nearest centroid.

The main steps are:

1. Load the customer dataset
2. Explore and preprocess the data
3. Select relevant features
4. Scale the features
5. Determine the optimal number of clusters using the Elbow Method
6. Train the K-Means model
7. Assign customers to clusters
8. Visualize and interpret the results

---

## 📊 Features

The dataset contains the following features:

| Feature         | Description                |
| --------------- | -------------------------- |
| `CustomerID`    | Unique customer identifier |
| `Age`           | Customer age               |
| `Income`        | Customer annual income     |
| `SpendingScore` | Customer spending score    |

For the main segmentation analysis, **Income** and **SpendingScore** are used as the primary clustering features.

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🐼 **Pandas** – Data manipulation and analysis
* 🔢 **NumPy** – Numerical computation
* 📊 **Matplotlib** – Data visualization
* 🤖 **Scikit-learn** – Machine Learning and K-Means clustering

---

## 📁 Project Structure

```text
Customer-Segmentation/
│
├── data/
│   └── customers.csv
│
├── clustering.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Segmentation.git
```

Move into the project directory:

```bash
cd Customer-Segmentation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the clustering program:

```bash
python clustering.py
```

The program will:

* Load the customer dataset
* Prepare the data
* Apply K-Means clustering
* Generate customer segments
* Display the clustering visualization

---

## 📈 Elbow Method

The **Elbow Method** is used to determine a suitable value for `K`.

It evaluates the clustering error for different numbers of clusters and helps identify the point where increasing `K` provides diminishing improvement.

Example:

```python
from sklearn.cluster import KMeans

errors = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    errors.append(model.inertia_)
```

---

## 🤖 K-Means Clustering

After selecting the appropriate number of clusters, the K-Means model is trained:

```python
model = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

data["Cluster"] = model.fit_predict(X)
```

Each customer is then assigned to a cluster.

---

## 📊 Visualization

The project visualizes customer segments using **Income** and **Spending Score**.

This makes it easier to identify groups such as:

* 💎 High Income / High Spending
* 💰 High Income / Low Spending
* 🛍️ Low Income / High Spending
* 📉 Low Income / Low Spending
* 👥 Medium Income / Medium Spending

> Note: The exact interpretation of each cluster depends on the model results.

---

## 💡 Business Applications

Customer segmentation can help businesses:

* Create targeted marketing campaigns
* Identify high-value customers
* Develop personalized offers
* Improve customer retention
* Understand purchasing behavior
* Allocate marketing resources more effectively

---

## 📦 Requirements

The project requires:

```text
pandas
numpy
matplotlib
scikit-learn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

Possible improvements include:

* Add **Age** to the clustering analysis
* Compare different clustering algorithms
* Add **Silhouette Score** for model evaluation
* Build an interactive **Streamlit dashboard**
* Add customer cluster profiling
* Deploy the application online
* Add automated data preprocessing

---

## 👨‍💻 Author

**Your Name**

Computer Science Student | Aspiring AI Engineer

---

## ⭐ Project Status

**Completed – Customer Segmentation with K-Means Clustering**

If you find this project useful, consider giving the repository a ⭐ on GitHub.
