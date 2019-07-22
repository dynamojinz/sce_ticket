window.onload=function(){
	 $('#searchInput').bind('keypress',function(event){
        if(event.keyCode == "13"){
            $("#search_form").trigger("submit");
            return false;
            }
        });
	 topBind();

     // $('#checkInput').bind('click',function(event){
     //        if(true){
     //            console.log("绑定事件成功");
     //            $("#checkForm").trigger("submit");
     //        }
     //    });
     // function changeState(state){
	  //    console.log(state);
     // }
}
function topBind() {
         var form = $(".weui-form-preview__item form");
         var input = $(".weui-form-preview__item form input");
         for (var i = 0; i <= form.length; i++) {
             $(input[i]).bind('click', function () {
                 topped($(this));
             });
         }

     }
function topped(a){
    console.log(a)
	$(a[0].parentNode).submit();
	console.log('topped ok')
}
