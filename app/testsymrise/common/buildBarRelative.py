import pandas as pd
import matplotlib.pyplot as plt

def buildBarRelative(input_data):
    print(sorted(list(set(input_data["City"])))) # OK

    ratio = []
    for item1, item2 in zip(input_data["Number"][::2], input_data["Number"][1::2]):
        ratio.append(item1/item2 * 100)

    print(ratio)

    concatList = list((zip(sorted(list(set(input_data["City"]))),ratio)))

    df = pd.DataFrame(concatList, columns=['City', 'Ratio'])

    print(df)

    # fig, ax = plt.subplots()
    # ax.bar(list(set(data["City"])), ratio, color=['red', 'blue', 'orange'])

    """
    plt.xlabel('Villes')
    plt.ylabel('Ratio %')
    plt.title('Taux d\'appartements avec climatisation par ville')
    plt.legend(title='%', loc='upper right')
    """
    df.plot(y="Ratio", x="City", kind="bar", color = ['red', 'blue', 'orange'], xlabel='City', ylabel="%", title="Relative shares of flats with A/C")

    plt.show()

# buildBarRelative({'City': ['Berlin', 'Berlin', 'Koln', 'Koln', 'Munchen', 'Munchen'], 'Air-conditioning': ['with A/C', 'without A/C', 'with A/C', 'without A/C', 'with A/C', 'without A/C'], 'Number': [364, 10667, 46, 1428, 126, 1289]})