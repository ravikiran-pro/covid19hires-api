(this["webpackJsonpreact-tut"]=this["webpackJsonpreact-tut"]||[]).push([[0],{16:function(e,n,t){e.exports=t(24)},24:function(e,n,t){"use strict";t.r(n);var o=t(0),a=t.n(o),i=t(6),r=t.n(i),c=t(11),l=t(12),s=t(8),h=t(15),d=t(14),u=t(7),f=t(9),w=function(e){Object(h.a)(t,e);var n=Object(d.a)(t);function t(e,o){var a;return Object(c.a)(this,t),(a=n.call(this,e,o)).handleShow=a.handleShow.bind(Object(s.a)(a)),a.handleClose=a.handleClose.bind(Object(s.a)(a)),a.state={show:!1},a}return Object(l.a)(t,[{key:"handleClose",value:function(){this.setState({show:!1})}},{key:"handleShow",value:function(){this.setState({show:!0})}},{key:"render",value:function(){return a.a.createElement(a.a.Fragment,null,a.a.createElement(f.a,{variant:"primary",onClick:this.handleShow},"Launch demo modal"),a.a.createElement(u.a,{show:this.state.show,onHide:this.handleClose},a.a.createElement(u.a.Header,{closeButton:!0},a.a.createElement(u.a.Title,null,"Modal heading")),a.a.createElement(u.a.Body,null,"Woohoo, you're reading this text in a modal!"),a.a.createElement(u.a.Footer,null,a.a.createElement(f.a,{variant:"secondary",onClick:this.handleClose},"Close"),a.a.createElement(f.a,{variant:"primary",onClick:this.handleClose},"Save Changes"))))}}]),t}(a.a.Component),v=Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));function g(e,n){navigator.serviceWorker.register(e).then((function(e){e.onupdatefound=function(){var t=e.installing;null!=t&&(t.onstatechange=function(){"installed"===t.state&&(navigator.serviceWorker.controller?(console.log("New content is available and will be used when all tabs for this page are closed. See https://bit.ly/CRA-PWA."),n&&n.onUpdate&&n.onUpdate(e)):(console.log("Content is cached for offline use."),n&&n.onSuccess&&n.onSuccess(e)))})}})).catch((function(e){console.error("Error during service worker registration:",e)}))}t(23);r.a.render(a.a.createElement(w,null),document.getElementById("root")),function(e){if("serviceWorker"in navigator){if(new URL("",window.location.href).origin!==window.location.origin)return;window.addEventListener("load",(function(){var n="".concat("","/service-worker.js");v?(!function(e,n){fetch(e,{headers:{"Service-Worker":"script"}}).then((function(t){var o=t.headers.get("content-type");404===t.status||null!=o&&-1===o.indexOf("javascript")?navigator.serviceWorker.ready.then((function(e){e.unregister().then((function(){window.location.reload()}))})):g(e,n)})).catch((function(){console.log("No internet connection found. App is running in offline mode.")}))}(n,e),navigator.serviceWorker.ready.then((function(){console.log("This web app is being served cache-first by a service worker. To learn more, visit https://bit.ly/CRA-PWA")}))):g(n,e)}))}}()}},[[16,1,2]]]);
//# sourceMappingURL=main.1cdf8ebd.chunk.js.map