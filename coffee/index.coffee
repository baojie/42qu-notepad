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
    if ! posted && (txt_val!=txt.val())
        posted = false
        fav("/css/img/load.gif")
        $.post(
            location.href,
            {txt: txt.val()},
            ->
                fav("/css/img/fav.gif")
                posted = true 
                txt_val = txt.val()
        )
    timer && clearTimeout timer
    timer = setTimeout(post,3000)

key = ->
    if posted
        fav('/css/img/favicon.gif')
    posted = false
    return 1

txt.keydown(key)       
txt.keyup(key)

post()
focus txt[0]


