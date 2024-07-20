//console.log("Olá mundo!")

//const titulo = document
//console.log(document)

// const titulo = document.getElementById("titulo")
// console.log(titulo);

// const texto = document.getElementsByClassName("texto-simples");
// console.log(texto);

// //pelo seletor css
// const seguntoTitulo = document.querySelector("div h2");
// console.log(seguntoTitulo);

// const textosPorClasse = document.querySelectorAll(".texto-simples");
// console.log(textosPorClasse)

//InnerText - retorna o texto sem formatação e sem elementos html
//InnerHTML - retorna o texto com formatação e com elementos html

// let elementoH1 = document.querySelector("h1");
// console.log(elementoH1);
// console.log(elementoH1.innerText);

// let elementoMain = document.querySelector("main");
// console.log(elementoMain);
// console.log(elementoMain.innerText);
// console.log(elementoMain.innerHTML);

// let elementoH1 = document.querySelector("h1");
// elementoH1.innerText = "Novo título com JS";

// let elementoMain = document.querySelector("main");
// elementoMain.innerHTML = `
//     <h2>Novo subtítulo</h2>
//     <ul>
//     <li>Elemento 1</li>
//     <li>Elemento 2</li>
//     <li>Elemento 3</li>
//     </ul>
// `;

//Criando Elemento com JS

//criar elemento
let novoElemento = document.createElement("li");
novoElemento.innerText = "JavaScript";
//console.log(novoElemento)
novoElemento.id = "ling-js";
console.log(novoElemento)
//adicionando elemento via dom
let listaLinguagens = document.querySelector(".lista-linguagens");
listaLinguagens.appendChild(novoElemento);

//adicionando elementos complexos
const postagemJavaScript = document.createElement("div");
postagemJavaScript.innerHTML = `
    <h2 class="post-titulo">JavaScript</h2>
    <p class="post-texto">JavaScript é uma linguagem de programação</p>
`;

//capturando elemento pai
const postagens = document.querySelector(".postagens");
//adicionando elemento
postagens.appendChild(postagemJavaScript);
