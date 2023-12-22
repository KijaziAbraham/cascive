document.addEventListener('DOMContentLoaded', () => {
    const selectHeader = document.querySelector('#header');
  
    if (selectHeader) {
      document.addEventListener('scroll', () => {
        window.scrollY > 100 ? selectHeader.classList.add('sticked') : selectHeader.classList.remove('sticked');
      });
    }
  });
  