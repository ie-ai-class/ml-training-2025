import pickle
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator
from sklearn.metrics import (
    PredictionErrorDisplay,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)


class MyUtil:
    def save_data(filename, data):
        with open(filename, "wb") as file:
            pickle.dump(data, file)

    def load_data(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data


class MyModel(BaseEstimator):
    def __init__(self, estimator=None, scalerX=None, scalerY=None):
        self.estimator = estimator
        self.scalerX = scalerX
        self.scalerY = scalerY
        self.dt = datetime.now().strftime("%Y-%m-%d_%H-%M")

    def fit(self, X, Y):
        X_sc = self.scalerX.fit_transform(X)
        Y_sc = self.scalerY.fit_transform(Y)
        self.estimator.fit(X_sc, Y_sc)
        self.is_fitted = True
        return self

    def predict(self, X):
        X_sc = self.transformX(X)
        return self.estimator.predict(X_sc)

    def transformX(self, X):
        if not self.is_fitted:
            raise Exception("Model is not fitted yet")
        X_sc = self.scalerX.transform(X)
        return X_sc

    def transformY(self, Y):
        if not self.is_fitted:
            raise Exception("Model is not fitted yet")
        Y_sc = self.scalerY.transform(Y)
        return Y_sc

    @staticmethod
    def eval_perf(y_true, y_pred):
        mse = mean_squared_error(y_true=y_true, y_pred=y_pred)
        mape = mean_absolute_percentage_error(y_true=y_true, y_pred=y_pred)
        r2 = r2_score(y_true=y_true, y_pred=y_pred)
        return mse, mape, r2

    @staticmethod
    def print_perf(data):
        for k, v in data.items():
            print(k, ":", v)

    def eval(self, X_train, X_test, Y_train, Y_test, save=False):
        Y_train = self.transformY(Y_train)
        Y_test = self.transformY(Y_test)
        Y_train_pred = self.predict(X_train)
        Y_test_pred = self.predict(X_test)

        data_arr = []
        for i in range(0, Y_train.shape[1]):
            mse_train, mape_train, r2_train = self.eval_perf(
                y_true=Y_train[:, i], y_pred=Y_train_pred[:, i]
            )
            mse_test, mape_test, r2_test = self.eval_perf(
                y_true=Y_test[:, i], y_pred=Y_test_pred[:, i]
            )

            data = {
                "Y": f"Y-{i + 1}",
                "MSE Train": mse_train,
                "MSE Test": mse_test,
                "MAPE Train": mape_train,
                "MAPE Test": mape_test,
                "R2 Train": r2_train,
                "R2 Test": r2_test,
            }
            self.print_perf(data)
            data_arr.append(data)

        mse_train, mape_train, r2_train = self.eval_perf(
            y_true=Y_train, y_pred=Y_train_pred
        )
        mse_test, mape_test, r2_test = self.eval_perf(y_true=Y_test, y_pred=Y_test_pred)
        self.print_perf(data)
        data = {
            "Y": "Y-All",
            "MSE Train": mse_train,
            "MSE Test": mse_test,
            "MAPE Train": mape_train,
            "MAPE Test": mape_test,
            "R2 Train": r2_train,
            "R2 Test": r2_test,
        }
        df_eval = pd.DataFrame.from_dict(data_arr)
        if save:
            filename = f"eval_{self.dt}.xlsx"
            df_eval.to_excel(filename, index=False)
        return df_eval

    def plot_res(self, X_train, X_test, Y_train, Y_test, save=False):
        Y_train = self.transformY(Y_train)
        Y_test = self.transformY(Y_test)
        Y_train_pred = self.predict(X_train)
        Y_test_pred = self.predict(X_test)

        for i in range(0, Y_train.shape[1]):
            fig, axes = plt.subplots(
                nrows=1,
                ncols=2,
                figsize=(10, 5),
                constrained_layout=True,
                sharex=True,
                sharey=True,
            )

            display_train = PredictionErrorDisplay(
                y_true=Y_train[:, i], y_pred=Y_train_pred[:, i]
            )
            display_train.plot(ax=axes[0])
            axes[0].set_title("Train")

            display_train = PredictionErrorDisplay(
                y_true=Y_test[:, i], y_pred=Y_test_pred[:, i]
            )
            display_train.plot(ax=axes[1])
            axes[1].set_title("Test")

            if save:
                filename = f"res_plot_{self.dt}_{i}.png"
                fig.savefig(filename, dpi=300)
            plt.show()
