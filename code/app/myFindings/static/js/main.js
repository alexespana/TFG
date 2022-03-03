let itemActive;

/**
 * Función auxiliar para seleccionar elementos de la página web
 * que cumplan el selector
 * 
 * @param {string} selector Selector del nodo deseado
 * @param {boolean} all Indica si se deben seleccionar todos los descendientes o no
 * @returns Nodos descendientes o el primer nodo del nodo que cumple el selector 
 */
 const select = (selector, all = false) => {
  if (all) {
    return [...document.querySelectorAll(selector)] 
  } else {
    return document.querySelector(selector)
  }
}

/**
 * Comprueba qué item del navbar es el actual
 */
if(sessionStorage.getItem("itemActive")){
  itemActive = sessionStorage.getItem("itemActive")
  _changeNavBarItem()
}
else{
  itemActive = 0
  sessionStorage.setItem("itemActive", 0)
  _changeNavBarItem()
}

/**
 * Función que modifica la variable de sesión itemActive
 * para almacenar el item actual
 * 
 * @param {int} index Índice del navbar seleccionado
 */
function navbarLinkActive(index){
  itemActive = index;
  sessionStorage.setItem("itemActive", index);
}

/**
 * Cambia el navbar activo y desactiva el anterior
 */
function _changeNavBarItem(){
  let navbarLinks = select('.navbar .nav-link', true)
  navbarLinks.forEach((item, index) => {
    if (index==itemActive) {
      item.classList.add('active')
    } else {
      item.classList.remove('active')
    }
  });
}

/**
 * Indicadores del Carousel
 */
let carouselIndicators = select("#carousel-indicators")
let carouselItems = select('.carousel-item', true)

carouselItems.forEach((_, index) => {
  (index === 0) ?
  carouselIndicators.innerHTML += "<li data-bs-target='#indicators' data-bs-slide-to='" + index + "' class='active'></li>":
  carouselIndicators.innerHTML += "<li data-bs-target='#indicators' data-bs-slide-to='" + index + "'></li>"
});

/**
 * Phone toggle
 */
function navbarPhone(){  
  select('#navbar').classList.toggle('phone-navbar')
  select('#navbar ul').classList.toggle('border-box')
  this.classList.toggle('bi-list')
  this.classList.toggle('bi-x-circle')
}

// Onclick listener
document.getElementsByClassName('phone-toggle')[0].onclick = navbarPhone
