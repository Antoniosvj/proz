let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
valorSubtotal.innerText = subtotalInfo.valor;


let btnAddProduts = document.querySelector("#btn-adicionar-produto-01");
//console.log(btnAddProduto);

let btnSubProduts = document.querySelector("#btn-subtrair-produto-01");
//console.log(btnSubProduts);

let qtdProducts = document.querySelector("#quantidade-produto-01");
//console.log(qtdProducts)

function addOne(){
  qtdProducts.value ++;
  //atualizar o dom
  subtotalInfo.quantidade++;
  subtotalInfo.valor +=11.66;
  attSubtotal();
}

btnAddProduts.addEventListener('click', addOne);

function subOne(){
 if (qtdProducts.value >1){
  qtdProducts.value--;
  //atualizar o dom
  subtotalInfo.quantidade--;
  subtotalInfo.valor -=11.66;
  attSubtotal();
 }
}

btnSubProduts.addEventListener('click', subOne);

function attSubtotal(){
  quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
  valorSubtotal.innerText = subtotalInfo.valor.toFixed(2);
}