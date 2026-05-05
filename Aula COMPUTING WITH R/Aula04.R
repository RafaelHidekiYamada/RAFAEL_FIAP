# Criando a base de dados:
dados <- c(rep(14,6), rep(15,12), rep(16, 9), rep(17,3))

# Frequencia Absoluta(fi):
fi <- table(dados)
fi

# Frequencia Absoluta Acumulada(fia):
fia <- cumsum(fi)
fia

# Frequencia Relativa(fr):
fr <- prop.table(fi)*100
fr

# Frequencia Relativa Acumulada(fra):
fra <- cumsum(fr)
fra

# Total das Colunas:
nfi <- c(fi, sum(fi))
nfia <- c(fia, "-")
nfr <- c(fr, sum(fr))
nfra <- c(fra, "-")

# Nome "Total" na ultima linha:
names(nfi)[length(nfi)] <- "Total"
names(nfia)[length(nfi)] <- "Total"
names(nfr)[length(nfr)] <- "Total"
names(nfra)[length(nfra)] <- "Total"