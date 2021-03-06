(function() {
  var date_build, section_tmpl;

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
      _("<div class=\"section\">\n     " + date_string + "\n     <p class=\"content\">\n           " + ($.escape(data[1])) + "\n     </p>\n     <a class=\"more\" href=\"javascript:void(0)\" rel=\"" + data[2] + "\">" + data[3] + "<span>字<span></a>\n</div>");
    }
    return _.html();
  };

  $(".section .more").live("click", function() {
    var self;
    self = this;
    self.href = "/:id/" + this.rel;
    return setTimeout(function() {
      return self.href = "javascript:void(0)";
    }, 0);
  });

  window.page_history = function(page) {
    var hash, note_list;
    if (!page) {
      page = 1;
    }
    if (page > 1) {
      hash = "#!" + page;
    } else {
      hash = '';
    }
    location.hash = hash;
    note_list = $('#note-list');
    $('.page').html('<div id="note_list_loading"/>');
    return $.getJSON("/:j/history-" + page, function(data) {
      var count, href, limit, now;
      note_list.html(section_tmpl(data));
      href = "javascript:page_history($page);void(0);";
      count = data[data.length - 1][0];
      now = data[data.length - 1][1];
      limit = data[data.length - 1][2];
      $('.page').html(pager(href, count, now, limit));
      return $(window).scrollTop(0);
    });
  };

  page_history(location.hash.slice(2));

}).call(this);
