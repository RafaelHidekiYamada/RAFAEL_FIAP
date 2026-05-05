# Conjuto de dados
vendas <- c(2, 4, 3, 4, 5, 2, 4)
vendas

# Análise Descritiva:
# Medidas de Tendência Central:
# Média:
mean(vendas)

# Mediana:
median(vendas)

# Moda:
table(vendas)
#ou
Mode(vendas)

# Máximo e Mínimo
range(vendas)

# Amplitude:
diff(range(vendas))

# Variância:
var(vendas)

# Desvio Padrão:
sd(vendas)

# Coeficiente de Variação:
sd(vendas)/mean(vendas)*100

# Medidas Separatrizes:
# Quartil:
quantile(vendas, probs=c(0.25, 0.50, 0.75))

# Sumario:
summary(vendas)

# Análise boxplot:
boxplot (vendas,
         col = "green",
         main = "Boxplot das vendas Semanais",
         ylab = "Quantidade de Vendas",
         xlab = "Dados Coletados na Ultima Semana")
