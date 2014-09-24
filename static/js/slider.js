 (function()
    {
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
    })();
