/**
 * Created by Administrator on 2016/4/1.
 */
function replyAuth(ths){
    var textareaVal = $(ths).val()
    if(textareaVal){
        $(ths).parent().siblings().each(function(){
            if($(this).hasClass('replyButton')){
                $(this).addClass('replyButton-active')
            }
            else{
                $(this).removeClass('replyButton-active')
            }
        })
    }
}

function replySon(ths){
    var linkId = $(ths).attr('linkid')
    $(ths).parent().siblings().each(function(){
        if($(this).hasClass('commentTestArea')){
            $(this).attr('linkid', linkId)
            $(this).children().prepend('<span style="float:left">add son comment : </span>')
        }
    })
}

function newdiscuss(ths,title){
   $.ajax({
            url: "/web/getCommentLst/?title="+title,
            type:'GET',
            success:function(data){
                var callBack = $.parseJSON(data);
                if(callBack.status){
                    console.info('-->callBack.commentTree : ',callBack.commentTree)
                    $(ths).parents().find('.commentTree').parent().html(callBack.commentTree);

                };
            }
        });
}

function replyComment(ths){
    var replyCommentPost = {}
    var discussArg = null
    var title = null
    if($(ths).hasClass('replyButton-active')){
        $(ths).siblings().each(function(){
            if($(this).hasClass('replyTextArea')){
                var textareaVal = $($(this).find('textarea')).val();
                replyCommentPost['comment'] = textareaVal
            }
        })
        $($($($(ths).parent()).parent()).parent()).siblings().each(function(){
            if($(this).hasClass('item-title')){
                title=$(this).text();
                replyCommentPost['title'] = title
            }
            if($(this).hasClass('item-discuss')){
                discussArg = $(this)
            }
        });
        replyCommentPost['linkid'] = $($(ths).parent()).attr('linkid')
        $.ajax({
                url: "/web/commentReply/",
                type:'POST',
                data:replyCommentPost,
                success:function(data){
                    var callBack = $.parseJSON(data);
                    if(callBack.status){
                        newdiscuss(ths,title)
                    };
                }
        });

    }
}

