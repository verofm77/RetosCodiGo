//L: Cantidad de litros que produce. Entero
//PG: Precio del galón. Real
//TG: Cantidad de galones que produce. Real
//GA: Ganancia por la entrega de leche. Real


let L = +prompt("Cantidad de litros que produce")
let PG = parseFloat(prompt("Precio del galón"))

let TG=(L/3.785)
let GA=PG*TG

//console.log("Ganancia: " + GA)

alert("Galones producido: " + L + " Ganancia: S/." + GA)