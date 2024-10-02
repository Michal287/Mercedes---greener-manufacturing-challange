from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

class EncodeCategorical:
    def __init__(self) -> None:

        self.le = LabelEncoder()
        self.le.fit(list("abcdefghijklmnopqrstuvwxyz"))

    def split_columns(self):
        for column in self.df_categorical.columns:
            self.df_categorical[f'{column}_single_char'] = self.df[column].apply(lambda x: x if len(x) == 1 else np.nan)
            self.df_categorical[f'{column}_splitted_char1'] = self.df[column].apply(lambda x: x[0] if len(x) == 2 else np.nan)
            self.df_categorical[f'{column}_splitted_char2'] = self.df[column].apply(lambda x: x[1] if len(x) == 2 else np.nan)

        # Remove basic columns
        self.df_categorical = self.df_categorical.iloc[:, 8:]

    def mapping_transform(self):
        for column in self.df_categorical.columns:
            self.df_categorical[column] = self.df_categorical[column].apply(lambda x: int(self.le.transform([x])[0]) + 1 if not x is np.nan else 0)

    def change_categorical_type(self):
        self.df.drop(columns=self.df.select_dtypes(include=['object']).columns, inplace=True)
        self.df = pd.concat([self.df, self.df_categorical], axis=1)

    def encode(self, df):
        self.df = df
        self.df_categorical = self.df.select_dtypes(object)

        self.split_columns()
        self.mapping_transform()
        self.change_categorical_type()
        return self.df