//TI: Tipo de hamburguesa. String
//N: Número de hamburguesas. Entero
//TP: Tipo de pago. String
//PA: Precio de la hamburguesa. Real
//CA: Cargo por uso de tarjeta. Real
//TO: Total sin cargo. Real
//TOT: Total con cargo. Real

let N = +prompt("Cantidad de hamburguesas7")
let TI = prompt("Tipo de hamburguesa. S-Sencilla D-Doble T-Triple")
let TP = prompt("Tipo de pago EF-Sin cargo TJ-Con Cargo")

switch(TI){
    case "S":
        PA=20 
        TO=PA*N
        switch(TP){
            case "TJ":
                CA=TO*0.05
                break;
            case "EF":
                CA=0
                break;
            default:
                alert("Ingresar valor TJ o EF")
        }
        break;
    case "D":
        PA=25
        TO=PA*N
        switch(TP){
            case "TJ":
                CA=TO*0.05
                break;
            case "EF":
                CA=0
                break;
            default:
                alert("Ingresar valor TJ o EF")
        }
        break;
    case "T":
        PA=28
        TO=PA*N
        switch(TP){
            case "TJ":
                CA=TO*0.05
                break;
            case "EF":
                CA=0
                break;
            default:
                alert("Ingresar valor TJ o EF")
        }
        break;
    default:
        alert("Ingresar valor S, D o T")
}
TOT=TO+CA
alert("Cuenta Detallada: Tipo: " + TI + "  Cantidad: " + N + "  Pago: " + TP + "  Precio: S/." + PA + "  Total a pagar: S/." + TOT)
