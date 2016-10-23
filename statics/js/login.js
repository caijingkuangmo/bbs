/**
 * Created by Administrator on 2016/3/31.
 */
function getlogin(loginRender){
    $.ajax({
                url: "/web/login/",
                type:'GET',
                success:function(data){
                    var callBack = $.parseJSON(data);
                    if(callBack.status){
                        $(loginRender).html(callBack.htmldata)
                    };
                }
            });
}