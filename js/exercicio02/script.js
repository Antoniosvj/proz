/*
 e um elemento que represente um produto à venda. O produto precisa incluir pelo menos o nome, a descrição e o preço. Pode incluir outros "elementos filhos" se achar necessário como, por exemplo, uma imagem. Procure usar o método simples e o método complexo, ensinados neste tópico.*/

//metodo simples
let titulo = document.createElement("h1")
titulo.innerText = "Mercadinho Livre";
titulo.id = "titulo";

//metodo complexo
bola = ['Bola Futebol', 'Bola para Jogar futebol', '129,90', './transferir.jpeg']

let produto = document.createElement("section");
produto.innerHTML = `
    <h2 id="produtoTitulo">${bola[0]}</h2>
    <p>${bola[1]}</p>
    <img src="${bola[3]}">
    <h3>${bola[2]}</h3>
`;

//adicionando no site
const bodySite = document.querySelector("body");
bodySite.appendChild(titulo);
bodySite.appendChild(produto);


