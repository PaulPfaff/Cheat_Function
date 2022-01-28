def cheat(question_number):
    if question_number == 1:
        print("import matplotlib.pyplot as plt")
        print("import numpy as np")
        print("sample = np.random.normal(0, 1, 100")
        print("plt.boxplot(sample)")
    elif question_number == 2:
        print("import seaborn")
        print("seaborn.stripplot(sample, color='black'")
        print("seaborn.violinplot(sample")
        print("The upper half of the violinplot shows the probability density of a value having a specific value,")
        print("smoothed to a certain degree")
        print("violinplots are better, because they are easier and faster to interpret")
    elif question_number == 3:
        print("import pandas as pd")
        print("import seaborn")
        print("titanic = pd.read_csv('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv'")
        print("titanic_plot = seaborn.histplot(titanic, x='Sex', hue='Survived', multiple='stack'")
    elif question_number == 4:
        print("import sklearn.datasets")
        print("import pandas as pd")
        print("wine = sklearn.datasets.load_wine()")
        print("wine = pd.DataFrame(data=np.c_[wine['data'], wine['target']], columns=wine['feature_names'] + ['target'])")
        print("(seaborn.regplot(x='malic_acid', y='alcohol, data=wine))")
    else :
        print("Only contains the answers to question 1 to 4")
