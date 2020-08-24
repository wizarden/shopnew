$(document).ready(function(){

    t = $(".mysend");

    t.on('click', function(e){
       
        var data = {};
        var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        data["csrfmiddlewaretoken"] = csrf_token;

        url=t.data('url');

        for (g in t.data()) {
            data[g] = t.data(g)
        }
        console.log(data);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("Ok");
            },
            error: function(){
                console.log("error")
            }
        })


    })
});