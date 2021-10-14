// Countryfield change color of select element as per boutique ado
let countrySelected = $('#id_country').val();
if(!countrySelected) {
    $('#id_country').css('color', '#777777');
};
$('#id_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#777777');
    } else {
        $(this).css('color', '#000');
    }
});