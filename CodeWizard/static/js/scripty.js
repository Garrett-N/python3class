
$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault()
        var form = $('#register-form').serialize();
        $.ajax({
            url : '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log("Success:")
                console.log(response);
            },
            error: function(errormsg) {
                console.log("Error:")
                console.log(errormsg)
            }
        });
    });
});
