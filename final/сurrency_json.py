from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import json

class CurrencyBase:
    def __init__(self, сurrency_date=None):
         self.сurrency_date = сurrency_date
         if сurrency_date == None:
            self.сurrency_date = date.today().strftime("%d.%m.%Y")
         self.base_url = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={self.сurrency_date}'
            
    def get_data(self):
        r = requests.get(self.base_url) 
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find("table", {"class": "data"})
        # Создание списка заголовков таблицы
        headers = [header.text for header in data.find_all('th')]
        # Создание списка строк таблицы
        rows = []
        for row in data.find_all('tr')[1:]:
            rows.append([val.text for val in row.find_all('td')])
        return headers, rows

    def safe_data(self, headers, rows):
        
        data = {
        "headers": headers,
        "rows": rows
        }

        # Сохранение словаря в JSON файл
        json_filename = f"Курсы иностранных валют к рублю Российской Федерации за {self.сurrency_date}"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return f"Data has been saved to {json_filename}"

    def make_hist(self, headers, rows):

        df = pd.DataFrame(rows, columns=headers)
        df['Цифр. код'] = df['Цифр. код'].astype(int)
        df['Единиц'] = df['Единиц'].astype(int)
        df['Курс'] = df['Курс'].str.replace(',', '.').astype(float)
        df['Курс 1 к 1'] = df['Курс'] / df['Единиц']
        
        fig = px.histogram(df, y='Курс 1 к 1', x='Валюта', title="Курсы иностранных валют к рублю Российской Федерации", width=1200, height=800)
        fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                  hovermode="x")
        return fig.show()
    
    

base = CurrencyBase()
headers, rows = base.get_data()
base.make_hist(headers, rows)
base.safe_data(headers, rows)
