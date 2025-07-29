from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
class DataPreprocessing:
    def __init__(self, df):
        self.df = df.copy() 
        self.encoder = LabelEncoder()
        self.scaler = StandardScaler()

    def tozala(self):
        for col in self.df.columns:
            if self.df[col].isnull().any():
                if self.df[col].dtype == 'object':
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
                else:
                    self.df[col] = self.df[col].fillna(self.df[col].mean())
        return self

    def encodla(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                if self.df[col].nunique() <= 6:
                    dummies = pd.get_dummies(self.df[col], prefix=col, dtype=int)
                    self.df = pd.concat([self.df.drop(columns=[col]), dummies], axis=1)
                else:
                    self.df[col] = self.encoder.fit_transform(self.df[col])
        return self

    def scaling_qil(self):
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns.drop("goals")
        self.df[numeric_cols] = self.scaler.fit_transform(self.df[numeric_cols])
        return self
     

    def get_df(self):
        return self.df
    
    
