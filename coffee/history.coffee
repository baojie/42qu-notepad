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
    for data in o[..-2]
       date_string = date_build(data[0])
       _ """
          <div class="section">
               #{date_string}
               <p class="content">
                     #{$.escape(data[1])}
               </p>
               <a class='more' href="/:id/#{data[2]}">#{data[3]}<span>字<span></a>
          </div>
       """
    _.html() 




page_history = (pathname) -> 
    if pathname == "/:"
        pathname = "/history"
    else
        pathname = "/#{pathname[2..]}"
    console.log("/:j#{pathname}")

    $.getJSON(
       "/:j#{pathname}",
       (data)->
           console.log(data)
           $('.nav').after(section_tmpl(data))
           href="http://42qu.cc/history%s"
           count = data[data.length-1][0]
           now = data[data.length-1][1]
           limit = data[data.length-1][2]
           page(href,count,now,limit)
    )



    

page_history(document.location.pathname)
