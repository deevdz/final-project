//Add and remove classes to the class event-section based on the screen size of the device
jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 568) {
        $('.event-section').removeClass('p-5');
        $('.event-section').addClass('p-1');
        $('.event-section').addClass('pt-5');
        $('.event-section').addClass('pb-5');
    } else if (ww >= 568) {
        $('.event-section').removeClass('p-1');
        $('.event-section').removeClass('pt-5');
        $('.event-section').removeClass('pb-5');
        $('.event-section').addClass('p-5');
    };
  };
  $(window).resize(function(){
    alterClass();
  });
  //Fire it when the page first loads:
  alterClass();
});