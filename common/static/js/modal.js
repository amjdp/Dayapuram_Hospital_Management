	// Select modal
    // var modal = document.getElementById('modalBox');

    // Select trigger link
    // var mpLink = document.getElementById("modalLink");

    // Select close action element
    // var close = document.getElementsByClassName("close")[0];

    // Open modal once the link is clicked
    // mpLink.onclick = function () {
    //     modal.style.display = "block";
    // };

    // Close modal once close element is clicked
    // close.onclick = function () {
    //     modal.style.display = "none";
    // };

    // Close modal when user clicks outside of the modal box
    // window.onclick = function (event) {
    //     if (event.target == modal) {
    //         modal.style.display = "none";
    //     }
    // };



    // Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
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