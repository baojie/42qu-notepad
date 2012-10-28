$ ->
   $('.back').click ->
        $(window).scrollTop(0)
   date_build = (timestamp) ->
       date = new Date(timestamp * 1000)
       month = date.getMonth() + 1
       year = date.getFullYear()
       day = date.getDate()
       "<p class=\"time\"><strong>" + year + "</strong>" + "<span>" + ("0" + month).substr(-2) + "&nbsp;.&nbsp;" + ("0" + day).substr(-2) + "</span>" + "</p>"


section_tmpl = (o) ->
    _ = $.html()
    for data in o[..-1]
       date_string = date_build(data[0])
       _ """
          <div class="section">
               #{date_string}
               <p class="content">
                     #{data[1]}
               </p>
               <a class='more' href="//#data[2]">#{data[3]}<span>字<span></a>
          </div>
       """
    _.html() 




page_history = (pathname) -> 
    if pathname == "//"
        pathname = "/history"
    else
        pathname = pathname[1..]
    console.log(pathname)

    $.getJSON(
       '//#{document.location.host}/j#{pathname}',
       (data)->
           console.log(data)
           $('.nav').after(section_tmpl(data))
    )


    href="http://42qu.cc/history%s"
    count = 500
    limit = 42
    now = 10
    page(href,count,now,limit)

    

page_history(document.location.pathname)
