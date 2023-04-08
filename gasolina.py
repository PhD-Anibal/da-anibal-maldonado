# código de geração do gráfico 
import pandas as pd
import seaborn as sns
data_df = pd.read_csv('gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=data_df, x="dia", y="venda")
    grafico.set(title='Venda de Gasolina x dia', xlabel='dia', ylabel='vaenda (l)');
grafico.figure.savefig("./gasolina.png")