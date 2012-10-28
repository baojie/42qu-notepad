txt = $ '#txt'
date = new Date()
posted = true
timer = 0

txt_val = ''

fav = (href)-> 
    $('#favicon').remove()
    link = document.createElement('link')
    link.type = 'image/gif'
    link.rel = 'shortcut icon'
    link.id = 'favicon'
    link.href = href
    document.getElementsByTagName('head')[0].appendChild(link)


post = ->
    val = $.trim(txt.val())
    if ! posted && (txt_val!=val)
        posted = false
        fav("/css/img/load.gif")
        $.post(
            location.href,
            {txt: val},
            ->
                fav("/css/img/fav.gif")
                posted = true 
                txt_val = val
        )
    timer && clearTimeout timer
    timer = setTimeout(post,3000)

key = ->
    if posted and txt_val!=$.trim(txt.val())
        fav('/css/img/favicon.gif')
        posted = false
    return 1

$ ->
    txt_val = $.trim(txt.val())
    txt.keydown(key)       
    txt.keyup(key)

    post()
    focus txt[0]
    window.onbeforeunload = ->
        if posted = false
            post()


###
    $('.more').hover(
         
        ->
            $(this).animate(
                "margin-left":"21px",
                1500,
                "linear"
            )
        ,
        ->
            $(this).animate(
                "margin-left":"13px",
                1500,
                "linear"
            )
    )
    
###
