(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[466],{4982:(e,t,l)=>{Promise.resolve().then(l.bind(l,5329))},5329:(e,t,l)=>{"use strict";l.r(t),l.d(t,{default:()=>m});var s=l(5155),a=l(2115),c=l(8173),r=l.n(c),n=l(5565),i=l(2651);let o="http://stillframe.local:5000",d="".concat("http://stillframe.local:3000","/music/callback");function m(){let[e,t]=(0,a.useState)({clientId:"",clientSecret:"",refreshToken:"",accessToken:"",mode:"default",blur:30,opacity:.5});(0,a.useEffect)(()=>{(async function(){try{let e=(await i.A.get("".concat(o,"/api/setting/SPOTIFY"))).data.result;e.CLIENT_ID&&e.CLIENT_SECRET&&t({clientId:e.CLIENT_ID,clientSecret:e.CLIENT_SECRET,refreshToken:e.REFRESH_TOKEN,accessToken:e.ACCESS_TOKEN,mode:e.MODE,blur:e.BLUR,opacity:e.OPACITY})}catch(e){console.error("Error fetching Spotify settings:",e)}})()},[]),(0,a.useEffect)(()=>{let t=async()=>{try{await i.A.post("".concat(o,"/api/setting/SPOTIFY"),{CLIENT_ID:e.clientId,CLIENT_SECRET:e.clientSecret,REFRESH_TOKEN:e.refreshToken,ACCESS_TOKEN:e.accessToken,MODE:e.mode,BLUR:e.blur,OPACITY:e.opacity})}catch(e){console.error("Error saving Spotify settings:",e)}};e.clientId&&e.clientSecret&&t()},[e]);let l=e=>{let{name:l,value:s}=e.target;t(e=>({...e,[l]:s}))};return(0,s.jsx)("div",{className:"grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]",children:(0,s.jsxs)("main",{className:"flex flex-col gap-8 row-start-2 items-center items-start",children:[(0,s.jsx)("div",{className:"mt-8",children:(0,s.jsxs)("nav",{className:"breadcrumb",children:[(0,s.jsx)(r(),{href:"/",children:"Home"})," / ",(0,s.jsx)("span",{children:"Music"})]})}),!e.refreshToken&&(0,s.jsxs)("div",{children:[(0,s.jsx)("label",{htmlFor:"clientId",children:"Spotify Client ID:"}),(0,s.jsx)("input",{type:"text",id:"clientId",name:"clientId",value:e.clientId,onChange:l,className:"border-b p-2 mb-4 w-full"}),(0,s.jsx)("label",{htmlFor:"clientSecret",children:"Spotify Client Secret:"}),(0,s.jsx)("input",{type:"password",id:"clientSecret",name:"clientSecret",value:e.clientSecret,onChange:l,placeholder:"********",className:"border-b p-2 mb-4 w-full"}),(0,s.jsxs)("button",{onClick:()=>{window.location.href="".concat("https://accounts.spotify.com/authorize","?client_id=").concat(e.clientId,"&redirect_uri=").concat(d,"&response_type=code&scope=").concat("user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-currently-playing")},className:"bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full flex items-center",children:[(0,s.jsx)(n.default,{src:"/images/spotify.svg",alt:"Spotify",width:24,height:24,className:"mr-2"}),"Connect to Spotify"]})]}),e.refreshToken&&(0,s.jsxs)("div",{children:[(0,s.jsxs)("div",{className:"mb-4",children:[(0,s.jsx)("label",{htmlFor:"mode",children:"Album Art Display: "}),(0,s.jsxs)("select",{id:"mode",name:"mode",defaultValue:e.mode,onChange:e=>t(t=>({...t,mode:e.target.value})),className:"ml-2",children:[(0,s.jsx)("option",{value:"default",children:"Default"}),(0,s.jsx)("option",{value:"fullscreen",children:"Fullscreen"})]})]}),(0,s.jsxs)("div",{className:"mb-4",children:[(0,s.jsx)("label",{htmlFor:"blur",children:"Background Blur: "}),(0,s.jsx)("input",{type:"number",id:"blur",name:"blur",min:"0",max:"100",step:"10",value:e.blur,onChange:l,className:"ml-2"})]}),(0,s.jsxs)("div",{className:"mb-4",children:[(0,s.jsx)("label",{htmlFor:"opacity",children:"Background Opacity: "}),(0,s.jsx)("input",{type:"number",id:"opacity",name:"opacity",min:"0",max:"1",step:"0.1",value:e.opacity,onChange:l,className:"ml-2"})]}),(0,s.jsxs)("div",{children:[(0,s.jsx)("h2",{children:"Preview: "}),(0,s.jsx)("img",{src:"".concat(o,"/api/music/currently-playing/image/PIL"),alt:"Currently Playing"})]})]})]})})}}},e=>{var t=t=>e(e.s=t);e.O(0,[651,565,441,587,358],()=>t(4982)),_N_E=e.O()}]);