# Exemplo 1:

idade <- 18
TemCarteira <- TRUE

if(idade >= 18 & TemCarteira){
  print("Pode dirgir")
} else {
  print("Não pode dirigir")
}

# Exemplo 2
ifelse(idade >= 18 & TemCarteira,
       "Pode Dirigir",
       "Não pode dirgir")

# Exemplo 3
 nota <- 6
 frequencia <- 75
 
 if(nota >= 7 & frequencia >= 75){
   print("Aprovado!")
 } else if(nota >= 5 && frequencia >= 75){
   print("Recuperação!")
 } else {
   print("Reprovado!")
 }
 
 #or
 
 ifelse(nota >= 7 & frequencia >= 75, "Aprovado",
        ifelse(nota >= 5 & frequencia >= 75, "Recuperação",
               "Reprovado"))
 
 # Exemplo 4
 tem_cafe <- FALSE
 if(!tem_cafe){
   print("Precisamos de mais café")
 } else {
   print("Já temos café suficente")
 }