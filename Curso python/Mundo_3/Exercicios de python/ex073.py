times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Fluminense',
         'Athletico - PR', 'Atlético - MG', 'América - MG', 'Goiás', 'Santos',
         'Chapecoense', 'Fortaleza', 'Botafogo', 'São Paulo', 'Cerará', 'Cuiabá',
         'Coritiba', 'Avaí', 'Atlético - GO', 'Juventude')
print(f"""{'-='*14}
Lista de times do Brasileirão: {times}
Os 5 primeiro colocados são: {times[:-15]}
{'-='*14}
Os ultimos 4 colocados da são: {times[-5:]}
{'-='*14}
Os times em ordem alfabética : {sorted(times)}
{'-='*14}
O time da chapecoense esta em: {len(times[:10])}º Lugar""")
