document.addEventListener('DOMContentLoaded', () => {
    const searchOpen = document.querySelector('.js-search-open');
    const searchClose = document.querySelector('.js-search-close');
    const searchWrap = document.querySelector(".js-search-form-wrap");
  
    searchOpen.addEventListener("click", (e) => {
      e.preventDefault();
      searchWrap.classList.add("active");
    });
  
    searchClose.addEventListener("click", (e) => {
      e.preventDefault();
      searchWrap.classList.remove("active");
    });
  });
  