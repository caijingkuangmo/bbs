/**
 * Created by Administrator on 2016/3/3.
 */
$(function () {
    $('#myTab li:eq(1) a').tab('show');

    /*$('#chouti-nav-left li').on('click',function(){
        if($(this).hasClass('nav-li-mouseon')){
            return
        }
        else{
            $(this).siblings().removeClass('nav-li-mouseon')
            $(this).siblings().addClass('hover')
            $(this).removeClass('hover')
            $(this).addClass('nav-li-mouseon')
        }

    });*/
    /*$('#chouti-nav-left li').on('mouseleave',function(){
          $(this).removeClass('nav-li-mouseon')
    });*/

    $('#hot-client_iphone').on('mouseover',function(){
        $(this).removeClass('hot-client_iphone')
        $(this).addClass('hot-client_iphone_on')
    });

     $('#hot-client_iphone').on('mouseleave',function(){
        $(this).removeClass('hot-client_iphone_on')
        $(this).addClass('hot-client_iphone')
    });

     $('#hot-client_android').on('mouseover',function(){
        $(this).removeClass('hot-client_android')
        $(this).addClass('hot-client_android_on')
    });

     $('#hot-client_android').on('mouseleave',function(){
        $(this).removeClass('hot-client_android_on')
        $(this).addClass('hot-client_android')
    });

    $('#hot-client_windows').on('mouseover',function(){
        $(this).removeClass('hot-client_windows')
        $(this).addClass('hot-client_windows_on')
    });

     $('#hot-client_windows').on('mouseleave',function(){
        $(this).removeClass('hot-client_windows_on')
        $(this).addClass('hot-client_windows')
    });

    $('#content-items').on('mouseover','.item-agree',function(){
        $(this).removeClass('item-agree')
        $(this).addClass('item-agree-mouseon')
    });

    $('.item-agree').on('mouseleave',function(){
        $(this).removeClass('item-agree-mouseon')
        $(this).addClass('item-agree')
    });

    $('.item-agree').on('click',function(){
        auth()
        var num = parseInt($(this).next().text())
        var title = ''
        $(this).parent().siblings().each(function(){
            if($(this).hasClass('item-title')){
                title=$(this).text()
                return
            }
        });
        dealwithThumbup(title)
        if($(this).hasClass('item-agree-click')){
            $(this).removeClass('item-agree-click');
            $(this).addClass('item-agree-mouseon');
            $(this).next().text(num-1);
        }
        else{
                $(this).removeClass('item-agree-mouseon');
                $(this).addClass('item-agree-click');
                $(this).next().text(num+1);
        };
    });

     $('#content-items').on('mouseover','.item-discuss',function(){
        $(this).removeClass('item-discuss')
        $(this).addClass('item-discuss-mouseon')
    });
    $('.item-discuss').on('mouseleave',function(){
        $(this).removeClass('item-discuss-mouseon')
        $(this).addClass('item-discuss')
    });

    $('#content-items').on('mouseover','.item-store',function(){
        $(this).removeClass('item-store')
        $(this).addClass('item-store-mouseon')
    });
    $('.item-store').on('mouseleave',function(){
        $(this).removeClass('item-store-mouseon')
        $(this).addClass('item-store')
    });

    $('.item-store').on('click',function(){
        if($(this).hasClass('item-store-click')){
            $(this).removeClass('item-store-click')
            $(this).addClass('item-store-mouseon')
        }
        else{
            $(this).removeClass('item-store-mouseon')
            $(this).addClass('item-store-click')
        }
    });
});

function msgRelease(ths){
    var newLinktext = $('#newLink').val()
    var newTitletext = $('#newTitle').val()
    var newAbstracttext = $('#newAbstract').val()
    console.info(newLinktext,newTitletext)
    /*if(newLinktext||newTitletext==null){
        alert('抱歉，链接和标题不能为空')
    }else{*/
    $('#content-items').prepend(
        '<div class="content-item">'+
                        '<div class="item-title">'+
                            '<a href='+newLinktext+'>'+newTitletext+'</a>'+
                        '</div>'+
                        '<div class="item-abstract-withPic">'+newAbstracttext+'</div>'+
                       // '<div class="item-picture"><img src="../homework/style/images/tw01.JPG" width="70" height="70"/></div>'+
                        '<div class="item-comment">'+
                            '<span class="item-agree"></span>'+
                            '<span class="item-num">4</span>'+
                            '<span class="item-discuss"></span>'+
                            '<span class="item-num">6</span>'+
                            '<span class="item-store"></span>'+
                            '<span class="item-store-char">私藏</span>'+
                            '<a href="http://dig.chouti.com/user/link/saved/1" class="item-auth">'+
                                '<span class="item-photo"><img src="../homework/style/images/photo.JPG" width="20" height="20"/></span>'+
                                '<b class="item-store-char">Eva_J</b>'+
                            '</a>'+
                            '<span class="item-time">'+
                                '<a class="item-time-a"><b>1分钟前</b></a>'+
                                '<i>入热榜</i>'+
                            '</span>'+
                        '</div>'+
                    '</div>'
    )
    //}
}

function gettime(){
    var d = new Date()
        var h = d.getHours();
        var m = d.getMinutes();
        t =((h<10 ? "0"+ h : h)+':'+(m<10 ? "0" + m : m))
        return t
}

function send(){
    var senText = $('#chat-textarea').val()
    $('#chat-main').append(
        '<div class="send">'+
            '<div class="userInfo"><span class="userInforight">'+gettime()+'</span><span class="userInforight">Eva_J</span></div>'+
                '<div class="arrow-right"></div>'+
                '<div class="sentenc-right">'+senText+'</div>'+
                '</div>'
    )

}

function dealwithThumbup(title){
    $.ajax({
            url: "/web/commentThumb/?title="+title,
            type:'GET',
            success:function(data){
                var callBack = $.parseJSON(data);
                if(callBack.status){
                    return 1
                };
            }
    });
}
