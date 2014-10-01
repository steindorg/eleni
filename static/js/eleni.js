var base = {
    /* init function is called on document ready*/
    init: function (){
        /*disable animation on images on small screens*/
        if($(window).width()>801){
            base.img_fade();
            console.log($(window).width());
        }
        /*asynchronous call on nav bar click*/
        $(".nav_div li").on('click',
            function ( e ) {
                var wrap = $('#main_cat');
                var href = $(this).find('.navlink').attr('href');
                base.load_project(href, wrap);
                $("li a").removeClass("active");
                $(this).find("a").addClass("active");
                e.preventDefault();

            })

    /*asynchronous call to home when clicking on Eleni podara*/
        $("#elenipro").on('click',
            function ( e ) {
                var wrap = $('#main_cat');
                var href = $(this).attr('href');
                base.load_project(href, wrap);
                $("li a").removeClass("active");
                e.preventDefault();

            })
    /*asynchronous call to project details when clicking on projects*/
        $("#main_cat").on('click', '#single_pro',
            function ( e ) {
                var wrap_2 = $('#main_cat');
                var href_2 = $(this).attr('href');
                var title = $(this).attr('title');
                /* display current navigation when choosing a project*/
                if(title === "Theatre"){
                     $('#theatrepro').addClass('active');
                }
                if(title === "Film"){
                     $('#filmpro').addClass('active');
                }
                if(title === "Tv"){
                     $('#tvpro').addClass('active');
                }
                if(title === "Various"){
                     $('#variouspro').addClass('active');
                }
                if(title === "Contact"){
                     $('#contactpro').addClass('active');
                }
                if(title === "Links"){
                     $('#linkspro').addClass('active');
                }
                base.load_details(href_2, wrap_2);
                e.preventDefault();
            })



    },
    /* Asynchronous load function for projects inside projet type*/
    load_project: function (href, wrap){
                                        /*img_fade is a function for
                                        image animation*/
        wrap.load( href + ' .content', base.img_fade);
    },
    /* Asynchronous load function for project details*/
    load_details: function (href, wrap){
                                        /*slider is a function for
                                        image slide show*/
        wrap.load( href + ' .content', base.slider);
    },
    /* Animation function that changes the color of the image and displays the
    title inside the image*/
    img_fade: function () {
            $('.content a .img').mouseenter(
            function () {
                $(this).stop().animate({
                    opacity: .3
                }, 200);
            $(this).closest('.content_container').find('.h3').stop().fadeIn(300);
            }).mouseleave(
            function () {
                $(this).stop().animate({
                    opacity: 1
                }, 200);
            $(this).closest('.content_container').find('.h3').stop().fadeOut(100);
                });
    },
    /* Function that creates the slide show inside project details*/
    slider: function () {
        var present=1;
        var next=2;
        var total_slide=document.getElementById("slider").childElementCount;

        $("#right").click(function()
        {
            present_slide="#slide"+present;
            console.log("#slide" + present+ "test");
            next_slide="#slide"+next;
            $(present_slide).css("display","none");
            $(next_slide).css("display","block");
            present++;
            next++;
            if(present==(total_slide+1))
            {
                present=1;
                next=2;
                for(i=1;i<=total_slide;i++)
                {
                    $("#slide"+i).css("display","none");
                }
                $("#slide1").css("display","block");
            }

        })

        $("#left").click(function()
        {
            if(present==1)
            {
            next_slide="#slide"+total_slide;
            present_slide="#slide"+present;
            $(present_slide).css("display","none");
            $(next_slide).css("display","block");

            present=total_slide;
            next=1;
            }else
            {
            next_slide="#slide"+(present-1);
            present_slide="#slide"+present;
            $(present_slide).css("display","none");
            $(next_slide).css("display","block");
            present--;
            next--;
            }
            if(next===0)
            {
                present=(total_slide-1);
                next=total_slide;

            }
        })
    }
};
/*init function called on document ready*/
$(document).ready(base.init);
















