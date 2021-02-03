import random

#iris dataset pandas describe()
#    sepal length, sepal width, petal length, petal width
#count  150.000000  150.000000  150.000000  150.000000
#mean     5.843333    3.057333    3.758000    1.199333
#std      0.828066    0.435866    1.765298    0.762238
#min      4.300000    2.000000    1.000000    0.100000
#25%      5.100000    2.800000    1.600000    0.300000
#50%      5.800000    3.000000    4.350000    1.300000
#75%      6.400000    3.300000    5.100000    1.800000
#max      7.900000    4.400000    6.900000    2.500000


def create_random_transaction() -> dict:
    """Create a fake, random message."""
    return {
        "sepal length": round(random.uniform(4.3, 7.9), 1),
        "sepal width": round(random.uniform(2.0, 4.4), 1),
        "petal length": round(random.uniform(1.0, 6.9), 1),
        "petal width": round(random.uniform(0.1, 2.5), 1)
    }