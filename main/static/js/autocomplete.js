var form = document.querySelector("#formReq");

$(document.querySelector("#formReq")).autocomplete({
        source : function(requete, reponse){ // les deux arguments représentent les données nécessaires au plugin
        $.ajax({
            source : '/ajax_calls/search/',
            minLength:2,
            dataType : 'json',
            data : {
            name_startsWith : $('#txtSearch').val(),
            maxRows : 15
            },
            
            success : function(data){
            reponse(data);
            }
    })
    }
});
