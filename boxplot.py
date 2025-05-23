import matplotlib.pyplot as plt

# Função para ler e dividir os dados em grupos
def ler_e_organizar(caminho_arquivo, grupo_tamanho):
    with open(caminho_arquivo, "r") as f:
        valores = [float(linha.strip()) for linha in f.readlines()]
    return [valores[i:i + grupo_tamanho] for i in range(0, len(valores), grupo_tamanho)]

# Parâmetros
grupo_tamanho = 30  # Número de execuções por grupo
arquivo1 = "boxplot_1.txt"
arquivo2 = "boxplot_2.txt"

# Lê e agrupa os dados de ambos os arquivos
dados1 = ler_e_organizar(arquivo1, grupo_tamanho)
dados2 = ler_e_organizar(arquivo2, grupo_tamanho)
dados = dados1 + dados2  # Junta todos os grupos

# Reordena os dados na ordem desejada: por função dentro da mesma dimensão
ordem_desejada = [0, 2, 4, 1, 3, 5, 6, 8, 10, 7, 9, 11]
dados = [dados[i] for i in ordem_desejada]


# Nomes correspondentes a cada grupo
nomes = [
    "5 dim. (GRI/STD)", "5 dim. (GRI/INER)", "5 dim. (GRI/CON)",
    "5 dim. (ACK/STD)", "5 dim. (ACK/INER)", "5 dim. (ACK/CON)",
    "10 dim. (GRI/STD)", "10 dim. (GRI/INER)", "10 dim. (GRI/CON)",
    "10 dim. (ACK/STD)", "10 dim. (ACK/INER)", "10 dim. (ACK/CON)"
]

# Verifica se a contagem bate
if len(dados) != len(nomes):
    raise ValueError(f"Número de grupos ({len(dados)}) não bate com número de nomes ({len(nomes)}).")

# Cria o boxplot
fig, ax = plt.subplots()
box = ax.boxplot(dados,
                 patch_artist=True,
                 showmeans=False,
                 showcaps=True,
                 showfliers=False,
                 widths=0.6)

# Cores para os grupos
cores = ['orange', 'skyblue', 'lightgreen', 'lightcoral', 'gold',
         'lightblue', 'palegreen', 'salmon', 'plum', 'khaki', 'turquoise']

for patch, cor in zip(box['boxes'], cores):
    patch.set_facecolor(cor)

# Rótulos e aparência
ax.set_xticklabels(nomes, rotation=45, ha="right")
ax.set_ylabel("Resultado Final do Algoritmo")
ax.set_title("Comparação de Desempenho: c1 = 3.05 e c2 = 1.05")
plt.tight_layout()

# Salvar e mostrar
plt.savefig("comparacao_boxplot.png", dpi=300, bbox_inches='tight')
plt.show()
