/**
 * Created by root on 17-6-12.
 */

$(document).ready(function () {
//
    var src_ip=$('#div-src-dbinfo').children('span').eq(0).text();
    var src_path=$('#div-src-dbinfo').children('span').eq(1).text();
    var src_u=$('#div-src-dbinfo').children('span').eq(2).text();
    var src_p=$('#div-src-dbinfo').children('span').eq(3).text();
    var tgt_ip=$('#div-tgt-dbinfo').children('span').eq(0).text();
    var tgt_path=$('#div-tgt-dbinfo').children('span').eq(1).text();
    var tgt_u=$('#div-tgt-dbinfo').children('span').eq(2).text();
    var tgt_p=$('#div-tgt-dbinfo').children('span').eq(3).text();
    $('#btn-src-startup').bind('click',function () {

    });

    $('#btn-src-stop').bind('click',function () {
    //    SRC停止 进程
        $.ajax({
        type:"POST",
        async:false,
        dataType:"text",
        data:{'ip':src_ip,'path':src_path,'u':src_u,'p':src_p,'runflag':2},
        url: "/sync_oper/",
        success:function (callback) {
            // alert(callback);
            $('.div-cmd-display').html(callback);
            // document.getElementById('div-display-log').scrollTop=document.getElementById('div-display-log').scrollHeight;
        },
        error:function (callback) {
            $('.div-cmd-display').html('操作出错')
        }
        });
    });

    $('#btn-src-chk').bind('click',function () {
    //    执行进程检查
        $.ajax({
        type:"POST",
        async:false,
        dataType:"text",
        data:{'ip':src_ip,'path':src_path,'u':src_u,'p':src_p,'runflag':0},
        url: "/sync_oper/",
        success:function (callback) {
            // alert(callback);
            $('.div-cmd-display').html(callback);
            // document.getElementById('div-display-log').scrollTop=document.getElementById('div-display-log').scrollHeight;
        },
        error:function (callback) {
            $('.div-cmd-display').html('操作出错')
        }
        });
    });

    $('#btn-tgt-chk').bind('click',function () {
    //    执行进程检查
        $.ajax({
        type:"POST",
        async:false,
        dataType:"text",
        data:{'ip':tgt_ip,'path':tgt_path,'u':tgt_u,'p':tgt_p,'runflag':0},
        url: "/sync_oper/",
        success:function (callback) {
            // alert(callback);
            $('.div-cmd-display').html(callback);
            // document.getElementById('div-display-log').scrollTop=document.getElementById('div-display-log').scrollHeight;
        },
        error:function (callback) {
            $('.div-cmd-display').html('操作出错')
        }
        });
    });
});