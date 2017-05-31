/**
 * Created by root on 17-5-31.
 */

function logs(str){
    console.log(str);
}


function setSrcSyncStatus(val) {
    switch (val)
    {
        case -1:
            return "告警";
        case 0:
            return "停止";
        case 1:
            return "正常";
    }
}


function chkTargetConfig(ssh_status,path_status,script_status) {
    if(ssh_status==1 && path_status==1 && script_status==1)
    {
        return 1;
    }
    if(ssh_status==-1)
    {

    }
}


function setSrcSyncActive(val) {
    switch (val)
    {
        case -1:
            return "进程异常";
        case 0:
            return "停止";
        case 1:
            return "待机";
        case 2:
            return "正常";
    }
}
function getSourceInfo(queue_id,trobj,i,trobj_plus) {
    $.ajax({
                type:"POST",
                async:true,
                dataType:"json",
                data:{rid:queue_id},
                url: "/display_source_info/",
                beforeSend:function () {
                    console.log("begin to get info from src_moni_info");
                },
                success:function (callback) {
                    if(callback["ssh_status"]==1 && callback["path_status"]==1 && callback["script_status"]==1)
                    {
                        //console.log(typeof callback["add_time"]);
                        trobj.children().eq(4).text(setSrcSyncStatus(callback["sync_status"]));
                        trobj.children().eq(5).text(setSrcSyncActive(callback["active"]));
                        trobj.children().eq(6).text(callback["add_time"]);
                        trobj_plus.children().eq(0).children().eq(0).children('#span-dbps-num').text(callback['dbps_cnt']);
                        trobj_plus.children().eq(0).children().eq(0).children('#span-vag-num').text(callback['capture_cnt']);
                        trobj_plus.children().eq(0).children().eq(0).children('#span-sender-num').text(callback['sender_cnt']);
                        trobj_plus.children().eq(0).children().eq(0).children('#span-vag-err').text(callback['capture_err']);
                        trobj_plus.children().eq(0).children().eq(0).children('#span-sender-err').text(callback['sender_err']);
                        // trobj_plus.children().eq(0).children().eq(2).children('#span-loader-time').text(callback['loader_time']);
                    }
                    // else
                    // {
                    //     if(callback["ssh_status"]==-1 || callback["path_status"]==-1)
                    //     {
                    //         trobj.children().eq(6).css({'color':'white','background':'red','font-weight':'600'});
                    //     }
                    //     if(callback["script_status"]==-1)
                    //     {
                    //         trobj.children().eq(7).css({'color':'white','background':'red','font-weight':'600'});
                    //     }
                    // }

                },
                error:function () {
                    console.log("数据抓取失败");
                }
            });
}

function displaySourceInfo() {
    for(var i=0;i<$("tbody").children().length;i++){
        if(i%2==0){
            //console.log("i="+i);
            var trobj=$("tbody").children().eq(i);
            var trobj_plus=$("tbody").children().eq(i+1);
            queueid=trobj.children().eq(0).children().eq(1).text();
            //console.log("queue_id="+queueid);
            //console.log(trobj.children().eq(1).text());
            //console.log(trobj);
            getSourceInfo(queueid,trobj,i,trobj_plus);
        }
        else {
            $("tbody").children().eq(i).css('color','rgb(98,98,143)');
        }
    }
}
$(document).ready(function () {
    //$("tbody").find('span.span-info').css({'font-size':'16px','color':'rgb(14,144,210)'});
    setInterval(displaySourceInfo,2000);
});