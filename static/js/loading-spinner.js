document.addEventListener("DOMContentLoaded", function () {
  // Assuming your loading spinner has an ID of 'loading-spinner'
  var loadingSpinner = document.getElementById('loading-spinner');

  // Show the loading spinner when the DOM is ready
  loadingSpinner.style.display = 'block';

  // Hide the loading spinner after a short delay (e.g., 1 second)
  setTimeout(function () {
      loadingSpinner.style.display = 'none';
  }, 1000);
});
