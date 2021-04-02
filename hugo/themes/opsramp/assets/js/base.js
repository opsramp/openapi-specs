(function ($) {

    'use strict';

    const preloader = document.querySelector('.page-loader');

    const fadeEffect = setInterval(() => {
      // if we don't set opacity 1 in CSS, then   //it will be equaled to "", that's why we   // check it
      if (!preloader.style.opacity) {
        preloader.style.opacity = 1;
      }
      if (preloader.style.opacity > 0) {
        preloader.style.opacity -= 0.1;
      } else {
        preloader.remove()
        clearInterval(fadeEffect);
      }
    }, 20);

    window.addEventListener("load", () => fadeEffect);

    function bottomPos(element) {
        return element.offset().top + element.outerHeight();
    }

    function submitFeedback(form, data) {
      console.log(form.action);
      console.log(data);

      $.post(form.action, data, null, "json")
      .done(function(data) {
        console.log(data);
        $('#feedback-success').slideDown('slow');
        setTimeout(function() {
          jQuery('#feedbackForm').modal('hide')
        }, 2000);
      }).fail(function(jqXHR, textStatus) {
        console.log(jqXHR);
        console.log(textStatus);
        $('#feedback-error').slideDown('slow');
        $("#err-state").html('An error occurred: ' + textStatus + '');
      });
    }

    $(function() {
      let form = $("#feedback-form");
      form.submit(function(event) {
        event.preventDefault();
        submitFeedback(this, form.serialize());
      });
    });

    $("#toggle-sidebar").on("click", function () {
      $("body").toggleClass("sidebar-active");
      $(this).toggleClass("collapsed"), $("#sidebar, #content").toggleClass("active"), $(".collapse.in").toggleClass("in")
      /*
      let currentState = getCookie("sbSt")
      if ("true" == currentState) {
        document.cookie = "sbSt=false";
      } else {
        document.cookie = "sbSt=true";
      } */
    })

    /*
    const getCookie = ckId => {
      let decodedCookie = decodeURIComponent(document.cookie)
      let ca = decodedCookie.split(";")

      for(var i = 0; i <ca.length; i++) {
        var c = ca[i].split("=")
        if (ckId == c[0]) {
          console.log(c[0])
          return c[1];
        }
      }
      return "";
    }

    let state = getCookie("sbSt")
    console.log("On Page Load:")
    console.log(state)

    if ("true" == state) {
      $("body, #sidebar, #content").removeClass("sidebar-active")
      $("#toggle-sidebar").addClass("collapsed")
      $(".collapse.in").removeClass("in")
    } */

}(jQuery));
