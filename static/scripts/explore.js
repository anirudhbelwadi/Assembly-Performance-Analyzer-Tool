$(".form-check-input").change(function () {
    var name = $(this).attr("name");
    if (name == "carbonFootprint") {
        if (!$(".constructionType").is(":checked")) {
            $("#constructionTypeNil").prop("checked", true);
        }
    }
});
$("#clearForm").click(function () {
    $(".constructionType").prop("required", true);
    $(".carbonFootprint").prop("required", false);
    $("#constructionTypeNil").prop("checked", true);
    $("#carbonFootprintNil").prop("checked", true);
});