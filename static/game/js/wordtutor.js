function quick_listen(e){
    var unicode = e.keyCode?e.keyCode:e.charCode;
    alert(unicode);
}
function bind_click_card(){
    $('.block-container').on('click',function(e){
        var div = $(this).children('.card');
        if (div.attr("class") == "block-level center card card-face"){
            div.attr("class","block-level center card card-hover");
            var str = div[0].style.webkitTransform;
            var str2 = div[0].style.transform;
            var patt1=new RegExp("rotate");
            if(patt1.test(str)){
                str = str.replace(/rotateX\((.*?)\)/g,'rotateX(180deg)');
            }
            else{
                str = str + ' rotateX(180deg)';
            }
            if(patt1.test(str2)){
                str2 = str2.replace(/rotateX\((.*?)\)/g,'rotateX(180deg)');
            }
            else{
                str2 = str2 + ' rotateX(180deg)';
            }
            var patt1=new RegExp("perspective");
            if(!patt1.test(str)){
                str = str + ' perspective(700px)';
            }
            if(!patt1.test(str2)){
                str2 = str2 + ' perspective(700px)';
            }
            div[0].style.webkitTransform = str;
            div[0].style.transform = str2;
            div.children('.title').attr("class","center-in word hide title");
            div.children('.features').attr("class","center-in word features");
        }
        else{
            div.attr("class","block-level center card card-face");
            var str = div[0].style.webkitTransform;
            var str2 = div[0].style.transform;
            var patt1=new RegExp("rotate");
            if(patt1.test(str)){
                str = str.replace(/rotateX\((.*?)\)/g,'');
            }
            if(patt1.test(str2)){
                str2 = str2.replace(/rotateX\((.*?)\)/g,'');
            }
            var patt1=new RegExp("perspective");
            if(!patt1.test(str)){
                str = str + ' perspective(700px)';
            }
            if(!patt1.test(str2)){
                str2 = str2 + ' perspective(700px)';
            }
            div[0].style.webkitTransform = str;
            div[0].style.transform = str2;
            div.children('.title').attr("class","center-in word title");
            div.children('.features').attr("class","center-in word hide features");
        }
    }); 
}
function add_callback(data){
    var module = "",
        data = JSON.parse(data);
    if (data['status'] == "OK"){
        $('#add_form input[type=reset]').trigger('click');
    }
    else{
        alert(data['error']);
    }
}
function set_callback(data){
    var module = "",
        data = JSON.parse(data);
    if (data['status'] == "OK"){
        $('#set_modal').modal('hide');
        window.location.reload();
    }
    else{
        alert(data['error']);
    }
}
function get_callback(data){
    var module = "",
        data = JSON.parse(data);
    var results = data['results'];
    $('#stage').empty();
    for (i=0;i<results.length;i++){
        var title = results[i].title;
        var features = results[i].features;
        var node = "<div class='block-container'>"+
                        "<div class='block-level center card card-face' id='no"+i+"'>"+
                            "<div class='center-in word title'>"+title+"</div>"+
                            "<div class='center-in word hide features'>"+features+"</div>"+
                        "</div>"+
                    "</div>";
        $('#stage').append(node);
    }
    $('#page').val(data['p']['page']);
    $('#classify').val(data['p']['classify']);
    $('#length').attr('width',results.length);
    bind_click_card();
}
function record_callback(data){
    var module = "",
        results = JSON.parse(data);
    $('#cihui').empty();
    for (i=0;i<results.length;i++){
        var classify = results[i].classify;
        var num = results[i].num;
        var node = "<div>" + classify + " : " + num + "</div>";
        $('#cihui').append(node);
    }
}
function mytransform(a,b){
    var width0 = $('#no1').width()+6;
    var height0 = 206;
    var width = (parseInt(b%5)-parseInt(a%5))*width0;
    var height = (parseInt(b/5)-parseInt(a/5))*height0;
    var div = $('#no'+a);
    if (div.attr("class") == "block-level center card card-hover"){
        div.attr("class","block-level center card card-face");
        div.children('.title').attr("class","center-in word title");
        div.children('.features').attr("class","center-in word hide features");
    }
    div[0].style.transform = 'translate('+width+'px,'+height+'px)';
    div[0].style.webkitTransform = 'translate('+width+'px,'+height+'px)';
}
$(function(){
    bind_click_card();
    var menuLeft = document.getElementById( 'menu' );
    var stage = document.getElementById('stage');
    var body = document.getElementsByTagName('body');
    addEvent(document.getElementById("stage"), 'mousemove', function(ev){
        var cursorPos = getMousePoint(ev);
        if (cursorPos.x < 10){
            classie.toggle( menuLeft, 'cbp-spmenu-open' );
            classie.toggle( stage, 'cbp-spmenu-push-toright' );
        }
    });
    $('#add-menu').on('click',function(){
        $('#add_form input[type=reset]').trigger('click');
        $('#input3').attr("value","");
    }); 
    $('.payer_name').on('click',function(){
        $('#input3').attr("value",$(this).attr("value"));
    });
    $('.orderby').on('click',function(){
        $('#input6').attr("value",$(this).attr("value"));
    });
    $('#add_save').on('click',function(){
        ajaxSubmit($('#add_form'),add_callback);
    });
    $('#set_save').on('click',function(){
        ajaxSubmit($('#set_form'),set_callback);
    });
    $('#confuse-menu').on('click',function(e){
        var length = $('#length').attr('width');
        if(length > 0){
            var present = _.range(length);
            var next = _.shuffle(present);
            for(var i=0;i<length;i++){
                mytransform(present[i],next[i]);
            }
        }
    });
    $('#paging-menu').on('click',function(e){
        var page = parseInt($('#page').val())+1;
        var classify = $('#classify').val();
        $.ajax({
            url: "/game/word-turn-over/get/",
            type: "GET", 
            data: {
                'classify':classify,
                'page':page
            },
            success:get_callback 
        });
    });
    $('#record-menu').on('click',function(){
        $.ajax({
            url: "/game/word-turn-over/record/",
            type: "GET", 
            data: {},
            success:record_callback 
        });
    }); 
    $('#close-menu').on('click',function(e){
        classie.toggle( menuLeft, 'cbp-spmenu-open' );
        classie.toggle( stage, 'cbp-spmenu-push-toright' );
    });
    $('.subclass').on('click',function(e){
        var page = 1;
        var classify = $(this).attr('value');
        $.ajax({
            url: "/game/word-turn-over/get/",
            type: "GET", 
            data: {
                'classify':classify,
                'page':page
            },
            success:get_callback 
        });
        $(".curclass").attr('class','subclass');
        $(this).attr('class','subclass curclass');
    });
    $('body').on('keyup',function(e){
        if(e.target == this){
            var unicode = e.keyCode?e.keyCode:e.charCode;
            if(unicode == 65)
                $('#add-menu').trigger('click');
            if(unicode == 83)
                $('#set-menu').trigger('click');
            if(unicode == 67)
                $('#confuse-menu').trigger('click');
            if(unicode == 80)
                $('#paging-menu').trigger('click');
            if(unicode == 82)
                $('#record-menu').trigger('click');
            if(unicode == 72)
                $('#close-menu').trigger('click');
        }
    });
});
