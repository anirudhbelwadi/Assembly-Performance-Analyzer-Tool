$('.navbar-nav>li>a').on('click', function () {
    $('.navbar-collapse').collapse('hide');
});
$('.navbar-toggler').on('click', function () {
    var scroll_amount = $(window).scrollTop();
    if (scroll_amount < 50) {
        $('.navbar').addClass('navbar_color');
    }
});
$(".bi-arrow-up-circle-fill").hide();
$(window).scroll(function () {
    var scroll_amount = $(window).scrollTop();
    if (scroll_amount > 50) {
        $(".navbar").addClass('navbar_resize');
        $(".navbar").removeClass('navbar_noresize');
        $('.navbar').addClass('navbar_color');
        $(".navbar img").addClass('navbar_logo_resize');
        $(".navbar img").removeClass('navbar_logo_noresize');
        $(".navbar-toggler").addClass('navbar_toggler_resize');
        $(".navbar-toggler").removeClass('navbar_toggler_noresize');
        $(".bi-arrow-up-circle-fill").fadeIn();
    }
    if (scroll_amount == 0) {
        $(".navbar").removeClass('navbar_resize');
        $(".navbar").addClass('navbar_noresize');
        $('.navbar').removeClass('navbar_color');
        $(".navbar img").removeClass('navbar_logo_resize');
        $(".navbar img").addClass('navbar_logo_noresize');
        $(".navbar-toggler").removeClass('navbar_toggler_resize');
        $(".navbar-toggler").addClass('navbar_toggler_noresize');
        $(".bi-arrow-up-circle-fill").fadeOut();
    }
});
var scroll_amount = $(window).scrollTop();
if (scroll_amount > 50) {
    $(".navbar").addClass('navbar_resize');
    $(".navbar").removeClass('navbar_noresize');
    $('.navbar').addClass('navbar_color');
    $(".navbar img").addClass('navbar_logo_resize');
    $(".navbar img").removeClass('navbar_logo_noresize');
    $(".navbar-toggler").addClass('navbar_toggler_resize');
    $(".navbar-toggler").removeClass('navbar_toggler_noresize');
    $(".bi-arrow-up-circle-fill").fadeIn();
}
if (scroll_amount == 0) {
    $(".navbar").removeClass('navbar_resize');
    $(".navbar").addClass('navbar_noresize');
    $('.navbar').removeClass('navbar_color');
    $(".navbar img").removeClass('navbar_logo_resize');
    $(".navbar img").addClass('navbar_logo_noresize');
    $(".navbar-toggler").removeClass('navbar_toggler_resize');
    $(".navbar-toggler").addClass('navbar_toggler_noresize');
    $(".bi-arrow-up-circle-fill").fadeOut();
}