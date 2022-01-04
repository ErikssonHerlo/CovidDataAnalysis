import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


class Report1:
    def __init__(self, filename, country, nameCountry, date, infected):
        self.nameCountry = nameCountry
        self.file_name = filename
        self.country = country
        self.date = date
        self.infected = infected

    @property
    def generateReport(self):

        extension = self.file_name.rsplit('.', 1)[1].lower()

        if extension == 'csv':
            dataframe = pd.read_csv(self.file_name)
        elif extension == 'json':
            dataframe = pd.read_json(self.file_name)
        else:
            dataframe = pd.read_excel(self.file_name)

        dataframe.fillna(0, inplace=True)

        # trabajando con fechas
        #dataframe = dataframe.assign(new_date=pd.to_datetime(dataframe[self.date]).apply(lambda date: date.toordinal()))

        # # intercamiando nombres
        #dataframe.rename(columns={self.date: "Original", "new_date": self.date}, inplace=True)

        print(dataframe[self.date].values)

        dataframe = dataframe[dataframe[self.country] == self.nameCountry]
        x = np.asarray(dataframe[self.date].values)[:, np.newaxis]
        y = np.asarray(dataframe[self.infected].values)[:, np.newaxis]
        pyplot.plot(x, y,color="blue")
        # regression transform
        poly_degree = 3
        polynomial_features = PolynomialFeatures(degree=poly_degree)
        x_transform = polynomial_features.fit_transform(x)

        # fit the model
        model = LinearRegression().fit(x_transform, y)
        y_new = model.predict(x_transform)

        # calculate rmse and r2
        rmse = np.sqrt(mean_squared_error(y, y_new))
        r2 = r2_score(y, y_new)
        print('RMSE: ', rmse)
        print('R2: ', r2)

        # prediction
        x_new_min = dataframe[self.date].min() - 30
        x_new_max = dataframe[self.date].max() + 30

        x_new = np.linspace(x_new_min, x_new_max, 50)
        x_new = x_new[:, np.newaxis]

        x_new_transform = polynomial_features.fit_transform(x_new)
        y_new = model.predict(x_new_transform)

        # pyplot the prediction

        #fig, ax = pyplot.subplots()
        #fig.canvas.draw()

        #labels = [item.get_text() for item in ax.get_xticklabels()]
        #labels[0:] = dataframe["Original"].values

       # print("label")
        #print(dataframe["Original"].values)

        # ax.set_xticklabels(labels,fontsize=7)
        # pyplot.xticks(rotation=45)


        #ax.set_xticklabels(labels, fontsize=7)
        #pyplot.xticks(rotation=45)

        pyplot.plot( x_new,y_new, color='tomato', linewidth=3)
        pyplot.grid()
        pyplot.xlim(x_new_min, x_new_max)
        pyplot.ylim(0, dataframe[self.infected].max())
        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse, 2), round(r2, 2))
        pyplot.title("Tendencia en {}\n ".format(self.nameCountry) + title, fontsize=10)
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        # pyplot.show()
        pyplot.savefig("./static/resources/report.png")

        diccionario = {
            'Reporte': 'Tendencia de infectados en un pais',
            'Tipo': 'Polinomial ',
            'Pais': self.nameCountry,
            'RMSE': round(rmse, 2),
            'R2': round(r2, 2)
        }
        return diccionario
