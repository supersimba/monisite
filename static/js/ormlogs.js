/**
 * Created by root on 17-6-7.
 */

function chkProcess(ip,path,u,p)
{
    $.ajax({
        type:"POST",
        async:true,
        dataType:"text",
        data:{'ip':ip,'path':path,'u':u,'p':p},
        url: "/check_process/",
        success:function (callback) {
            // alert(callback);
            // document.write(callback);
            $('#div-display-log').html(callback)
        },
        error:function (callback) {
            $('#div-display-log').html('进程查看出错')
        }
    });
}


function getSyncLogs() {
    
}

$(document).ready(function () {
    //查看源端进程
    $('#btn-chk-src-pro').bind('click',function () {
        ip=$('.div-dbinfo').find('.span-dbinfo-ip').text();
        path=$('.div-dbinfo').find('.span-dbinfo-path').text();
        u=$('.div-dbinfo').find('.span-dbinfo-u').text();
        p=$('.div-dbinfo').find('.span-dbinfo-p').text();
        chkProcess(ip,path,u,p);
    });
    //查看T端进程
    $('#btn-chk-tgt-pro').bind('click',function () {
        ip=$('.div-dbinfo').find('.span-dbinfo-ip').text();
        path=$('.div-dbinfo').find('.span-dbinfo-path').text();
        u=$('.div-dbinfo').find('.span-dbinfo-u').text();
        p=$('.div-dbinfo').find('.span-dbinfo-p').text();
        chkProcess(ip,path,u,p);
    });
});