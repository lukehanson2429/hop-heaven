// Prevent multiple submits on Rating Submission
$('.prevent_multiple').click(function() {
    var old_width = $(this).width();                                // store original width
    $(this).html('<i class="fa fa-refresh fa-lg fa-spin"></i>');    // replace button text with icon
    $(this).width(old_width);                                       // restore original width
    $(this).prop('disabled', true);                                 // disable the button
    $(this).parents('form:first').submit();                         // submit the form
    $(this).trigger("reset");
});