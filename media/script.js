$(document).ready(function(){
  $("#box").fadeIn();
  $("#screen").fadeIn();
  $("#fullscreen").click(function() {
    $("#box").fadeIn();
    $("#screen").fadeIn();
  });
  if ($("#box").is(":visible")) {
    $("#screen").click(function() {
      $("#screen").fadeOut();
      $("#box").fadeOut();
    });
  }
});