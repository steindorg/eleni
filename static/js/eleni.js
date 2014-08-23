/*$(document).ready(function () {
   
    var wrap = $('#main_cat');
    $(".mainp li").click(function ( e ) {
        
        e.preventDefault();
        $(this).addClass("active");
        $(this).siblings().removeClass("active");
        var href = $(this).find('#mainpro').attr('href');
        
        wrap.load( href + ' .content', 
            function (){
                $('.content a .img').hover(
                        function () {
                            $(this).stop().animate({
                                opacity: .4
                            }, 400);
                            $(this).closest('.content').find('.h3').fadeIn(800);
                        }, 
                        function () {
                            $(this).stop().animate({
                                opacity: 1
                            }, 700);
                            $(this).closest('.content').find('.h3').fadeOut(600);
                        
                        });
                        });
    });
});



(function () {
    
    var base = {
        
        wrap: $('#main_cat'),
        init: function ( e ){
            console.log(this);
            $(".mainp li").click(function ( e ) {
            e.preventDefault();
            $(this).addClass("active");
            $(this).siblings().removeClass("active");
            var href = $(this).find('#mainpro').attr('href');
            wrap.load( href + ' .content', this.img_fade);
                });

        },
        img_fade: function () {
            $('.content a .img').hover(function () {
                $(this).stop().animate({
                    opacity: .4
                }, 400);
            $(this).closest('.content').find('.h3').fadeIn(800);
            }, 
            function () {
                $(this).stop().animate({
                    opacity: 1
                }, 700);
            $(this).closest('.content').find('.h3').fadeOut(600);
                });
        }   
    
    };

  
   


})();

*/
   
 

var base = {
    
    init: function (){
     $(".mainp li").on('click', 
        function ( e ) {
            var wrap = $('#main_cat');
            var href = $(this).find('#mainpro').attr('href');
            base.load_project(href, wrap);
            $(this).addClass("active");
            $(this).siblings().removeClass("active");
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
        
        if (href === '/contact'){
            /*console.log('this worked for contact');*/
            wrap.load( href + ' .content');
            $(document).ajaxStop( function () {
            base.form_sub();
            });
        }
        else
        {
            wrap.load( href + ' .content', base.img_fade);
        }
    },
    
    load_details: function (href, wrap){
        wrap.load( href + ' #main_cat');
    },
    
    img_fade: function () {
            $('.content a .img').hover(
            function () {
                $(this).stop().animate({
                    opacity: .4
                }, 400);
            $(this).closest('.content').find('.h3').fadeIn(800);
            }, 
            function () {
                $(this).stop().animate({
                    opacity: 1
                }, 700);
            $(this).closest('.content').find('.h3').fadeOut(600);
                });
    },   
    
    form_sub: function ( e ) {
        
        /*$("#feedbackform").on('submit', function ( e ) {
            var form = $('#feedbackform');
            $.post( "/contact/", $(this).serialize(), 
            function ( e ){
                $('#ajaxwrapper').load('/contact/' + '#ajaxwrapper', form.serializeArray(),
                    function () {
                        $("a[href$='/contact']").addClass("active");
                        
                    }

                    );
                

            });
            
            e.preventDefault();
        
        }); */            
        var form = $("#contactform");
        console.log(form.attr('action') + ' er þetta ekki a gera sig');
        form.submit(function(e) {
            
            $("#sendbutton").attr('disabled', true)
            $("#sendwrapper").prepend('<span>Sending message, please wait... </span>')
            $("#ajaxwrapper").load(
                '/contact/' + ' #ajaxwrapper',
                form.serializeArray(),
                
                function(responseText, responseStatus) {
                    console.log('do I go here ');
                    $("#sendbutton").attr('disabled', false)
                }
            );
            e.preventDefault(); 
        });


    }
    

};

$( document).ready(base.init);

jQuery(function() {
      var form = jQuery("#contactform");
      form.submit(function(e) {
          jQuery("#sendbutton").attr('disabled', true)
          jQuery("#sendwrapper").prepend('<span>Sending message, please wait... </span>')
          jQuery("#ajaxwrapper").load(
              form.attr('action') + ' #ajaxwrapper',
              form.serializeArray(),
              function(responseText, responseStatus) {
                  jQuery("#sendbutton").attr('disabled', false)
              }
          );
          e.preventDefault(); 
      });
  });















