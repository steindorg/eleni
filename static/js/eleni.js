var base = {

    init: function (){
        /*mainp breytist i nav*/
        if($(window).width()>801){
            base.img_fade();
            console.log($(window).width());
        }



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
                var title = $(this).attr('title');
                if(title === "Theatre"){
                    console.log(title + "ok this works");
                     $('#theatrepro').addClass('active');
                }
                if(title === "Film"){
                    console.log(title + "ok this works");
                     $('#filmpro').addClass('active');
                }
                if(title === "Tv"){
                    console.log(title + "ok this works");
                     $('#tvpro').addClass('active');
                }
                if(title === "Various"){
                    console.log(title + "ok this works");
                     $('#variouspro').addClass('active');
                }
                if(title === "Contact"){
                    console.log(title + "ok this works");
                     $('#contactpro').addClass('active');
                }
                if(title === "Links"){
                    console.log(title + "ok this works");
                     $('#linkspro').addClass('active');
                }
                base.load_details(href_2, wrap_2);
               e.preventDefault();
            })



    },

    load_project: function (href, wrap){
        console.log("load project" + href);
        wrap.load( href + ' .content', base.img_fade);

    },

    load_details: function (href, wrap){
        console.log("load project details" + href);
        wrap.load( href + ' .content', base.slider);
    },

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

    slider: function () {
        console.log("test the slider if it starts");
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

$(document).ready(base.init);
















