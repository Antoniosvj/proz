const titulo = document.getElementById("titulo");
titulo.innerText = "Titulo do Exercício";

const linkExercicio = document.querySelector("a")
linkExercicio.innerText = "link exercício";

const listaOrdenada = document.querySelector("ol");
listaOrdenada.innerHTML = `
    <li>item 1 lista ordenanda</li>
    <li>item 2 lista ordenanda</li>
    <li>item 3 lista ordenanda</li>
    `;
const listaNaoOrdenada = document.querySelector("ul");
listaNaoOrdenada.innerHTML = `
    <li>Item 1 lista não ordenada</li>
    <li>Item 2 lista não ordenada</li>
    <li>Item 3 lista não ordenada</li>
`;
