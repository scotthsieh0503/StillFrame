(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[678],{3600:(e,t,l)=>{"use strict";l.r(t),l.d(t,{default:()=>n});var s=l(5155),a=l(2115);let r=e=>{let{level:t=1,className:l,...s}=e;return a.createElement("h".concat(t),{className:l,...s})};var c=l(5565),o=l(2651);function n(){let[e,t]=(0,a.useState)([]),[l,n]=(0,a.useState)([]),[i,h]=(0,a.useState)([]);(0,a.useEffect)(()=>{o.A.get("http://localhost:5000/api/photo").then(e=>{n(e.data.result)}).catch(e=>{console.error("Error fetching photos:",e)})},[]);let d=e=>{h(t=>t.includes(e)?t.filter(t=>t!==e):[...t,e])};return(0,s.jsx)("div",{className:"grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]",children:(0,s.jsxs)("main",{className:"flex flex-col gap-8 row-start-2 items-center sm:items-start",children:[(0,s.jsx)(r,{level:1,children:"Photos"}),(0,s.jsx)("input",{type:"file",accept:"image/*",multiple:!0,onChange:e=>{e.target.files&&t(Array.from(e.target.files))}}),(0,s.jsx)("button",{onClick:()=>{e.length>0&&e.forEach(e=>{let l=new FormData;l.append("file",e),o.A.post("http://localhost:5000/api/photo/upload",l).then(e=>{n(t=>[...t,e.data.result]),t([]),console.log("Upload successful:",e.data)}).catch(e=>{console.error("Error uploading file:",e)})})},children:"Upload"}),l.length>0&&(0,s.jsxs)("div",{className:"mt-8",children:[(0,s.jsxs)("div",{children:[(0,s.jsxs)("label",{children:[(0,s.jsx)("input",{type:"checkbox",className:"mr-1 mb-4",onChange:e=>{e.target.checked?h(l):h([])},checked:i.length===l.length&&l.length>0}),"Select All"]}),(0,s.jsx)("button",{className:"float-right",onClick:()=>{i.length>0&&i.forEach(e=>{o.A.delete(e).then(t=>{n(t=>t.filter(t=>t!==e)),h(t=>t.filter(t=>t!==e)),console.log("Delete successful:",t.data)}).catch(e=>{console.error("Error deleting photo:",e)})})},children:"Delete"})]}),(0,s.jsx)("div",{className:"grid grid-cols-4 gap-4",children:l.map(e=>(0,s.jsxs)("div",{className:"flex justify-center items-center cursor-pointer",onClick:()=>d(e),children:[(0,s.jsx)("input",{type:"checkbox",checked:i.includes(e),onChange:()=>d(e),className:"mr-1"}),(0,s.jsx)(c.default,{src:e,width:90,height:90,alt:"Uploaded photo",quality:30,className:"w-32 h-32 object-cover rounded-md",unoptimized:!0})]},e))})]})]})})}},5286:(e,t,l)=>{Promise.resolve().then(l.bind(l,3600))}},e=>{var t=t=>e(e.s=t);e.O(0,[895,441,587,358],()=>t(5286)),_N_E=e.O()}]);