var base = {
    
    init: function (){
        /*mainp breytist i nav*/
        $(".nav_div li").on('click', 
            function ( e ) {
                var wrap = $('#main_cat');
                var href = $(this).find('.navlink').attr('href');
                base.load_project(href, wrap);
                $("li a").removeClass("active");
                $(this).find("a").addClass("active");
                e.preventDefault();
            
            })
        
        $("#elenipro").on('click', 
            function ( e ) {
                var wrap = $('#main_cat');
                var href = $(this).attr('href');
                base.load_project(href, wrap);
                $("li a").removeClass("active");
                e.preventDefault();
            
            })
            
        $("#main_cat").on('click', '#single_pro', 
            function ( e ) {
                var wrap_2 = $('#main_cat');
                var href_2 = $(this).attr('href');
                base.load_details(href_2, wrap_2);
                e.preventDefault();
            })
    },
    
    load_project: function (href, wrap){
           
        wrap.load( href + ' .content', base.img_fade);
        
    },
    
    load_details: function (href, wrap){
        wrap.load( href + ' .content');
    },
    
    img_fade: function () {
            $('.content a .img').hover(
            function () {
                $(this).stop().animate({
                    opacity: .4
                }, 400);
            $(this).closest('.content_container').find('.h3').fadeIn(800);
            }, 
            function () {
                $(this).stop().animate({
                    opacity: 1
                }, 700);
            $(this).closest('.content_container').find('.h3').fadeOut(600);
                });
    }   
};

$( document).ready(base.init);
















