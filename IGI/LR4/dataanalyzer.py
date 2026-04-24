import pandas as pd

class DataAnalyzer:
    filename = 'Automobile_data.csv'
    def __init__(self):
        pass

    def anylyze(self):
        """Create dataframe with renamed row indexes"""
        df = pd.read_csv(self.filename)
        # Создаем список списков на основе реальных данных
        data_list = []
        for i in range(3): 
            row = [
                df.loc[i, 'symboling'],          
                df.loc[i, 'wheel-base'],          
                df.loc[i, 'length'],              
                df.loc[i, 'horsepower'],         
                df.loc[i, 'price']                
            ]
            data_list.append(row)

        print("\nСписок списков (первые 3 автомобиля):")
        print(data_list)

        column_names = ['symboling', 'wheel_base', 'length', 'horsepower', 'price']

        #  Создаем DataFrame
        car_features = pd.DataFrame(data_list, columns=column_names)

        #  Изменяем индексы на ['car_A', 'car_B', 'car_C']
        car_features.index = ['car_A', 'car_B', 'car_C']


        print("\n" + "="*50)
        print("Итоговый DataFrame car_features:")
        print("="*50)
        print(car_features)
    
    def average_coast(self):
        """Calculate average coast of auto with max num of cylinders"""
        df = pd.read_csv(self.filename)
        # Преобразуем колонку price в числовой тип
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        print(df['num-of-cylinders'].unique())

        max_cyl = 'twelve'
        max_cyl_cars = df[df['num-of-cylinders'] == max_cyl]  # Отфильтруем строки с максимальным числом цилиндров

        # Вычислим среднюю цену
        avg_price_max_cyl = round(max_cyl_cars['price'].mean(), 2)
        print(f"Средняя цена автомобилей с {max_cyl} цилиндрами: {avg_price_max_cyl}")
    
    def mpg_comparison(self):
        """Calculate relationship between max expensive and max cheapest"""
        df = pd.read_csv(self.filename)
        
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['highway-mpg'] = pd.to_numeric(df['highway-mpg'], errors='coerce')
        
        df_clean = df.dropna(subset=['price', 'highway-mpg']).copy()
        
        # Квартили
        Q1 = df_clean['price'].quantile(0.25)
        Q3 = df_clean['price'].quantile(0.75)
        
        cheap_cars = df_clean[df_clean['price'] <= Q1]
        expensive_cars = df_clean[df_clean['price'] >= Q3]
        
        avg_mpg_cheap = cheap_cars['highway-mpg'].mean()
        avg_mpg_expensive = expensive_cars['highway-mpg'].mean()
        
        ratio = avg_mpg_expensive / avg_mpg_cheap
        print(f"Отношение (дорогие / дешевые) = {ratio:.2f}")