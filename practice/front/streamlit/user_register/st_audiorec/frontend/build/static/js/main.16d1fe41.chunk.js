(this.webpackJsonpstreamlit_component_template=this.webpackJsonpstreamlit_component_template||[]).push([[0],{17:function(e,t,a){e.exports=a(28)},28:function(e,t,a){"use strict";a.r(t);var n=a(6),r=a.n(n),o=a(15),c=a.n(o),i=a(0),l=a(1),s=a(2),u=a(3),d=a(8),m=a(11),p=(a(27),function(e){Object(s.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,o=new Array(n),c=0;c<n;c++)o[c]=arguments[c];return(e=t.call.apply(t,[this].concat(o))).state={isFocused:!1,recordState:null,audioDataURL:"",reset:!1,regis:!1},e.render=function(){var t=e.props.theme,a={},n=e.state.recordState;if(t){var o="1px solid ".concat(e.state.isFocused?t.primaryColor:"gray");a.border=o,a.outline=o}return r.a.createElement(r.a.Fragment,null,r.a.createElement("span",null,r.a.createElement("div",{className:"audio_rec_cover"},r.a.createElement("div",{className:"audio_canvas"},r.a.createElement(m.b,{state:n,onStop:e.onStop_audio,type:"audio/wav",backgroundColor:"rgb(255, 255, 255)",foregroundColor:"rgb(255,76,75)",canvasWidth:"",canvasHeight:39})),r.a.createElement("div",null,r.a.createElement("button",{id:"record",onClick:e.onClick_start},"\ub179\uc74c"))),r.a.createElement("div",{className:"audio_player"},r.a.createElement("audio",{id:"audio",controls:!0,src:e.state.audioDataURL}))))},e.onClick_start=function(t){if("\ub179\uc74c"===t.target.innerText)return e.setState({reset:!1,audioDataURL:"",recordState:m.a.START}),d.a.setComponentValue(""),t.target.innerText="\uc911\uc9c0",t.target.id="stop",!0;e.setState({reset:!1,recordState:m.a.STOP,regis:!0}),t.target.innerText="\ub179\uc74c",t.target.id="record"},e.onClick_regis=function(e){},e.onClick_reset=function(){e.setState({reset:!0,audioDataURL:"",recordState:m.a.STOP}),d.a.setComponentValue("")},e.onClick_continue=function(){if(""!==e.state.audioDataURL){var t=(new Date).toLocaleString(),a="streamlit_audio_"+(t=(t=(t=t.replace(" ","")).replace(/_/g,"")).replace(",",""))+".wav",n=document.createElement("a");n.style.display="none",n.href=e.state.audioDataURL,n.download=a,document.body.appendChild(n),n.click()}},e.onStop_audio=function(t){!0===e.state.reset?(e.setState({audioDataURL:""}),d.a.setComponentValue("")):(e.setState({audioDataURL:t.url}),fetch(t.url).then((function(e){return e.blob()})).then((function(e){return new Response(e).arrayBuffer()})).then((function(e){d.a.setComponentValue({arr:new Uint8Array(e)})})))},e}return Object(i.a)(a)}(d.b)),f=Object(d.c)(p);d.a.setComponentReady(),d.a.setFrameHeight(),c.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(f,null)),document.getElementById("root"))}},[[17,1,2]]]);
//# sourceMappingURL=main.16d1fe41.chunk.js.map