(function($) {
    $.fn.isAfter = function(sel){
        return this.prevAll(sel).length !== 0;
    }
    $.fn.isBefore= function(sel){
        return this.nextAll(sel).length !== 0;
    }
})(django.jQuery);