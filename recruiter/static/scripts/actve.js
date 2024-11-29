 // Get all the navigation links
 const navLinks = document.querySelectorAll('.nav-link');

 // Get the current page URL
 const currentPage = window.location.pathname;

 // Loop through the links and add the 'active' class to the one that matches the current page
 navLinks.forEach(link => {
   if (link.getAttribute('href') === currentPage) {
     link.classList.add('active');
   }
 });