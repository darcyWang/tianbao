function addDownload(){
    var divDown = $('<footer class="download" onclick="javascript:location.href=\'http://a.app.qq.com/o/simple.jsp?pkgname=com.dingjian.yangcongtao\'"><em class="logo">YoungChoice</em><div><h1>�����</h1><h2>ȫ����ױ��Ʒ����</h2></div><a class="bdrds" href="javascript:;" target="_blank">���������App</a></footer>');
    $("body").append(divDown);

    var ff=GetRequest("ff");

    alert(ff);

    if(ff.toString()!="undefined"){
        $(".download").css("display","none");
        alert("have ff");
    }
}
