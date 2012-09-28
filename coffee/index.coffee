$ ->
    txt = $ '#textarea'
    date = new Date()
    posted = true
    timer = 0
    txt_val = ''
    post = ->
        if posted && (txt_val!=txt.val())
            posted = false
            $.post(
                location.href,
                {txt: txt.val()},
                ->
                    #$('.save_hint').html("#{date.toLocaleTimeString()} 保存成功!")
                    posted = true 
                    txt_val = txt.val()
            )
        timer && clearTimeout timer
        timer = setTimeout(post,3000)

    key = ->
        posted = false
        return 1

    txt.keydown(key)       
    txt.keyup(key)

    post()
    focus txt[0]


