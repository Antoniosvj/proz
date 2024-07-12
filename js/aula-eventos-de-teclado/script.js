const linkPerfil = document.getElementById("link-perfil");
const navPerfil = document.getElementById("nav-perfil");

linkPerfil.addEventListener("mouseover", ()=> { //evento quando passa o mouse por cima
  navPerfil.style.display = "block"
})

linkPerfil.addEventListener("mouseout", ()=> { //evento quando passa o mouse por cima
  navPerfil.style.display = "none"
})

// document.addEventListener('keyup',(e) =>{
//   console.log(e.key) //pegar qual é a letra
//   console.log(e.code) //pegar qual o codigo da tecla

//   if (e.code == 'Digit1'){
//     //console.log('abrindo o menu de perfil')
//     navPerfil.style.display = 'block'
//   } else if (e.code == 'Escape'){
//     navPerfil.style.display = 'none'
//   }
// })

const linkPerfilDados = document.getElementById('link-perfil-dados')
 
document.addEventListener('keyup', (e) => {
  if(navPerfil.style.display == 'block'){
    if (e.code == 'Digit1'){
      linkPerfilDados.click()
    }
  } else if (e.code == 'Digit1'){
    navPerfil.style.display = 'block'
  }
 
})

