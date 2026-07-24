import matplotlib.pyplot as plt


def basic_info(df):

    print("=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)

    print(df.head())

    print("\nShape")
    print(df.shape)

    print("\nInfo")
    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistics")
    print(df.describe())


def plot_histograms(df):

    df.hist(figsize=(10,8))

    plt.tight_layout()

    plt.savefig("images/histograms.png")

    plt.show()