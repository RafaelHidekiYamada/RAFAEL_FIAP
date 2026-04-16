# Vetor
vator <- 1:7
vetor1

vetor2 <- c(2, 5, 2.6, 1/2, -8)
vetor2

vetor3 <- c("Maria", "João", "Pedro", "Paulo", "Sandra")
vetor3 # ou usar print(vetor3)

# Matriz
matriz1 <- matrix(1:8, nrow=4, ncol=2)
matriz1

matriz2 <- matrix(c(15, 18, 13, 17, 15, 12, 21, 20, 22),
                  nrow=3,
                  ncol=3)
matriz2

# Array:
array1 <- array(1:12, dim=c(2,3,2))
array1

# Dataframe (Tabela):
clientes <- data.frame(Nome=c("Andre", "Paulo", "Gustavo", "Daniela", "Roger", "Caio"),
                       idade=c(32, 24, 12, 30, 47, 3),
                       Sexo=c("M", "M", "M", "F", "M", "M"),
                       Escolaridade=c("Graduado", "Graduando", "Fundamental", "Pós-Graduada", "EJA", "Maternal"),
                       Estado=c("SP", "RJ", "MG", "BH", "SP", "SP"),
                       Profissão=c("Influencer", "Borracheiro", "Gamer", "Empresária", "CEO", "Herdeiro"),
                       Renda=c("R$ 30.000,00", "R$ 13.000,00", "R$ 4.000,00", "R$ 60.000,00", "R$ 20.000,00", "R$ 3.000,00"))
clientes

clientes_atualizada <- rbind(clientes,
                             data.frame(Nome="Fagner",
                                       idade=32,
                                       Sexo="M",
                                       Escolaridade="Graduado",
                                       Estado="SP",
                                       Profissão="Engenheiro",
                                       Renda="R$ 7.000,00"))

# Lista:
lista <- list(clientes,
              matriz2,
              vetor3,
              exemplo <- c(5, 8, 9, 7))
lista

# Localizando Diretorio do R (WorkSpace):
getwd()

# Importandos Bases De Dados:
dados1 <- read.table("DadosAula.txt", header=T)
dados1

# CSV:
dados2 <- read.csv2("DadosAula.csv")
dados2

# XLSX:
install.packages("openxlsx") # Instalar Pacote
library(openxlsx) # Habilita Pacote

dados3 <- read.xlsx("DadosAula.xlsx")
dados3
