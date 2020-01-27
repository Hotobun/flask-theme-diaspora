/*
 * Diaspora
 * @author LoeiFy
 * @url http://lorem.in
 */

var Home = location.href,
    Pages = 4,
    xhr,
    xhrUrl = '';
 

var Diaspora = {

    L: function(url, f, err) {
        if (url == xhrUrl) { 
            return false
        }

        xhrUrl = url;

        if (xhr) { 
            xhr.abort()
        }

        xhr = $.ajax({
            type: 'GET',
            url: url,
            timeout: 1000,
            success: function(data) {
                f(data)
                xhrUrl = '';
            },
            error: function(a, b, c) {
                if (b == 'abort') {
                    err && err()
                } else {
                    window.location.href = url
                }
                xhrUrl = '';
            }
        })

    },

    P: function() {
        return !!('ontouchstart' in window);
    },

    PS: function() {
        if (!(window.history && history.pushState)) return;

        history.replaceState({u: Home, t: document.title}, document.title, Home)

        window.addEventListener('popstate', function(e) {
            var state = e.state;

            if (!state) return;

            document.title = state.t;

            if (state.u == Home) {
                $('#preview').css('position', 'fixed')
                setTimeout(function() {
                    $('#preview').removeClass('show').addClass('trans')
                    $('#container').show()
                    window.scrollTo(0, parseInt($('#container').data('scroll')))
                    setTimeout(function() {
                        $('#preview').html('')
                        $(window).trigger('resize')
                    }, 300)
                }, 0)
            } else {
                Diaspora.loading()

                Diaspora.L(state.u, function(data) {

                    document.title = state.t;

                    $('#preview').html($(data).filter('#single'))

                    Diaspora.preview()

                    setTimeout(function() { Diaspora.player(state.d) }, 0)
                })
            }

        })
    },

    HS: function(tag, flag) {
        var id = tag.data('id') || 0,
            url = tag.attr('href'),
            title = tag.attr('title') || tag.text();

        if (!$('#preview').length || !(window.history && history.pushState)) location.href = url;

        Diaspora.loading()

        var state = {d: id, t: title, u: url};

        Diaspora.L(url, function(data) {

            if (!$(data).filter('#single').length) {
                location.href = url;
                return
            }

            switch (flag) {

                case 'push':
                    history.pushState(state, title, url)
                break;

                case 'replace':
                    history.replaceState(state, title, url)
                break;

            }

            document.title = title;

            $('#preview').html($(data).filter('#single'))

            switch (flag) {

                case 'push': 
                    Diaspora.preview()
                break;

                case 'replace':
                    window.scrollTo(0, 0)
                    Diaspora.loaded()
                break;
            }

            setTimeout(function() {
                if (!id) id = $('.icon-play').data('id');
                Diaspora.player(id)

                // get download link
                $('.content img').each(function() { 
                    if ($(this).attr('src').indexOf('/uploads/2014/downloading.png') > -1) {
                        $(this).hide()
                        $('.downloadlink').attr('href', $(this).parent().attr('href'))
                    }
                })

                if (flag == 'replace') {
                    $('#top').show()
                }
            }, 0)

        })
    },

    preview: function() { 
        setTimeout(function() {
            $('#preview').addClass('show')
            $('#container').data('scroll', window.scrollY)
            setTimeout(function() {
                $('#container').hide()
                setTimeout(function() {
                    $('#preview').css({
                        'position': 'static',
                        'overflow-y': 'auto'
                    }).removeClass('trans')
                    $('#top').show()

                    Diaspora.loaded()
                }, 500)
            }, 300)
        }, 0)
    },

    player: function(id) {
        var p = $('#audio');
        if (!p.length) {
            $('.icon-play').css({
                'color': '#dedede',
                'cursor': 'not-allowed'
            })
            return
        }
        var sourceSrc= $("#audio source").eq(0).attr('src')
        if (sourceSrc == '' && p[0].src == ''){
            audiolist = $('#audio-list li');
            mp3 = audiolist.eq([Math.floor(Math.random() * audiolist.size())])
            p[0].src = mp3.data('url')
        }

        if (p.eq(0).data("autoplay") == true) {
            p[0].play();
        }

        p.on({
            'timeupdate': function() {
                var progress = p[0].currentTime / p[0].duration * 100;
                $('.bar').css('width', progress + '%');
                if (progress / 5 <= 1) {
                    p[0].volume = progress / 5;
                }else {
                    p[0].volume = 1;
                }
            },
            'ended': function() {
                $('.icon-pause').removeClass('icon-pause').addClass('icon-play')
            },
            'playing': function() {
                $('.icon-play').removeClass('icon-play').addClass('icon-pause')
            }
        })
    },

    loading: function() {
        var w = window.innerWidth;
        var css = '<style class="loaderstyle" id="loaderstyle'+ w +'">'+
                  '@-moz-keyframes loader'+ w +'{100%{background-position:'+ w +'px 0}}'+
                  '@-webkit-keyframes loader'+ w +'{100%{background-position:'+ w +'px 0}}'+
                  '.loader'+ w +'{-webkit-animation:loader'+ w +' 3s linear infinite;-moz-animation:loader'+ w +' 3s linear infinite;}'+
                  '</style>';
        $('.loaderstyle').remove()
        $('head').append(css)

        $('#loader').removeClass().addClass('loader'+ w).show()
    },

    loaded: function() {
        $('#loader').removeClass().hide()
    },

    F: function(id, w, h) {
        var _height = $(id).parent().height(),
            _width = $(id).parent().width(),
            ratio = h / w;

        if (_height / _width > ratio) {
            id.style.height = _height +'px';
            id.style.width = _height / ratio +'px';
        } else {
            id.style.width = _width +'px';
            id.style.height = _width * ratio +'px';
        }

        id.style.left = (_width - parseInt(id.style.width)) / 2 +'px';
        id.style.top = (_height - parseInt(id.style.height)) / 2 +'px';
    }

}

$(function() {

    if (Diaspora.P()) {
        $('body').addClass('touch')
    }

    if ($('#preview').length) {

        var cover = {};
        cover.t = $('#cover');
        cover.w = cover.t.attr('width');
        cover.h = cover.t.attr('height');

        ;(cover.o = function() {
            $('#mark').height(window.innerHeight)
        })();

        if (cover.t.prop('complete')) {
            // why setTimeout ? 
            setTimeout(function() { cover.t.load() }, 0)
        }

        cover.t.on('load', function() {

            ;(cover.f = function() {

                var _w = $('#mark').width(), _h = $('#mark').height(), x, y, i, e;

                e = (_w >= 1000 || _h >= 1000) ? 1000 : 500;

                if (_w >= _h) {
                    i = _w / e * 50;
                    y = i;
                    x = i * _w / _h;
                } else {
                    i = _h / e * 50;
                    x = i;
                    y = i * _h / _w;
                }

                $('.layer').css({
                    'width': _w + x,
                    'height': _h + y,
                    'marginLeft': - 0.5 * x,
                    'marginTop': - 0.5 * y
                })

                if (!cover.w) {
                    cover.w = cover.t.width();
                    cover.h = cover.t.height();
                }

                Diaspora.F($('#cover')[0], cover.w, cover.h)

            })();

            setTimeout(function() { 
                $('html, body').removeClass('loading')
            }, 1000)

            $('#mark').parallax()

            var vibrant = new Vibrant(cover.t[0]);
            var swatches = vibrant.swatches()

            if (swatches['DarkVibrant']) {
                $('#vibrant polygon').css('fill', swatches['DarkVibrant'].getHex())
                $('#vibrant div').css('background-color', swatches['DarkVibrant'].getHex())
            }
            if (swatches['Vibrant']) {
                $('.icon-menu').css('color', swatches['Vibrant'].getHex())
            }

        })

        if (!cover.t.attr('src')) {
            alert('Please set the post thumbnail')
        }

        $('#preview').css('min-height', window.innerHeight)

        Diaspora.PS()

        $('.pview a').addClass('pviewa')

        var T;
        $(window).on('resize', function() { 
            clearTimeout(T)

            T = setTimeout(function() { 
                if (!Diaspora.P() && location.href == Home) {
                    cover.o()
                    cover.f()
                }

                if ($('#loader').attr('class')) {
                    Diaspora.loading()
                }
            }, 500)
        })  

    } else {

        $('#single').css('min-height', window.innerHeight)
        $('html, body').removeClass('loading')
        
        window.addEventListener('popstate', function(e) {
            if (e.state) location.href = e.state.u;
        })

        Diaspora.player($('.icon-play').data('id'))

        $('.icon-icon, .image-icon').attr('href', '/')

        // get download link
        $('.content img').each(function() {
            if ($(this).attr('src').indexOf('/uploads/2014/downloading.png') > -1) {
                $(this).hide()
                $('.downloadlink').attr('href', $(this).parent().attr('href')).css('display', 'block')
            }
        })

        $('#top').show()

    }

    $(window).on('scroll', function() {
        if ($('.scrollbar').length && !Diaspora.P() && !$('.icon-images').hasClass('active')) {
            var st = $(window).scrollTop(),
                ct = $('.content').height();

            if (st > ct) {
                st = ct
            }

            $('.scrollbar').width((50 + st) / ct * 100 +'%')

            if (st > 80 && window.innerWidth > 800) {
                $('.subtitle').fadeIn()
            } else {
                $('.subtitle').fadeOut()
            }
        }
    })

    $(window).on('touchmove', function(e) {
        if ($('body').hasClass('mu')) {
            e.preventDefault()
        }
    })

    $('body').on('click', function(e) {

        var tag = $(e.target).attr('class') || '',
            rel = $(e.target).attr('rel') || '';
        // .content > ... > img
        if (e.target.nodeName == "IMG" && $(e.target).parents('div.content').length > 0) {
            tag = 'pimg';
        }
        if (!tag && !rel) return;

        switch (true) {

            // nav menu
            case (tag.indexOf('switchmenu') != -1):
                window.scrollTo(0, 0)
                $('html, body').toggleClass('mu');
                return false;
            break;

            // next page
            case (tag.indexOf('more') != -1):
                tag = $('.more');

                if (tag.data('status') == 'loading') {
                    return false
                }

                var num = parseInt(tag.data('page')) || 1;

                if (num == 1) {
                    tag.data('page', 1)
                }

                if (num >= Pages) {
                    return
                }

                tag.html('加载中..').data('status', 'loading')
                Diaspora.loading()

                Diaspora.L(tag.attr('href'), function(data) {
                    var link = $(data).find('.more').attr('href');
                    if (link != undefined) {
                        tag.attr('href', link).html('加载更多').data('status', 'loaded')
                        tag.data('page', parseInt(tag.data('page')) + 1)
                    } else {
                        // $('#pager').remove()
                    }
					
					var tempScrollTop = $(window).scrollTop()
                    $('#primary').append($(data).find('.post'))
					$(window).scrollTop(tempScrollTop)
                    Diaspora.loaded()
					$('html,body').animate({ scrollTop: tempScrollTop + 400 }, 500)
                }, function() {
                    tag.html('加载更多').data('status', 'loaded')
                })

                return false;
            break;

            // post images
            case (tag.indexOf('icon-images') != -1):
                window.scrollTo(0, 0)

                var d = $('.icon-images');

                if (d.data('status') == 'loading') {
                    return false
                }

                if (d.hasClass('active')) {
                    d.removeClass('active')

                    $('.article').css('height', 'auto')
                    $('.section').css('left', '-100%')
                    setTimeout(function() { 
                        $('.images').data('height', $('.images').height()).css('height', '0') 
                    }, 0)
                } else {
                    d.addClass('active')

                    $('.images').css('height', $('.images').data('height'))

                    if ($('.icon-images').hasClass('tg')) {
                        $('.section').css('left', 0) 
                        setTimeout(function() { $('.article').css('height', '0') }, 0)
                    } else {
                        if (!(Diaspora.P() && window.innerWidth < 700)) {
                            $('.zoom').Chocolat()
                        }

                        Diaspora.loading()
                        d.data('status', 'loading')

                        var m = 5, r = 120;
                        if (Diaspora.P() && window.innerWidth < 600) {
                            m = 1;
                            r = 80;
                        }
                        $('#jg').justifiedGallery({
                            margins: m, 
                            rowHeight : r,
                        }).on('jg.complete', function () {
                            $('.section').css('left', 0)
                            $('.icon-images').addClass('tg')

                            d.data('status', '')
                            Diaspora.loaded() 
                            setTimeout(function() { $('.article').css('height', '0') }, 0)
                        })
                    }

                }
            break;
            // home
            case (tag.indexOf('icon-home') != -1): 
                $('.toc').fadeOut(1000);
                if ($('#preview').hasClass('show')) { 
                    history.back();
                } else {  
                    location.href = $('.icon-home').data('url') 
                }
                return false;
                break;
            // qrcode
            case (tag.indexOf('icon-scan') != -1):
                if ($('.icon-scan').hasClass('tg')) {
                    $('#qr').toggle()
                } else {
                    $('.icon-scan').addClass('tg')
                    $('#qr').qrcode({ width: 128, height: 128, text: location.href}).toggle()
                }
                return false;
                break;
            // audio play
            case (tag.indexOf('icon-play') != -1):
                $('#audio')[0].play()
                $('.icon-play').removeClass('icon-play').addClass('icon-pause')
                return false;
                break;
            // audio pause
            case (tag.indexOf('icon-pause') != -1):
                $('#audio')[0].pause()
                $('.icon-pause').removeClass('icon-pause').addClass('icon-play')
                return false;
                break;

            // post like
            case (tag.indexOf('icon-like') != -1):
                var t = $(e.target).parent(),
                    classes = t.attr('class');

                if (t.prev().hasClass('icon-view')) return;

                classes = classes.split(' ');
                if(classes[1] == 'active') return;

                t.addClass('active')

                var id = t.attr('id').split('like-');

                $.ajax({
                    type: 'POST',
                    url: '/index.php',
                    data: 'likepost=' + id[1],
                    success: function() {
                        var text = $('#like-'+ id[1]).html(),
                            patt= /(\d)+/,
                            num = patt.exec(text);

                        num[0] ++;
                        $('#like-'+ id[1]).html('<span class="icon-like"></span><span class="count">' + num[0] + '</span>')
                    }
                })
            break;

            // history state
            case (tag.indexOf('cover') != -1):
                Diaspora.HS($(e.target).parent(), 'push')
                return false;
            break;

            // history state
            case (tag.indexOf('posttitle') != -1):
                Diaspora.HS($(e.target), 'push')
                return false;
            break;

            // relate post
            case (tag.indexOf('relatea') != -1): 
                Diaspora.HS($(e.target), 'replace')
                return false;
            break;

            // relate post
            case (tag.indexOf('relateimg') != -1): 
                Diaspora.HS($(e.target).parent(), 'replace')
                return false;
            break;

            // prev, next post
            case (rel == 'prev' || rel == 'next'):
                if (rel == 'prev') {
                    var t = $('#prev_next a')[0].text
                } else {
                    var t = $('#prev_next a')[1].text
                }
                $(e.target).attr('title', t)

                Diaspora.HS($(e.target), 'replace')
                return false;
            break;
            
            // photoswipe
            case (tag.indexOf('pimg') != -1):
                var pswpElement = $('.pswp').get(0);
                if (pswpElement) {
                    var items = [];
                    var index = 0;
                    var imgs = [];
                    $('.content img').each(function(i, v){
                        // get index
                        if (e.target.src == v.src) {
                            index = i;
                        }
                        var item = {
                            src: v.src,
                            w: v.naturalWidth,
                            h: v.naturalHeight
                        };
                        imgs.push(v);
                        items.push(item);
                    });
                    var options = {
                        index: index,
                        shareEl: false,
                        zoomEl: false,
                        allowRotationOnUserZoom: true,
                        history: false,
                        getThumbBoundsFn: function(index) {
                            // See Options -> getThumbBoundsFn section of documentation for more info
                            var thumbnail = imgs[index],
                                pageYScroll = window.pageYOffset || document.documentElement.scrollTop,
                                rect = thumbnail.getBoundingClientRect(); 

                            return {x:rect.left, y:rect.top + pageYScroll, w:rect.width};
                        }
                    };
                    var lightBox= new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, items, options);
                    lightBox.init();
                }
                return false;
                break;

            // quick view
            case (tag.indexOf('pviewa') != -1):
                $('body').removeClass('mu')
                setTimeout(function() { 
                    Diaspora.HS($(e.target), 'push')
                    $('.toc').fadeIn(1000);
                }, 300)

                return false;
            break;

            default:
                return;
            break;
        }

    })

    console.log("%c Github %c","background:#24272A; color:#ffffff","","https://github.com/LoeiFy/Diaspora")

})




// 后面是我增加的 
// 请求json flag变量 如果到最后就不再判断
var get_json_tur = true;
var site_indexpath = '/'
var json_xhr = new XMLHttpRequest();

function add_archive(data){
    // console.log("function add_archive");
    // console.log("data:",data);
    // console.log(data["data"], data.data, data.more);
    var primary = document.getElementById('primary');
    var more_a = document.getElementById("moreurl");
    var more_button = document.getElementById("more_button");
    var now_y = getScrollTop();
    for (index in data.data){ 
        item = data.data[index];
        // console.log("item",item);
        if(document.getElementById(item.filename)){
            // console.log("function new_json 已存在文章 ", item.filename)
            continue;
        }
        var new_div_post = document.createElement("div");
        var new_a = document.createElement("a");
        var new_img = document.createElement("img");
        var new_div_else = document.createElement("div");
        var new_else_h = document.createElement("h3");
        var new_else_a = document.createElement("a");
        var new_pdate = document.createElement("p");
        var new_abstract = document.createElement("p");

        new_div_post.className = "post";
        new_div_else.className = 'else'
        new_else_a.className = 'posttitle';
        new_img.className = "cover";

        new_div_post.id = item.filename;
        new_a.href = item.href;
        new_img.src = item.imgurl;
        new_img.width = "680";
        new_img.height = "440";
        new_a.appendChild(new_img);

        new_div_post.appendChild(new_a);

        new_pdate.innerHTML = item.date;
        new_abstract.innerHTML = item.abstract;
        
        new_else_a.href = item.href;
        new_else_a.title = item.title;
        new_else_a.text = item.title;

        new_else_h.appendChild(new_else_a);
        new_div_else.appendChild(new_pdate);            
        new_div_else.appendChild(new_else_h);
        new_div_else.appendChild(new_abstract);
        
        new_div_post.appendChild(new_div_else);

        primary.append(new_div_post);
        
        // console.log("append done");
        if (data.more){
            if (data.more == "end"){
                get_json_tur = false;
                more_button.innerHTML = "没有更多";
                more_a.href = "";
                more_button.onclick = remove_pager;
            }
            else{
                more_button.innerHTML = "加载更多";
                more_a.href = data.more;
            }
        }
        scrollTo(0,now_y);
    } 
} 

// 该函数只在首页有效 加载文章
function new_json(){
    // console.log("function new_json")
    if (window.location.pathname != site_indexpath){
        // console.log("URL:", window.document.URL,"pathname : ",  window.location.pathname);
        // console.log("if window.location.pathname != site_indexpath --> True")
        return 
    }else{
        // console.log("URL:", window.document.URL,"pathname : ",  window.location.pathname);
    } 
    var more_button = document.getElementById("more_button");
    var more_a = document.getElementById("moreurl");
    if (!more_a){
        return ;
    }
    more_button.innerHTML = "加载中...";
    // console.log(more_button, "加载中")
    var jsonurl = more_a.href 
    json_xhr.open('GET', jsonurl);
    var count = 0
    json_xhr.onreadystatechange = function (){ 
        count = count +1 
        var data = json_xhr.responseText;
        if (data){
            data = JSON.parse(data); 
            add_archive(data);
        } 
    }  
    try{
        json_xhr.send(); 
    } catch (error){
        console.log('error 正在重新请求 ');
        setTimeout("new_json()", 2000);
    }
}

// 滑动到底部获取新文章
$(window).scroll(function () {
//如果窗口划过的距离等于  页面高度减窗口高度   就说明已经到底部了 
// $(window).scrollTop() == $(document).height() - $(window).height() 
// QQ浏览器会算小数点 划过距离不等于页面高度减窗口高度 到底了无效 比喻 99.6666 != 200 - 100 
    // console.log( $(window).scrollTop() , $(document).height() ,  $(window).height() )
    if (get_json_tur ){ 
        if ($(window).scrollTop() > $(document).height() - $(window).height() - 3 ) {  
            // console.log("已经到底部");
            new_json(); 
        }
    } else {
        // console.log("get_json_tur", get_json_tur);
    } 
});    

// 获取滚动条坐标
function getScrollTop(){ 
var scrollTop=0; 
if(document.documentElement&&document.documentElement.scrollTop){ 
    scrollTop=document.documentElement.scrollTop; 
}else if(document.body){ 
    scrollTop=document.body.scrollTop; 
} 
return scrollTop; 
}  

// 首页加载完毕时调用js 加载文章数据
window.onload=function(){ 
if (this.document.getElementsByClassName('post').length < 1 ){
    new_json();
}
else {
    // console.log(this.document.getElementsByClassName('post').length )
}
};

// 已经没有数据的时候 再次点击加载更多 会消失
function remove_pager() { 
    console.log("remove parger")
    $('#pager').remove();
}


function reply_click(obj){
    if ($(obj).attr("class") == "comment-reply-link" ){ 
        var temp_small = "<small><a rel=\"nofollow\" id=\"cancel-comment-reply-link\" href=\"javascript:;\" onclick=\"reply_click(this)\">取消回复</a></small>";
        $("#reply-title").html( $(obj).attr("aria-label")   + temp_small );  
        if ( $("#comment_from_article").val() != $(obj).attr("data-fid") ){
            // 楼层原回复fid 与 input data-fid 不一致 
            alert("error 当前无法写入数据 ")
        }else{
            $("#comment_root_id").val( $(obj).attr("data-commentid") ) ;
        }
    }
    
    if ($(obj).attr("id") == "cancel-comment-reply-link" ){ 
        $("#reply-title").text("发表评论");
        $("#comment_root_id").val( 0 ); 
    }
}

function email_form(){
    var x=document.forms["comment-article-form"]["email"].value; 
	var atpos=x.indexOf("@");
    var dotpos=x.lastIndexOf("."); 
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length){ 
        document.getElementById("comment-form-email-label").innerHTML = "请填写有效的邮箱地址 "
        document.getElementById("comment-form-email-label").style.color = "#FF4500";
        document.getElementById("form-submit").style.visibility="hidden";
  		return false;
    }else{ 
        document.getElementById("comment-form-email-label").innerHTML = "邮箱 * "
        document.getElementById("comment-form-email-label").style.color = "";
        document.getElementById("form-submit").style.visibility="";
        return true;
    }
}
  


$(function () {
    var speed = 600;//滚动速度

    var h=document.body.clientHeight;
 
    //回到底部 
    var windowHeight = parseInt($("body").css("height"));//整个页面的高度 
    $("a.comment-reply-link").click(function () { 
        //alert(h); 
        $('html,body').animate({ 
            scrollTop: h+'px' 
        }, 
        speed);  
    }); 
});
 