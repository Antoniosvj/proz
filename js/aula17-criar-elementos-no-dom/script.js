const arrayPostagens = [
  {
    titulo: "Pop Vegan",
    subtitulo: "Comida vegana para todos!",
    data: "06/07/2022",
    texto: "Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)"
  },
  {
    titulo: "Make Hommus. Not War",
    subtitulo: "Só delivery, para curtir em casa!",
    data: "18/08/2022",
    texto: "Neste restaurante não só pode, como é encorajado comer o antepasto como prato principal. Recomendamos os kibes e a kafta bonina."
  },
  {
    titulo: "Churrascada do Mar",
    subtitulo: "Melhor do que estar na praia!",
    data: "30/08/2022",
    texto: "Todos conhecemos e amamos um bom churrasco, mas o que você acha de experimentar um churrasco focado em frutos do mar? Nós gostamos, experimente e nos conte o que você achou!"
  },
];
/*
// Selecione o elemento main
const main = document.querySelector("main");

// Iterar sobre o array e criar o HTML para cada postagem
arrayPostagens.forEach(postagem => {
  // Cria um novo elemento article para cada postagem
  const artigo = document.createElement("article");
  artigo.innerHTML = `
    <h3>${postagem.titulo}</h3>
    <p class="subtitulo">${postagem.subtitulo}</p>
    <div class="data">${postagem.data}</div>
    <p>${postagem.texto}</p>
  `;
  
  // Adiciona o novo artigo ao final do main
  main.appendChild(artigo);
});

*/


// Selecione o elemento main
const main = document.querySelector("main");

// Usar um loop for para iterar sobre o arrayPostagens
for (let i = 0; i < arrayPostagens.length; i++) {
  const postagem = arrayPostagens[i];

  // Cria um novo elemento article para cada postagem
  const artigo = document.createElement("article");
  artigo.innerHTML = `
    <h3>${postagem.titulo}</h3>
    <p class="subtitulo">${postagem.subtitulo}</p>
    <div class="data">${postagem.data}</div>
    <p>${postagem.texto}</p>
  `;
  
  // Adiciona o novo artigo ao final do main
  main.appendChild(artigo);
}
