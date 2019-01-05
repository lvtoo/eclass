$(function () {//Wait for page to be ready
    $('#hamburger').click(function () {
        $('.nav').css('margin-left', '0');
        $('.navoverlay').css('opacity', '1');
        $('.navoverlay').css('z-index', '60');
        $('.navoverlay').click(function () {
            $('.navoverlay').css('opacity', '0');
            $('.navoverlay').css('z-index', '-1');
            $('.nav').css('margin-left', '-100%');
        })
    })
});
// $(function(){//Wait for page to be ready
//       var filtersOpen = false;
//   $('#option').click(function(){
//     $('.nav').css('margin-left', '0');
//     $('.navoverlay').css('opacity', '0');
//     $('.navoverlay').css('z-index', '60');
//     $('.navoverlay').click(function(){
//       if(filtersOpen){
//       //Move Filter Window Off screen
//       $('.filters').css('right','-100%');
//       filtersOpen = false;//set the boolean to false
//     }else{
//       $('.filters').css('right', '0px');
//       filtersOpen = true; //set the boolean to true
//     }
//
//       $('.navoverlay').css('opacity', '0');
//       $('.navoverlay').css('z-index', '-1');
//       $('.nav').css('margin-left', '-100%');
//     })
//   })
// })


$(function () {//Wait for page to be ready
    var filtersOpen = false;
    $('#option').click(function () {
        $('.competition-post').css('display', 'block');
    });
    $('#settings').click(function () {
        if (filtersOpen) {
            //Move Filter Window Off screen
            $('.filters').css('right', '-100%');
            filtersOpen = false;//set the boolean to false
        } else {
            $('.filters').css('right', '0px');
            filtersOpen = true; //set the boolean to true
        }
    })
});

var newsOpen = false;
$('#competition-filter').click(function () {
    if (!newsOpen) {
        $('.news').css('height', '0');
        $('.news').css('margin-bottom', '0');
        $('#competition-filter').css('color', '#DEDEDE');
        newsOpen = true;
    } else {
        $('.news').css('height', '120px');
        $('.news').css('margin-bottom', '10px');
        $('#competition-filter').css('color', '#222');
        newsOpen = false;
    }
});


var noticesOpen = false;
$('#portfolio-filter').click(function () {
    if (!noticesOpen) {
        $('.notices').css('height', '0');
        $('.notices').css('margin-bottom', '0px');
        $('#portfolio-filter').css('color', '#DEDEDE');
        noticesOpen = true;
    } else {
        $('.notices').css('height', '120px');
        $('.notices').css('margin-bottom', '10px');
        $('#portfolio-filter').css('color', '#222');
        noticesOpen = false;
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
var a = 3;
var load = true;

//获取页面顶部被卷起来的高度
function scrollTop() {
    return Math.max(
        //chrome
        document.body.scrollTop,
        //firefox/IE
        document.documentElement.scrollTop);
}

function windowHeight() {
    return (document.compatMode == "CSS1Compat") ?
        document.documentElement.clientHeight :
        document.body.clientHeight;
}

//获取页面文档的总高度
function documentHeight() {
    //现代浏览器（IE9+和其他浏览器）和IE8的document.body.scrollHeight和document.documentElement.scrollHeight都可以
    return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
}


$(window).on('scroll', function () {
    if (scrollTop() + windowHeight() >= (documentHeight() - 50/*滚动响应区域高度取50px*/)) {
        if (load == true) {
            feedJoin(a);
            a++;
        }

    }
});


function feedJoin(a) {
    $.ajax({
        type: 'get',
        async: false,
        url: "/api/news",
        dataType: 'html',
        data: {'p': a},
        success: function (reponse) {
            $(".feed").append(reponse)
        },
        error: function () {
            load = false;
            $("#bottom").css("display", "block");
        }
    });
}

//////下拉框
$("#sort").click(function () {
    $("#dropdown-con").toggle();
});
//搜索

$(function () {
    // $("#search").click(function () {
    //     var key = $("#con").val();
    //     if (key == "") {
    //         alert("请输入关键字");
    //         return false;
    //     }
    //     $.ajax({
    //         type: "post",
    //         url: "/search/",
    //         data: {
    //             'key_words': key,
    //             csrfmiddlewaretoken: '{{ csrf_token }}'
    //
    //         },
    //         success: function () {
    //             window.location.href = "/search/"
    //         },
    //         error: function () {
    //             alert("发生未知错误")
    //         }
    //     })
    // });
    $('input').keydown(function (event) {
        if (event.keyCode == 13) {
            var key = $("#con").val();
            if (key == "") {
                alert("请输入关键字");
                return false;
            }
            $.ajax({
                type: "get",
                url: "/search/",
                data: {
                    'key_words': key,
                },
                success: function () {
                    window.location.href = "/search/"
                },
                error: function () {
                    alert("发生未知错误")
                }
            })
        }
    });
});
// $(function () {
//     var start = 10;
//     var offset = 15;
//
//     /*首次加载*/
//     function unicode2Chr(str) {
//         return unescape(str.replace(/\\/g, "%"))
//     }
//
//     $("#ajax-button").click(function () {
//         // alert(currentPage+'-'+nextPage);
//         feedJoin(start, offset);
//     });
//
//     function feedJoin(start, offset) {
//         $.ajax({
//             type: 'get',
//             url: "/api/news",
//             data: {
//                 "start": start,
//                 "offset": offset
//             },
//             dataType: 'json',
//             success: function (reponse) {
//
//                 // data = unicode2Chr(reponse);
//                 for (var i = 0; i < reponse.length; i++) {
//                     var obj = reponse[i];
//                     var html = "<div class=\"feed-item notices\"><div class=\"text-holder-noimage col-3-5\"><div class=\"feed-title\">" +
//                         obj.title +
//                         "</div><div class=\"feed-description\">" +
//                         obj.description +
//                         "</div></div>" +
//                         "<div class=\"feed-meta\"><span class=\"single\"><i\n" +
//                         "                                class=\"fa fa-tags\"></i>" +
//                         obj.type +
//                         "</span><span\n" +
//                         "                                class=\"single\"><i class=\"fa fa-clock-o\"></i>" +
//                         obj.pub_date +
//                         "</span></div>\n" +
//                         "                    </div>"
//                 }
//                 html = unicode2Chr(html);
//                 $('.feed').append(html);
//                 start += 5;
//                 offset +=5;
//
//             },
//             error: function () {
//                 alert("error!")
//             }
//         });
//     }




