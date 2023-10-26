import pandas as pd
import matplotlib.pyplot as plt

def buildBarAbsolute(input_data):
    """
    this fonction builds a graphic bar 

    return : displays a graphic bar
    """
    df = pd.DataFrame(input_data)

    # Créer un pivot table pour avoir "Avec Climatisation" et "Sans Climatisation" comme colonnes distinctes
    pivot_table = df.pivot(index='City', columns='Air-conditioning', values='Number')

    # Afficher deux barres distinctes pour chaque ville
    pivot_table.plot(kind='bar')
    plt.xlabel('Cities')
    plt.ylabel('Number of flats')
    plt.title('number of flats with and without air-conditioning')
    plt.legend(title='Air-conditioning', loc='upper right')
    plt.show()
