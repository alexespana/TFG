let itemActive;

/**
 * Auxiliary function to select web page elements that comply
 * with the selector
 *
 * @param {string} selector Selector of the desired node
 * @param {boolean} all Indicates whether all offspring should be selectes or not
 * @returns Descendant nodes or the first node of the node that satisfies the selector
 */
 const select = (selector, all = false) => {
  if (all) {
    return [...document.querySelectorAll(selector)]
  } else {
    return document.querySelector(selector)
  }
}

/**
 * Auxiliary function to add an Event listener to a given
 * node(s)
 * 
 * @param {string} typeOfEvent Type of event
 * @param {string} selector Selector of the desired node
 * @param {function} listener Function that will perform a certain action for the event
 * @param {boolean} all Indicates whether all offspring should be selectes or not
 */
  const on = (typeOfEvent, selector, listener, all = false) => {
  let selectedElements = select(selector, all)
  if (selectedElements) {
    if (all) {
      selectedElements.forEach(e => e.addEventListener(typeOfEvent, listener))
    } else {
      selectedElements.addEventListener(typeOfEvent, listener)
    }
  }
}

/**
 * Checks which navbar item is the current one
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
 * Function that modifies the session variable itemActive to
 * store the current item
 *
 * @param {int} index Index of selected navbar
 */
function navbarLinkActive(index){
  itemActive = index;
  sessionStorage.setItem("itemActive", index);
}

/**
 * Function that changes the active navbar item and desactivates
 * the previous one
 */
function _changeNavBarItem(){
  let navbarLinks = select('.navbar .nav-link', true)
  navbarLinks.forEach((item, index) => {
    if (index==itemActive) {
      item.classList.add('active')
    } else {
      item.classList.remove('active')

      if( (itemActive>1 && itemActive <12 && index==1) ||
          (itemActive>13 && itemActive<24 && index==13)
      ){
        item.classList.add('active')
      }

      if( (itemActive>5 && itemActive<8 && index==5) ||
           (itemActive>9 && itemActive<12 && index==9) ||
           (itemActive>17 && itemActive<20 && index==17) ||
           (itemActive>21 && itemActive<24 && index==21)         
      ){
        item.classList.add('active')
      }
    }
  });
}

/**
 * Carousel indicators
 */
let carouselIndicators = select("#carousel-indicators")
let carouselItems = select('.carousel-item', true)

carouselItems.forEach((_, index) => {
  (index === 0) ?
  carouselIndicators.innerHTML += "<li data-bs-target='#indicators' data-bs-slide-to='" + index + "' class='active'></li>":
  carouselIndicators.innerHTML += "<li data-bs-target='#indicators' data-bs-slide-to='" + index + "'></li>"
});

/**
 * Function that changes classes related to the navbar in
 * mobile view
 */
function navbarPhone(){
  select('#navbar').classList.toggle('phone-navbar')
  select('#navbar ul').classList.toggle('border-box')
  this.classList.toggle('bi-list')
  this.classList.toggle('bi-x-circle')
}

// Onclick listener
document.getElementsByClassName('phone-toggle')[0].onclick = navbarPhone

/**
 * Function that adds the active-dropdown class to navbar dropdowns
 */
function navbarDropdown(){
  if (select('#navbar').classList.contains('phone-navbar')) 
    this.nextElementSibling.classList.toggle('active-dropdown')
}

// Add an event listener
on('click', '.navbar .dropdown > a', navbarDropdown, true)