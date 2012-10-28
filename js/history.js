(function() {
  var date_build, page_history, section_tmpl;

  $(function() {
    return $('.back').click(function() {
      return $(window).scrollTop(0);
    });
  });

  date_build = function(timestamp) {
    var date, day, month, year;
    date = new Date(timestamp * 1000);
    month = date.getMonth() + 1;
    year = date.getFullYear();
    day = date.getDate();
    return "<p class=\"time\"><strong>" + year + "</strong>" + "<span>" + ("0" + month).substr(-2) + "&nbsp;.&nbsp;" + ("0" + day).substr(-2) + "</span>" + "</p>";
  };

  section_tmpl = function(o) {
    var data, date_string, _, _i, _len, _ref;
    _ = $.html();
    _ref = o.slice(0, -1);
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      data = _ref[_i];
      date_string = date_build(data[0]);
      _("<div class=\"section\">\n     " + date_string + "\n     <p class=\"content\">\n           " + ($.escape(data[1])) + "\n     </p>\n     <a class='more' href=\"/:id/" + data[2] + "\">" + data[3] + "<span>字<span></a>\n</div>");
    }
    return _.html();
  };

  page_history = function(pathname) {
    if (pathname === "/:") {
      pathname = "/history";
    } else {
      pathname = "/" + pathname.slice(2);
    }
    console.log("/:j" + pathname);
    return $.getJSON("/:j" + pathname, function(data) {
      var count, href, limit, now;
      console.log(data);
      $('.nav').after(section_tmpl(data));
      href = "http://42qu.cc/history%s";
      count = data[data.length - 1][0];
      now = data[data.length - 1][1];
      limit = data[data.length - 1][2];
      return page(href, count, now, limit);
    });
  };

  page_history(document.location.pathname);

}).call(this);
