const voltar = document.getElementById('voltar-index')
document.addEventListener('keyup', (e) =>{

  if(e.code == 'Backspace'){
    voltar.click()
  }
})