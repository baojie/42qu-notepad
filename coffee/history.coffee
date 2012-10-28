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
        for data in o
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

   fake_data=[[1351338972,"是一本兼具趣味性、实用性与学习性的操作系统图书。作者川合秀实从计算机的构造、汇编语言、C语言开始解说，让读者在实...",'baidu.com',22],[1351338972,"是一本兼具趣味性、实用性与学习性的操作系统图书。作者川合秀实从计算机的构造、汇编语言、C语言开始解说，让读者在实...",'baidu.com'],[1351338972,"fdfjdkfjdkfjkdf",'baidu.com',22],[1351338972,"是一本兼具趣味性、实用性与学习性的操作系统图书。作者川合秀实从计算机的构造、汇编语言、C语言开始解说，让读者在实...",'baidu.com',22],[1351338972,"是一本兼具趣味性、实用性与学习性的操作系统图书。作者川合秀实从计算机的构造、汇编语言、C语言开始解说，让读者在实...",'baidu.com',22],[1351338972,"fdfjdkfjdkfjkdf",'baidu.com',22],[1351338972,"是一本兼具趣味性、实用性与学习性的操作系统图书。作者川合秀实从计算机的构造、汇编语言、C语言开始解说，让读者在实...",'baidu.com',22]];

   $('.nav').after(section_tmpl(fake_data));

   href="http://42qu.cc/history%s"
   count = 500
   limit = 42
   now = 10
   page(href,count,now,limit)
