/**
 * Created by Administrator on 2016/3/30.
 */
$(function(){
/*    var menus = $("#navbar a[href='{{ request.path }}']")[0];
    $(menus).parent().addClass("active")
    $(menus).parent().siblings().removeClass("active")*/

    $('#href').on('blur','#articlehref',function(){
        if($('#articlehref').val()){
            $('#getTitleButton').addClass('add-link-022-active')
        }
        else{
            $('#getTitleButton').removeClass('add-link-022-active')
        }
    })
})

function publish(ths,category){
    auth(ths,'publish')
    $.ajax({
                url: "/web/publish/"+category,
                type:'GET',
                success:function(data){
                    var callBack = $.parseJSON(data);
                    if(callBack.status){
                        $('#'+category).html(callBack.htmldata)
                        $('#'+category).siblings().each(function(){
                            $(this).html('')
                        })
                    };
                }
            });
}

function getTitle(){
    if($('#articlehref').val()){
        var url = $('#articlehref').val();
        $.ajax({
            url: "/web/geturl/?url="+url,
            type:'GET',
            success:function(data){
                var callBack = $.parseJSON(data);
                if(callBack.status){
                    $('#title').val(callBack.gettitle)
                };
            }
        });
    }
}

function discuss(ths){
    auth(ths,'discuss')
    var title = ''
    $(ths).parent().siblings().each(function(){
        if($(this).hasClass('item-title')){
            title=$(this).text()
            return
        }
    });
    $.ajax({
            url: "/web/getCommentLst/?title="+title,
            type:'GET',
            success:function(data){
                var callBack = $.parseJSON(data);
                if(callBack.status){
                    $(ths).parent().next().html(callBack.commentTree)
                };
            }
        });
}

function closeComment(ths){
    $(ths).parent().parent().parent().html('')
}

/*function add(dailogBody){
    $(dailogBody).children().each(function(){
        if($(this).hasClass('active')){
            console.info($(this).find('a')[0])
            var activeDiv = $(this).find('a')[0]
            var category = $(activeDiv).attr('href')
            var submitJson = {}
            alert(category)
            var categoryStr = $(category).attr('id')
            $(category).find('.form-control').each(function(){
                submitJson[$(this).attr('name')]=$(this).val()
            })
            $(category).find('#id_img').each(function(){
                submitJson[$(this).attr('name')]=$(this).val()
            })
            console.info(submitJson)
            submitJson['saveType']=categoryStr
            $.ajax({
                //url: "/web/publish/"+categoryStr,
                url: "/web/add/",
                type:'POST',
                data:submitJson,
                success:function(data){
                    var callBack = $.parseJSON(data);
                    if(callBack.status){
                        $('#title').val(callBack.gettitle)
                    };
                }
        });
        }
    })
}*/
