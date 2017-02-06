// var c = {{c|safe}};
// $('#result').html(c);

$(function(){

    // var c = {{c|safe}};
    // $('#result').html(c);
    $('#add').click(function(){
        //alert('jquery test');
        var a= $('#a').val();
        var b= $('#b').val();
        // $.get(url,数据,处理函数) ajax的get方法， 
        // function(reponse.status,xht) 
        // responseText 返回的内容
        // textStatus (请求状态)
        // XMLHttpRequest(XMLHttpRequest 对象)
        $.get('/ajax_add/',{'a':a,'b':b},function(reponse,status,xhr){
            alert(reponse);
            $('#result').html('reponse');
        });
    });
    $('#ajaxjz').click(function(){
        alert('ajaxjz');
        $.getJSON("/ajax_dict/",function(ret){
            alert(ret);
            $('#ajaxresult').append(ret.subl+'<br>');
        });
    });
});