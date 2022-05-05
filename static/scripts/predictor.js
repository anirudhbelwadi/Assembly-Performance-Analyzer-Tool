$(".form-select").change(function () {
    var details = ['window', 'curtain_wall', 'balcony_roof', 'opaque_wall', 'roofing']
    var id = $(this).attr("id");
    $("#" + id).prop("required", true);
    for (var i = 0; i < 5; i++) {
        if (details[i] != id) {
            if ($("#" + details[i]).val() == "") {
                $("#" + details[i]).prop("required", true)
            }
            else {
                $("#" + details[i]).prop("required", false)
            }
        }
    }
});
$("#clearForm").click(function () {
    var details = ['window', 'curtain_wall', 'balcony_roof', 'opaque_wall', 'roofing']
    $("#" + details[0]).prop("required", true);
    for (var i = 1; i < 5; i++) {
        $("#" + details[i]).prop("required", false);
    }
});