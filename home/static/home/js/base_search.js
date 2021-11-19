$(document).ready(function () {

    csrf_token = $("[name='csrfmiddlewaretoken']").val()
            $.ajax({
                type: "post",
                dataType: "json",
                url: "/Search",
                data: {
                    csrfmiddlewaretoken: csrf_token,
                },
                success: function (response) {
                    
                    $("#search_").autocomplete({
                        lookup: response['values'],
                        onSelect:function(e){
                            $("#search_").val("");
                            window.location.href = e['data']['url']+'?query='+e["value"];
                        },
                        groupBy:"category",
                        minChars:2,
                        maxHeight:500,
                        forceFixPosition:true,
                        lookupLimit:8,
                        
                        
                    })
                },
                error: function(error){
                    console.error(error);
                }
            });


    $(".search_page").hide();
    $(".search_div").on("click", function (e) {
        $(".search_page").fadeIn();
    });
    $("#close_search").click(function (e) {
        $(".search_page").fadeOut();
    });
    $("#search_").on("keyup",function(){
        
    });
});