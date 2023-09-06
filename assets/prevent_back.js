window.addEventListener("load", function(){
    window.history.pushState(null, null, window.location.href);
    window.onpopstate = function(event) {
        window.history.go(1);
    };
});