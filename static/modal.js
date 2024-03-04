document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById("myModal");
  var mainImage = document.getElementById("main-image");
  var modalImage = document.getElementById("modal-image");
  var span = document.getElementsByClassName("close")[0];
  var galleryImages = Array.from(document.getElementById("image-bar").children);

  var selectedImage = galleryImages[0];
  selectedImage.setAttribute("id", "selected");

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

  galleryImages.forEach(image => {
    image.onclick = function(event) {
      if(image.getAttribute("id") === "selected")
        return;

      // Update image attributes
      selectedImage.removeAttribute("id");
      selectedImage = image;
      selectedImage.setAttribute("id", "selected");

      // Update image display
      var selectedSource = selectedImage.getAttribute("src")
      mainImage.setAttribute("src", selectedSource);
      modalImage.setAttribute("src", selectedSource);
    }
  });
});