/*!
 * IE10 viewport hack for Surface/desktop Windows 8 bug
 * Copyright 2014 Twitter, Inc.
 * Licensed under the Creative Commons Attribution 3.0 Unported License. For
 * details, see http://creativecommons.org/licenses/by/3.0/.
 */

// See the Getting Started docs for more information:
// http://getbootstrap.com/getting-started/#support-ie10-width

(function () {
  'use strict';
  if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement('style')
    msViewportStyle.appendChild(
      document.createTextNode(
        '@-ms-viewport{width:auto!important}'
      )
    )
    document.querySelector('head').appendChild(msViewportStyle)
  }
})();

/*! jquery.cookie v1.4.1 | MIT */
!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?a(require("jquery")):a(django.jQuery)}(function(a){function b(a){return h.raw?a:encodeURIComponent(a)}function c(a){return h.raw?a:decodeURIComponent(a)}function d(a){return b(h.json?JSON.stringify(a):String(a))}function e(a){0===a.indexOf('"')&&(a=a.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return a=decodeURIComponent(a.replace(g," ")),h.json?JSON.parse(a):a}catch(b){}}function f(b,c){var d=h.raw?b:e(b);return a.isFunction(c)?c(d):d}var g=/\+/g,h=a.cookie=function(e,g,i){if(void 0!==g&&!a.isFunction(g)){if(i=a.extend({},h.defaults,i),"number"==typeof i.expires){var j=i.expires,k=i.expires=new Date;k.setTime(+k+864e5*j)}return document.cookie=[b(e),"=",d(g),i.expires?"; expires="+i.expires.toUTCString():"",i.path?"; path="+i.path:"",i.domain?"; domain="+i.domain:"",i.secure?"; secure":""].join("")}for(var l=e?void 0:{},m=document.cookie?document.cookie.split("; "):[],n=0,o=m.length;o>n;n++){var p=m[n].split("="),q=c(p.shift()),r=p.join("=");if(e&&e===q){l=f(r,g);break}e||void 0===(r=f(r))||(l[q]=r)}return l};h.defaults={},a.removeCookie=function(b,c){return void 0===a.cookie(b)?!1:(a.cookie(b,"",a.extend({},c,{expires:-1})),!a.cookie(b))}});

(function ($) {
  $(document).ready(function(){
    var show_hide_sidebar_menu = function () {
      hidden_menu = $('#sidebar-menu').data('hidden');
      main_classes = 'col-xs-6 col-xs-offset-6 col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2';
      if (hidden_menu) {
        $('.main').addClass(main_classes).removeClass('col-sm-12');
        $('.sidebar-menu').css('left', '0').data('hidden', false);
        $('.django-admin-title').hide();
        $.removeCookie('hidden_sidebar_menu', {path: '/'});
      } else {
        $('.main').removeClass(main_classes).addClass('col-sm-12');
        $('.sidebar-menu').css('left', '-50%').data('hidden', true);
        $('.django-admin-title').fadeIn();
        $.cookie('hidden_sidebar_menu', true, {path: '/'});
      }
    };
    if (!$('body').hasClass('popup')) {
      if ($.cookie('hidden_sidebar_menu')) {
        /* always show on change_list.html */
        if (!$('body').hasClass('change-list')) {
          show_hide_sidebar_menu();
        }
      }
      $('.show-hide-sidebar-menu').on('click', function(e){
        show_hide_sidebar_menu();
        e.preventDefault();
      });
    }
    // list models
    $('.nav-sidebar li:first-child a').on('click', function () {
      var $nav_sidebar = $(this).closest('.nav-sidebar');
      if ($nav_sidebar.hasClass('show-models')) {
        $nav_sidebar.removeClass('show-models');
      } else {
        $nav_sidebar.addClass('show-models');
      }
      return false;
    });
  });
})(django.jQuery);
