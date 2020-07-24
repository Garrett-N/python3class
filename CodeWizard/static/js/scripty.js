
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

    $(document).on("submit", '#login-form', function(e){
        e.preventDefault();
        var form = $(this).serialize();
        console.log(form)
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res) {
                if (res == "error"){
                    alert("Could not log in.");
                }else{
                    console.log("Logged in as ", res);
                }
            }
        })
    });
});
