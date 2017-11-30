$(document).ready(function() {
     $('#agreeCheck').click(function() {
        if ($(this).is(':checked')) {
            $('#submitAbstract').removeAttr('disabled');  
        } else {
            $('#submitAbstract').attr('disabled', true);
        }
    });   

});