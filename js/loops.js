/*
for (let i=0; i<10; i++){
    console.log(i)
}
    */
   /*
//percorrer array
let letras = ['a', 'b', 'c']
console.log(letras.length)

for (let i = 0; i <letras.length; i++){
    console.log(letras[i]);
}

*/
let numerosDaSorte = [37, 14, 26, 5, 94, 87]  

for (let numero of numerosDaSorte){
  if (numero %2 ==0 && numero <50){
    console.log(`${numero} é par e menor que 50`)
  }  else if (numero <50){
    console.log(`${numero} é menor que 50`)
  } else{
    console.log(`${numero} é maior que 50`)
  }
}
