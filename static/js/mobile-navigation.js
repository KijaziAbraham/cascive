document.addEventListener('DOMContentLoaded', () => {
    const mobileNavToogleButton = document.querySelector('.mobile-nav-toggle');
  
    if (mobileNavToogleButton) {
      mobileNavToogleButton.addEventListener('click', function (event) {
        event.preventDefault();
        mobileNavToogle();
      });
    }
  
    function mobileNavToogle() {
      document.querySelector('body').classList.toggle('mobile-nav-active');
      mobileNavToogleButton.classList.toggle('bi-list');
      mobileNavToogleButton.classList.toggle('bi-x');
    }
  
    document.querySelectorAll('#navbar a').forEach(navbarlink => {
      if (!navbarlink.hash) return;
  
      let section = document.querySelector(navbarlink.hash);
      if (!section) return;
  
      navbarlink.addEventListener('click', () => {
        if (document.querySelector('.mobile-nav-active')) {
          mobileNavToogle();
        }
      });
    });
  
    const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');
  
    navDropdowns.forEach(el => {
      el.addEventListener('click', function (event) {
        if (document.querySelector('.mobile-nav-active')) {
          event.preventDefault();
          this.classList.toggle('active');
          this.nextElementSibling.classList.toggle('dropdown-active');
  
          let dropDownIndicator = this.querySelector('.dropdown-indicator');
          dropDownIndicator.classList.toggle('bi-chevron-up');
          dropDownIndicator.classList.toggle('bi-chevron-down');
        }
      });
    });
  });
  