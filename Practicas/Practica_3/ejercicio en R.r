nombres <- c("Juan", "María", "Pedro", "Ana")
edades <- c(25, 30, 28, 35)

persona_mas_joven <- function(nombres, edades) {
  indice <- which.min(edades)
  return(nombres[indice])
}

nombre_mas_joven <- persona_mas_joven(nombres, edades)
edad_mas_joven <- min(edades)
cat("La persona más joven es", nombre_mas_joven, "con", edad_mas_joven, "años.")