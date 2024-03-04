document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById("myModal");
  var mainImage = document.getElementById("main-image");
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks on the button, open the modal
  mainImage.onclick = function() {
    modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
});