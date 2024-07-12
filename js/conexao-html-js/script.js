const logotipo = document.getElementById("logo")
console.log(logotipo) /*verificar se recuperou*/

const autor = document.getElementsByClassName("post-autor")
console.log(autor)

const post2 = document.getElementById("post02")
console.log(post2)

const formulario = document.getElementById("formulario")
console.log(formulario)

const ambosPosts = document.getElementById("posts")
console.log(ambosPosts)

const datas = document.getElementsByClassName("post-data")
console.log(datas)

const texto = document.getElementsByClassName("post-texto")
console.log(texto)

const redesSociais = document.getElementsByClassName("lista_redes")
console.log(redesSociais)

const textoPost02 = document.querySelector("article .post-texto")
console.log(textoPost02)


const linkPost01 = document.querySelector("#post01 .post-texto a")
console.log(linkPost01)

const negrito = document.querySelector("#post02 .post-texto strong")
console.log(negrito)

const nomeForm = document.querySelector("#formulario form #nome")
console.log(nomeForm)

const listaFinal = document.querySelectorAll("footer .lista_redes a")
console.log(listaFinal)

const linknavegacao = document.querySelectorAll(".elementos_nav a")
console.log(linknavegacao)

const negritos = document.querySelectorAll(".post-autor strong, .post-data strong")
console.log(negritos)