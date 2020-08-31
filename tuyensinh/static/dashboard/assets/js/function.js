$(document).ready(function(){
    var current = location.pathname;
    $('#admin_sidebar li a').each(function(){
        var $this = $(this);
        // if the current path is like this link, make it active
        if($this.attr('href') === current ){
            $this.parent().addClass('active');
        }else{
            $this.parent().removeClass('active');
        }
    });
});
