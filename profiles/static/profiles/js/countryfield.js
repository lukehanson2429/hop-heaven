// Countryfield change color as per Boutique Ado project with custom color 
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#777777');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#777777');
    } else {
        $(this).css('color', '#000');
    }
});