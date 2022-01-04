import math

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


class Report1:
    """
    Regresion Lineal, se usara para regresiones lineales simples
    como predecir los infectados en un pais, y se me proporciona
    dos variables para calcularlo

    para usar esta clase debere tener una variable dependiente (x)
    y una variable objetivo (y)
    """

    def _init_(self, file_name, x, y, prediccion, colum_date, c_date):
        self.file_name = file_name
        self.x = x
        self.y = y
        self.prediccion = prediccion
        self.column_date = colum_date
        self.c_date = c_date

    def function(self):
        # leo el archivo

        target = self.y
        extension = self.file_name.rsplit('.', 1)[1].lower()

        if extension == 'csv':
            dataframe = pd.read_csv(self.file_name)
        elif extension == 'json':
            dataframe = pd.read_json(self.file_name)
        else:
            dataframe = pd.read_excel(self.file_name)

        # tratamiento de fechas

        if int(self.c_date) == 1:
            dataframe[self.column_date] = dataframe[self.column_date].replace(
                to_replace='(( )[0-9]?[0-9](pm|am))|(( )[0-9]?[0-9]:[0-9][0-9](:[0-9][0-9])?)+', value="",
                regex=True)

            data_date = pd.Series(dataframe[self.column_date]).values
            dataframe[self.column_date] = dataframe[self.column_date].replace(
                to_replace='(/|-)', value="", regex=True)

            value = dataframe[self.column_date][0]
            value = "{}".format(value)
            size_value = len(value)
            divisor = 1 * (10 ** size_value)

            dataframe[self.column_date] = pd.to_numeric(dataframe[self.column_date])
            dataframe[self.column_date].apply(lambda x: (float(x) / float(divisor)))

        # tratamiento de datos nulos
        dataframe.fillna(0, inplace=True)

        # Seleccion de datos
        dataframe = dataframe[[self.x, self.y]]
        dataframe.fillna(0, inplace=True)

        value_y = pd.DataFrame(dataframe[self.y])
        value_x = pd.DataFrame(dataframe[self.x])

        dataframe = value_x
        dataframe[target] = value_y[target].reset_index().drop(columns='index')
        dataframe.fillna(0, inplace=True)

        # eliminacion de espacios entre los valores de dat
        dataframe[target].replace(["\\\\t", "", '', "\\\\00"], "---")
        dataframe[self.x].replace(["\\\\t", "", '', "\\\\00"], "---")

        dataframe = dataframe.fillna(0)
        # obtengo la variable independiente, eje x
        independent = dataframe.drop(columns=target).columns
        independent.fillna(0)  # espacios vacios lleno con 0
        # defino el modelo
        modelo = LinearRegression()
        modelo.fit(X=dataframe[independent], y=dataframe[target])

        dataframe["predicted"] = modelo.predict(dataframe[independent])

        prediction_test = dataframe[[target, "predicted"]]

        x_t, x_test, y_t, y_test = train_test_split(dataframe[independent], dataframe[target], train_size=0.9)
        mse = mean_squared_error(y_t, y_test)
        rmse = math.sqrt(mse)
        mse = rmse = 10
        # value_prediction = self.prediccion
        predicted = ''
        if not (self.prediccion == ''):
            predicted_to_int = int(self.prediccion)
            if dataframe[self.x] == dataframe[self.column_date]:
                predicted_to_int = predicted_to_int / divisor
            predicted = modelo.predict([[predicted_to_int]])

        # y = a + bx
        y_pred = modelo.predict(x_test)

        plt.xlim(float(dataframe[self.x].min()) * 1.1, float(dataframe[self.x].max()) * 1.1)
        plt.scatter(x_test, y_test, color="red")
        plt.scatter(x_test, y_pred, color="blue")
        plt.plot(x_t, modelo.predict(x_t), color="black")

        plt.title(self.x + " vs " + self.y)
        plt.xlabel("Valor X: " + self.x)
        plt.ylabel("Valor y: " + self.y)
        plt.scatter(data=dataframe, x=self.x, y=self.y)

        plt.grid(None)
        plt.savefig("./static/img.png")
        plt.close('all')