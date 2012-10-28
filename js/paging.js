(function() {
  var PAGE_LIMIT, PAGE_NO_TEMPLATE, formatstr, template;

  PAGE_LIMIT = 42;

  PAGE_NO_TEMPLATE = "<a href=\"%s\">%s</a>";

  template = "<div class=\"page\"></div>";

  formatstr = function(href, page_template, hreftext, templatetext) {
    href = href.replace("%s", hreftext);
    page_template = page_template.replace(/\"%s\"/, href);
    page_template = page_template.replace(/%s/, templatetext);
    return page_template;
  };

  window.page = function(href, count, now, limit) {
    var begin, end, htm, i, links, merge_begin, merge_end, omit_len, pageLink, paging, scope, show_begin_mid, spanNow, total;
    now = parseInt(now);
    if (now <= 0) {
      now = 1;
    }
    end = Math.floor((count + limit - 1) / limit);
    if (now > end) {
      now = end;
    }
    scope = 2;
    total = Math.floor((count + limit - 1) / limit);
    if (total > 1) {
      merge_begin = false;
      merge_end = false;
      omit_len = scope + 3;
      if (total <= (scope + omit_len + 1)) {
        begin = 1;
        end = total;
      } else {
        if (now > omit_len) {
          merge_begin = true;
          begin = now - scope;
        } else {
          begin = 1;
        }
        if ((total - now) >= omit_len) {
          merge_end = true;
          end = now + scope;
        } else {
          end = total;
        }
        if ((end - begin) < (scope * 2)) {
          if (now <= omit_len) {
            end = Math.min(begin + scope * 2, total);
          } else {
            begin = Math.max(end - scope * 2, 1);
          }
          if (!(begin > omit_len)) {
            merge_begin = false;
            begin = 1;
          }
          if (!((total - end) >= omit_len)) {
            merge_end = false;
            end = total;
          }
        }
      }
    }
    links = [];
    if (now > 1) {
      pageLink = formatstr(href, PAGE_NO_TEMPLATE, now - 1, "&lt");
      links.push(pageLink);
    } else {
      links.push("<span class=\"plt\">&lt;</span>");
    }
    if (merge_begin) {
      pageLink = formatstr(href, PAGE_NO_TEMPLATE, 1, 1);
      pageLink += "...";
      links.push(pageLink);
      show_begin_mid = false;
      if (begin > 8) {
        show_begin_mid = Math.floor(begin / 2);
      }
      if (show_begin_mid) {
        pageLink = formatstr(href, PAGE_NO_TEMPLATE, show_begin_mid, show_begin_mid);
        pageLink += "...";
        links.push(pageLink);
      }
    }
    i = begin;
    while (i < now) {
      pageLink = formatstr(href, PAGE_NO_TEMPLATE, i, i);
      links.push(pageLink);
      i++;
    }
    spanNow = "<span class=\"now\">%s</span>";
    spanNow = spanNow.replace(/%s/, now);
    links.push(spanNow);
    i = now + 1;
    while (i < end + 1) {
      pageLink = formatstr(href, PAGE_NO_TEMPLATE, i, i);
      links.push(pageLink);
      i++;
    }
    if (merge_end) {
      links.push("...");
    }
    if (now < total) {
      pageLink = formatstr(href, PAGE_NO_TEMPLATE, now + 1, "&gt");
      links.push(pageLink);
    } else {
      links.push("<span class=\"pgt\">&gt;</span>");
    }
    htm = "";
    i = 0;
    while (i < links.length) {
      htm += links[i];
      i++;
    }
    paging = $(template);
    $(htm).appendTo(paging);
    return paging.appendTo($("body"));
  };

}).call(this);
