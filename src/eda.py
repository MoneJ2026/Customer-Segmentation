import os
import matplotlib.pyplot as plt


# Images folder yoo hin jirre uuma
os.makedirs("images", exist_ok=True)


def basic_info(df):

    print("=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nShape")
    print(df.shape)

    print("\nInfo")
    df.info()

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistics")
    print(df.describe())


def income_distribution(df):

    plt.figure(figsize=(8, 5))

    plt.hist(df["Income"], bins=10)

    plt.title("Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Customers")

    plt.grid(True)

    plt.savefig("images/income_distribution.png")
    plt.show()


def spending_distribution(df):

    plt.figure(figsize=(8, 5))

    plt.hist(df["SpendingScore"], bins=10)

    plt.title("Spending Score Distribution")
    plt.xlabel("Spending Score")
    plt.ylabel("Customers")

    plt.grid(True)

    plt.savefig("images/spending_distribution.png")
    plt.show()


def scatter_plot(df):

    plt.figure(figsize=(8, 6))

    plt.scatter(
        df["Income"],
        df["SpendingScore"]
    )

    plt.title("Income vs Spending Score")
    plt.xlabel("Income")
    plt.ylabel("Spending Score")

    plt.grid(True)

    plt.savefig("images/scatter.png")
    plt.show()