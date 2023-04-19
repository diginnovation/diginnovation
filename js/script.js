$(document).ready(function () {
  // grab the initial top offset of the navigation
  var stickyNavTop = $(".nav").offset().top;

  // our function that decides weather the navigation bar should have "fixed" css position or not.
  var stickyNav = function () {
    var scrollTop = $(window).scrollTop(); // our current vertical position from the top

    // if we've scrolled more than the navigation, change its position to fixed to stick to top,
    // otherwise change it back to relative
    if (scrollTop > stickyNavTop) {
      $(".nav").addClass("sticky");
    } else {
      $(".nav").removeClass("sticky");
    }
  };

  stickyNav();
  // and run it again every time you scroll
  $(window).scroll(function () {
    stickyNav();
  });
});

$(".scroll").on("click", function (event) {
  event.preventDefault();
  $("html,body").animate({
    scrollTop: $(this.hash).offset().top - 130,
  });
});

$("#navbarSupportedContent .nav-item .nav-link").on("click", function () {
  $(".navbar-collapse").collapse("hide");
});

// atur waktu akhir countdown
var countDownDate = new Date("June 28, 2023 00:00:00").getTime();

// perbarui countdown setiap 1 detik
var x = setInterval(function () {
  // dapatkan waktu saat ini
  var now = new Date().getTime();

  // hitung selisih waktu antara sekarang dan waktu akhir countdown
  var distance = countDownDate - now;

  // hitung waktu untuk jam, menit, dan detik
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // tampilkan waktu pada elemen countdown timer
  document.getElementById("countdown-timer").innerHTML =
    days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

  // jika waktu countdown telah habis, tampilkan pesan
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown-timer").innerHTML =
      "Selamat Hari Raya Idul Adha 2023.";
  }
}, 1000);
