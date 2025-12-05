var W,_,se,Ce,S,oe,le,ie,de,V,J,N,pe,T={},ce=[],Re=/acit|ex(?:s|g|n|p|$)|rph|grid|ows|mnc|ntw|ine[ch]|zoo|^ord|itera/i,U=Array.isArray;function C(t,e){for(var r in e)t[r]=e[r];return t}function q(t){t&&t.parentNode&&t.parentNode.removeChild(t)}function Ee(t,e,r){var a,s,o,l={};for(o in e)o=="key"?a=e[o]:o=="ref"?s=e[o]:l[o]=e[o];if(arguments.length>2&&(l.children=arguments.length>3?W.call(arguments,2):r),typeof t=="function"&&t.defaultProps!=null)for(o in t.defaultProps)l[o]===void 0&&(l[o]=t.defaultProps[o]);return $(t,l,a,s,null)}function $(t,e,r,a,s){var o={type:t,props:e,key:r,ref:a,__k:null,__:null,__b:0,__e:null,__c:null,constructor:void 0,__v:s??++se,__i:-1,__u:0};return s==null&&_.vnode!=null&&_.vnode(o),o}function L(){return{current:null}}function x(t){return t.children}function k(t,e){this.props=t,this.context=e}function D(t,e){if(e==null)return t.__?D(t.__,t.__i+1):null;for(var r;e<t.__k.length;e++)if((r=t.__k[e])!=null&&r.__e!=null)return r.__e;return typeof t.type=="function"?D(t):null}function he(t){var e,r;if((t=t.__)!=null&&t.__c!=null){for(t.__e=t.__c.base=null,e=0;e<t.__k.length;e++)if((r=t.__k[e])!=null&&r.__e!=null){t.__e=t.__c.base=r.__e;break}return he(t)}}function X(t){(!t.__d&&(t.__d=!0)&&S.push(t)&&!O.__r++||oe!=_.debounceRendering)&&((oe=_.debounceRendering)||le)(O)}function O(){for(var t,e,r,a,s,o,l,d=1;S.length;)S.length>d&&S.sort(ie),t=S.shift(),d=S.length,t.__d&&(r=void 0,a=void 0,s=(a=(e=t).__v).__e,o=[],l=[],e.__P&&((r=C({},a)).__v=a.__v+1,_.vnode&&_.vnode(r),G(e.__P,r,a,e.__n,e.__P.namespaceURI,32&a.__u?[s]:null,o,s??D(a),!!(32&a.__u),l),r.__v=a.__v,r.__.__k[r.__i]=r,fe(o,r,l),a.__e=a.__=null,r.__e!=s&&he(r)));O.__r=0}function ue(t,e,r,a,s,o,l,d,h,i,u){var n,m,c,b,y,v,g,f=a&&a.__k||ce,R=e.length;for(h=Se(r,e,f,h,R),n=0;n<R;n++)(c=r.__k[n])!=null&&(m=c.__i==-1?T:f[c.__i]||T,c.__i=n,v=G(t,c,m,s,o,l,d,h,i,u),b=c.__e,c.ref&&m.ref!=c.ref&&(m.ref&&Y(m.ref,null,c),u.push(c.ref,c.__c||b,c)),y==null&&b!=null&&(y=b),(g=!!(4&c.__u))||m.__k===c.__k?h=_e(c,h,t,g):typeof c.type=="function"&&v!==void 0?h=v:b&&(h=b.nextSibling),c.__u&=-7);return r.__e=y,h}function Se(t,e,r,a,s){var o,l,d,h,i,u=r.length,n=u,m=0;for(t.__k=new Array(s),o=0;o<s;o++)(l=e[o])!=null&&typeof l!="boolean"&&typeof l!="function"?(typeof l=="string"||typeof l=="number"||typeof l=="bigint"||l.constructor==String?l=t.__k[o]=$(null,l,null,null,null):U(l)?l=t.__k[o]=$(x,{children:l},null,null,null):l.constructor==null&&l.__b>0?l=t.__k[o]=$(l.type,l.props,l.key,l.ref?l.ref:null,l.__v):t.__k[o]=l,h=o+m,l.__=t,l.__b=t.__b+1,(i=l.__i=Pe(l,r,h,n))!=-1&&(n--,(d=r[i])&&(d.__u|=2)),d==null||d.__v==null?(i==-1&&(s>u?m--:s<u&&m++),typeof l.type!="function"&&(l.__u|=4)):i!=h&&(i==h-1?m--:i==h+1?m++:(i>h?m--:m++,l.__u|=4))):t.__k[o]=null;if(n)for(o=0;o<u;o++)(d=r[o])!=null&&(2&d.__u)==0&&(d.__e==a&&(a=D(d)),me(d,d));return a}function _e(t,e,r,a){var s,o;if(typeof t.type=="function"){for(s=t.__k,o=0;s&&o<s.length;o++)s[o]&&(s[o].__=t,e=_e(s[o],e,r,a));return e}t.__e!=e&&(a&&(e&&t.type&&!e.parentNode&&(e=D(t)),r.insertBefore(t.__e,e||null)),e=t.__e);do e=e&&e.nextSibling;while(e!=null&&e.nodeType==8);return e}function Pe(t,e,r,a){var s,o,l,d=t.key,h=t.type,i=e[r],u=i!=null&&(2&i.__u)==0;if(i===null&&d==null||u&&d==i.key&&h==i.type)return r;if(a>(u?1:0)){for(s=r-1,o=r+1;s>=0||o<e.length;)if((i=e[l=s>=0?s--:o++])!=null&&(2&i.__u)==0&&d==i.key&&h==i.type)return l}return-1}function ne(t,e,r){e[0]=="-"?t.setProperty(e,r??""):t[e]=r==null?"":typeof r!="number"||Re.test(e)?r:r+"px"}function j(t,e,r,a,s){var o,l;e:if(e=="style")if(typeof r=="string")t.style.cssText=r;else{if(typeof a=="string"&&(t.style.cssText=a=""),a)for(e in a)r&&e in r||ne(t.style,e,"");if(r)for(e in r)a&&r[e]==a[e]||ne(t.style,e,r[e])}else if(e[0]=="o"&&e[1]=="n")o=e!=(e=e.replace(de,"$1")),l=e.toLowerCase(),e=l in t||e=="onFocusOut"||e=="onFocusIn"?l.slice(2):e.slice(2),t.l||(t.l={}),t.l[e+o]=r,r?a?r.u=a.u:(r.u=V,t.addEventListener(e,o?N:J,o)):t.removeEventListener(e,o?N:J,o);else{if(s=="http://www.w3.org/2000/svg")e=e.replace(/xlink(H|:h)/,"h").replace(/sName$/,"s");else if(e!="width"&&e!="height"&&e!="href"&&e!="list"&&e!="form"&&e!="tabIndex"&&e!="download"&&e!="rowSpan"&&e!="colSpan"&&e!="role"&&e!="popover"&&e in t)try{t[e]=r??"";break e}catch{}typeof r=="function"||(r==null||r===!1&&e[4]!="-"?t.removeAttribute(e):t.setAttribute(e,e=="popover"&&r==1?"":r))}}function ae(t){return function(e){if(this.l){var r=this.l[e.type+t];if(e.t==null)e.t=V++;else if(e.t<r.u)return;return r(_.event?_.event(e):e)}}}function G(t,e,r,a,s,o,l,d,h,i){var u,n,m,c,b,y,v,g,f,R,E,M,H,re,I,F,z,w=e.type;if(e.constructor!=null)return null;128&r.__u&&(h=!!(32&r.__u),o=[d=e.__e=r.__e]),(u=_.__b)&&u(e);e:if(typeof w=="function")try{if(g=e.props,f="prototype"in w&&w.prototype.render,R=(u=w.contextType)&&a[u.__c],E=u?R?R.props.value:u.__:a,r.__c?v=(n=e.__c=r.__c).__=n.__E:(f?e.__c=n=new w(g,E):(e.__c=n=new k(g,E),n.constructor=w,n.render=He),R&&R.sub(n),n.state||(n.state={}),n.__n=a,m=n.__d=!0,n.__h=[],n._sb=[]),f&&n.__s==null&&(n.__s=n.state),f&&w.getDerivedStateFromProps!=null&&(n.__s==n.state&&(n.__s=C({},n.__s)),C(n.__s,w.getDerivedStateFromProps(g,n.__s))),c=n.props,b=n.state,n.__v=e,m)f&&w.getDerivedStateFromProps==null&&n.componentWillMount!=null&&n.componentWillMount(),f&&n.componentDidMount!=null&&n.__h.push(n.componentDidMount);else{if(f&&w.getDerivedStateFromProps==null&&g!==c&&n.componentWillReceiveProps!=null&&n.componentWillReceiveProps(g,E),e.__v==r.__v||!n.__e&&n.shouldComponentUpdate!=null&&n.shouldComponentUpdate(g,n.__s,E)===!1){for(e.__v!=r.__v&&(n.props=g,n.state=n.__s,n.__d=!1),e.__e=r.__e,e.__k=r.__k,e.__k.some(function(P){P&&(P.__=e)}),M=0;M<n._sb.length;M++)n.__h.push(n._sb[M]);n._sb=[],n.__h.length&&l.push(n);break e}n.componentWillUpdate!=null&&n.componentWillUpdate(g,n.__s,E),f&&n.componentDidUpdate!=null&&n.__h.push(function(){n.componentDidUpdate(c,b,y)})}if(n.context=E,n.props=g,n.__P=t,n.__e=!1,H=_.__r,re=0,f){for(n.state=n.__s,n.__d=!1,H&&H(e),u=n.render(n.props,n.state,n.context),I=0;I<n._sb.length;I++)n.__h.push(n._sb[I]);n._sb=[]}else do n.__d=!1,H&&H(e),u=n.render(n.props,n.state,n.context),n.state=n.__s;while(n.__d&&++re<25);n.state=n.__s,n.getChildContext!=null&&(a=C(C({},a),n.getChildContext())),f&&!m&&n.getSnapshotBeforeUpdate!=null&&(y=n.getSnapshotBeforeUpdate(c,b)),F=u,u!=null&&u.type===x&&u.key==null&&(F=ge(u.props.children)),d=ue(t,U(F)?F:[F],e,r,a,s,o,l,d,h,i),n.base=e.__e,e.__u&=-161,n.__h.length&&l.push(n),v&&(n.__E=n.__=null)}catch(P){if(e.__v=null,h||o!=null)if(P.then){for(e.__u|=h?160:128;d&&d.nodeType==8&&d.nextSibling;)d=d.nextSibling;o[o.indexOf(d)]=null,e.__e=d}else{for(z=o.length;z--;)q(o[z]);K(e)}else e.__e=r.__e,e.__k=r.__k,P.then||K(e);_.__e(P,e,r)}else o==null&&e.__v==r.__v?(e.__k=r.__k,e.__e=r.__e):d=e.__e=De(r.__e,e,r,a,s,o,l,h,i);return(u=_.diffed)&&u(e),128&e.__u?void 0:d}function K(t){t&&t.__c&&(t.__c.__e=!0),t&&t.__k&&t.__k.forEach(K)}function fe(t,e,r){for(var a=0;a<r.length;a++)Y(r[a],r[++a],r[++a]);_.__c&&_.__c(e,t),t.some(function(s){try{t=s.__h,s.__h=[],t.some(function(o){o.call(s)})}catch(o){_.__e(o,s.__v)}})}function ge(t){return typeof t!="object"||t==null||t.__b&&t.__b>0?t:U(t)?t.map(ge):C({},t)}function De(t,e,r,a,s,o,l,d,h){var i,u,n,m,c,b,y,v=r.props||T,g=e.props,f=e.type;if(f=="svg"?s="http://www.w3.org/2000/svg":f=="math"?s="http://www.w3.org/1998/Math/MathML":s||(s="http://www.w3.org/1999/xhtml"),o!=null){for(i=0;i<o.length;i++)if((c=o[i])&&"setAttribute"in c==!!f&&(f?c.localName==f:c.nodeType==3)){t=c,o[i]=null;break}}if(t==null){if(f==null)return document.createTextNode(g);t=document.createElementNS(s,f,g.is&&g),d&&(_.__m&&_.__m(e,o),d=!1),o=null}if(f==null)v===g||d&&t.data==g||(t.data=g);else{if(o=o&&W.call(t.childNodes),!d&&o!=null)for(v={},i=0;i<t.attributes.length;i++)v[(c=t.attributes[i]).name]=c.value;for(i in v)if(c=v[i],i!="children"){if(i=="dangerouslySetInnerHTML")n=c;else if(!(i in g)){if(i=="value"&&"defaultValue"in g||i=="checked"&&"defaultChecked"in g)continue;j(t,i,null,c,s)}}for(i in g)c=g[i],i=="children"?m=c:i=="dangerouslySetInnerHTML"?u=c:i=="value"?b=c:i=="checked"?y=c:d&&typeof c!="function"||v[i]===c||j(t,i,c,v[i],s);if(u)d||n&&(u.__html==n.__html||u.__html==t.innerHTML)||(t.innerHTML=u.__html),e.__k=[];else if(n&&(t.innerHTML=""),ue(e.type=="template"?t.content:t,U(m)?m:[m],e,r,a,f=="foreignObject"?"http://www.w3.org/1999/xhtml":s,o,l,o?o[0]:r.__k&&D(r,0),d,h),o!=null)for(i=o.length;i--;)q(o[i]);d||(i="value",f=="progress"&&b==null?t.removeAttribute("value"):b!=null&&(b!==t[i]||f=="progress"&&!b||f=="option"&&b!=v[i])&&j(t,i,b,v[i],s),i="checked",y!=null&&y!=t[i]&&j(t,i,y,v[i],s))}return t}function Y(t,e,r){try{if(typeof t=="function"){var a=typeof t.__u=="function";a&&t.__u(),a&&e==null||(t.__u=t(e))}else t.current=e}catch(s){_.__e(s,r)}}function me(t,e,r){var a,s;if(_.unmount&&_.unmount(t),(a=t.ref)&&(a.current&&a.current!=t.__e||Y(a,null,e)),(a=t.__c)!=null){if(a.componentWillUnmount)try{a.componentWillUnmount()}catch(o){_.__e(o,e)}a.base=a.__P=null}if(a=t.__k)for(s=0;s<a.length;s++)a[s]&&me(a[s],e,r||typeof t.type!="function");r||q(t.__e),t.__c=t.__=t.__e=void 0}function He(t,e,r){return this.constructor(t,r)}function be(t,e,r){var a,s,o,l;e==document&&(e=document.documentElement),_.__&&_.__(t,e),s=(a=typeof r=="function")?null:r&&r.__k||e.__k,o=[],l=[],G(e,t=(!a&&r||e).__k=Ee(x,null,[t]),s||T,T,e.namespaceURI,!a&&r?[r]:s?null:e.firstChild?W.call(e.childNodes):null,o,!a&&r?r:s?s.__e:e.firstChild,a,l),fe(o,t,l)}function ve(t){function e(r){var a,s;return this.getChildContext||(a=new Set,(s={})[e.__c]=this,this.getChildContext=function(){return s},this.componentWillUnmount=function(){a=null},this.shouldComponentUpdate=function(o){this.props.value!=o.value&&a.forEach(function(l){l.__e=!0,X(l)})},this.sub=function(o){a.add(o);var l=o.componentWillUnmount;o.componentWillUnmount=function(){a&&a.delete(o),l&&l.call(o)}}),r.children}return e.__c="__cC"+pe++,e.__=t,e.Provider=e.__l=(e.Consumer=function(r,a){return r.children(a)}).contextType=e,e}W=ce.slice,_={__e:function(t,e,r,a){for(var s,o,l;e=e.__;)if((s=e.__c)&&!s.__)try{if((o=s.constructor)&&o.getDerivedStateFromError!=null&&(s.setState(o.getDerivedStateFromError(t)),l=s.__d),s.componentDidCatch!=null&&(s.componentDidCatch(t,a||{}),l=s.__d),l)return s.__E=s}catch(d){t=d}throw t}},se=0,Ce=function(t){return t!=null&&t.constructor==null},k.prototype.setState=function(t,e){var r;r=this.__s!=null&&this.__s!=this.state?this.__s:this.__s=C({},this.state),typeof t=="function"&&(t=t(C({},r),this.props)),t&&C(r,t),t!=null&&this.__v&&(e&&this._sb.push(e),X(this))},k.prototype.forceUpdate=function(t){this.__v&&(this.__e=!0,t&&this.__h.push(t),X(this))},k.prototype.render=x,S=[],le=typeof Promise=="function"?Promise.prototype.then.bind(Promise.resolve()):setTimeout,ie=function(t,e){return t.__v.__b-e.__v.__b},O.__r=0,de=/(PointerCapture)$|Capture$/i,V=0,J=ae(!1),N=ae(!0),pe=0;var Fe=0;function p(t,e,r,a,s,o){e||(e={});var l,d,h=e;if("ref"in h)for(d in h={},e)d=="ref"?l=e[d]:h[d]=e[d];var i={type:t,props:h,key:r,ref:l,__k:null,__:null,__b:0,__e:null,__c:null,constructor:void 0,__v:--Fe,__i:-1,__u:0,__source:s,__self:o};if(typeof t=="function"&&(l=t.defaultProps))for(d in l)h[d]===void 0&&(h[d]=l[d]);return _.vnode&&_.vnode(i),i}var xe=ve({registerChild:()=>{},unregisterChild:()=>{},get parentThis(){return null}}),A=class extends k{childRefs=[];ref=L();childrenRef=L();togglerRef=L();headerRef=L();registerChild(e){e&&!this.childRefs.includes(e)&&this.childRefs.push(e)}unregisterChild(e){this.childRefs=this.childRefs.filter(r=>r!==e)}get isCollapsible(){return this.props.collapsible!==!1}get isFocusable(){return this.props.focusable!==!1}get isCollapsed(){return this.childrenRef.current?.getAttribute("data-collapsed")==="true"}get isRootContainer(){return this.props.rootContainer===!0}get isExpanded(){return!this.isCollapsed}componentWillMount(){try{this.context?.registerChild(this.ref)}catch(e){console.log(e)}}get parent(){let e=this.context;return e?.parentThis?.current?e.parentThis.current:null}get root(){let e=this.parent;for(;e;)if(e.parent)e=e.parent;else return e;return null}componentDidMount(){this.ref.current=this}expand(){this.isCollapsible&&(this.childrenRef.current?.setAttribute("data-collapsed","false"),this.togglerRef.current?.setAttribute("data-collapsed","false"),this.props.collapsed=!1)}collapse(){this.isCollapsible&&(this.childrenRef.current?.setAttribute("data-collapsed","true"),this.togglerRef.current?.setAttribute("data-collapsed","true"),this.props.collapsed=!0)}toggle(){this.isCollapsed?this.expand():this.collapse()}expandAll(){this.expand(),this.childRefs.forEach(e=>e.current?.expandAll())}collapseAll(e){e||this.collapse(),this.childRefs.forEach(r=>r.current?.collapseAll())}renderHeader(){return p(x,{children:this.props.header?this.props.header:p(x,{children:"\xA0"})})}renderItems(){return p(xe.Provider,{value:{registerChild:e=>this.registerChild(e),unregisterChild:e=>this.unregisterChild(e),parentThis:this.ref},children:this.props.children})}isElementInViewport(e){let r=e.getBoundingClientRect(),a=this.root?.childrenRef.current?.closest("expandable-root")??document.body;if(a){let s=a.getBoundingClientRect();return r.bottom>=s.top&&r.top<s.bottom}return r.top>=0&&r.left>=0&&r.bottom<=window.innerHeight&&r.right<=window.innerWidth}ensureElementInView(e){e&&!this.isElementInViewport(e)&&e.scrollIntoView({block:"nearest",inline:"nearest"})}focusHeader(){this.isFocusable&&(this.ensureElementInView(this.headerRef.current),this.headerRef.current?.focus({preventScroll:!0}))}handleKeyDown(e){let r=this.headerRef.current,a=r?.getRootNode();if(r&&r===a.activeElement)switch(e.key){case"ArrowLeft":e.stopPropagation(),this.isCollapsed?this.parent?.focusHeader():this.collapse();break;case"ArrowRight":e.stopPropagation(),this.isExpanded?this.getFirstChild()?.focusHeader():this.expand();break;case"ArrowDown":if(e.preventDefault(),e.stopPropagation(),this.isExpanded&&this.childRefs.length>0)this.childRefs[0].current?.focusHeader();else{let s=this;for(;s;){let o=s?.parent;if(!o)break;let l=o.childRefs.indexOf(s.ref);if(l<o.childRefs.length-1){o.childRefs[l+1].current?.focusHeader();return}s=o}}break;case"ArrowUp":if(e.preventDefault(),e.stopPropagation(),this.parent){let s=this.parent.childRefs.indexOf(this.ref);if(s>0){let o=this.parent.childRefs[s-1]?.current;for(;o?.isExpanded&&o.childRefs.length>0;)o=o.childRefs[o.childRefs.length-1]?.current;o?.focusHeader()}else this.parent.focusHeader()}break;case"Home":this.root&&this.root.childRefs.length&&(e.preventDefault(),e.stopPropagation(),this.root.getFirstChild()?.focusHeader());break;case"End":this.root&&this.root.childRefs.length&&(e.preventDefault(),e.stopPropagation(),this.root?.getLastExpandedChild()?.focusHeader());break;case"PageUp":this.root&&this.root.childRefs.length&&(e.preventDefault(),e.stopPropagation(),this.root.getFirstChild()?.focusHeader());break;case"PageDown":this.root&&this.root.childRefs.length&&(e.preventDefault(),e.stopPropagation(),this.root?.getLastExpandedChild()?.focusHeader());break;default:break}}handleWheel(e){let r=this.childrenRef.current;if(r){let a=r.scrollTop===0&&e.deltaY<0,s=r.scrollTop+r.clientHeight>=r.scrollHeight&&e.deltaY>0;!a&&!s&&e.stopPropagation()}}getFirstChild(){return this.childRefs.length>0?this.childRefs[0].current??void 0:null}getLastChild(){if(this.childRefs.length>0)return this.childRefs[this.childRefs.length-1].current??void 0}getLastExpandedChild(){let e=this.getLastChild();for(;e?.isExpanded&&e.childRefs.length>0;)e=e.getLastChild();return e}render(){return p(x,{children:[p("div",{ref:this.headerRef,...this.isFocusable?{tabIndex:0}:{},class:this.isRootContainer?"expander-root-header":"expander-header",onKeyDown:e=>{this.handleKeyDown(e)},onClick:e=>{e.stopPropagation(),this.toggle(),this.headerRef.current?.focus()},children:[this.isRootContainer?p("div",{class:"expander-root-header-left",title:this.props.title}):p("div",{class:"expander-header-left",title:this.props.title,children:this.renderHeader()}),p("div",{class:"expander-header-right",children:[p("span",{class:"expander-icon expand-all",title:"Expand all",onClick:e=>{e.stopPropagation(),this.expandAll()}}),p("span",{class:"expander-icon collapse-all",title:"Collapse all",onClick:e=>{e.stopPropagation(),this.collapseAll()}})]}),this.isCollapsible?p("span",{ref:this.togglerRef,class:`expander-icon toggle ${this.props.collapsed?"closed":"open"}`,"data-collapsed":this.props.collapsed,onClick:e=>{e.stopPropagation(),this.toggle()}}):null]}),p("div",{ref:this.childrenRef,onWheel:e=>{this.isRootContainer&&this.handleWheel(e)},"data-collapsed":this.props.collapsed,class:`children ${this.isCollapsible?"collapsible":""} ${this.isRootContainer?"root-container":""}`,children:this.renderItems()})]})}};A.contextType=xe;var Q=class extends k{renderItems(){return p(x,{children:this.props.data.items.map(e=>te(e))})}render(){return p("div",{class:"result-body expandable-root",children:p(A,{focusable:!1,collapsible:!1,rootContainer:!0,children:this.renderItems()})})}},Z=class extends k{render(){let e=this.props.data.level.toLocaleLowerCase();return p("table",{id:this.props.data.id,class:`messages ${e}-message`,children:p("tr",{class:"message-row",children:[p("td",{class:"time",children:this.props.data.timestamp}),p("td",{class:`${e} level`,children:p("span",{class:`label ${e}`,children:this.props.data.level})}),this.props.data.html?p("td",{class:"message",dangerouslySetInnerHTML:{__html:this.props.data.message}}):p("td",{class:"message",children:this.props.data.message})]})})}},ee=class extends k{renderHeader(){return p(x,{children:[p("span",{class:"elapsed",title:"Elapsed time",children:this.props.data.elapsed_time}),p("span",{class:`label ${this.props.data.status.toLowerCase()}`,children:this.props.data.type}),p("span",{class:"assign",children:this.props.data.assign.join("    ")}),p("span",{class:"name",children:[this.props.data.owner?p("span",{class:"parent-name",children:[this.props.data.owner," . "]}):null,this.props.data.name]}),"\xA0",p("span",{class:"arg",children:this.props.data.args})]})}renderItems(){return p(x,{children:[p("table",{class:"metadata keyword-metadata",children:[this.props.data.doc?p("tr",{children:[p("th",{children:"Documentation:"}),p("td",{class:"doc",dangerouslySetInnerHTML:{__html:this.props.data.doc}})]}):null,this.props.data.tags&&this.props.data.tags.length>0?p("tr",{children:[p("th",{children:"Tags:"}),p("td",{class:"tags",children:this.props.data.tags.join(", ")})]}):null,this.props.data.timeout?p("tr",{children:[p("th",{children:"Tags:"}),p("td",{class:"tags",children:this.props.data.timeout})]}):null,p("tr",{children:[p("th",{children:"Start / End / Elapsed:"}),p("td",{children:[this.props.data.start_time," / $",this.props.data.elapsed_time," / $",this.props.data.elapsed_time]})]})]}),this.props.data.items.map(e=>te(e))]})}render(){return p("div",{class:"keyword",children:p(A,{header:this.renderHeader(),collapsed:this.props.data.status!=="FAIL",title:`${this.props.data.type} ${this.props.data.owner?this.props.data.owner+"."+this.props.data.name:this.props.data.name} [${this.props.data.status}]`,children:this.renderItems()})})}};function te(t){switch(t.node_type){case"root":return p(Q,{data:t});case"message":return p(Z,{data:t});case"keyword":return p(ee,{data:t});default:return p("div",{children:"Unknown node type"})}}var B=class extends k{render(){return te(this.props.data)}};var ye=`:target {
    overflow: hidden;
}

/* Generic and misc styles */
.result-body {
    /* font-family: var(--vscode-font-family); */
    font-family: Helvetica, sans-serif;
    color: var(--vscode-robotcode-logForeground);
    background-color: var(--vscode-robotcode-logBackground);
}

.root-container {
    overflow-y: auto;
    max-height: var(--notebook-cell-output-max-height);
}

table {
    table-layout: fixed;
    word-wrap: break-word;
    empty-cells: show;
}

th,
td {
    vertical-align: top;
}


hr {
    height: 1px;
    border: 0;
}

a,
a:link,
a:visited {
    text-decoration: none;
}

a>img {
    border-width: 1px !important;
    border-style: solid !important;
}

a:hover,
a:active {
    text-decoration: underline;
}

.parent-name {
    font-size: x-small;
}

.message {
    white-space: pre-wrap;
}

/* Headers */
#header {
    width: 65em;
    height: 3em;
    margin: 20px 0 6px 0;
}

h1 {
    float: left;
    margin: 0 0 0.5em 0;
    width: 75%;
}

h2 {
    clear: left;
}

#generated {
    float: right;
    text-align: right;
    font-size: 0.9em;
    white-space: nowrap;
}

/* Documentation headers */
.doc>h2 {
    font-size: 1.2em;
}

.doc>h3 {
    font-size: 1.1em;
}

.doc>h4 {
    font-size: 1.0em;
}

.label {
    padding: 2px 5px;
    font-size: 0.75em;
    letter-spacing: 1px;
    white-space: nowrap;
    border-radius: 3px;
    color: var(--vscode-robotcode-logLabelForeground);
    background-color: var(--vscode-robotcode-logLabelBackground);
}

.label.debug,
.label.trace,
.label.error,
.label.keyword {
    letter-spacing: 0;
}

.label.pass,
.label.fail,
.label.error,
.label.skip,
.label.warn {
    font-weight: bold;
    color: var(--vscode-robotcode-logLabelWarnForeground);
    background-color: var(--vscode-robotcode-logLabelWarnBackground);
}

.label.pass {
    background-color: #97bd61;
    color: var(--vscode-robotcode-logLabelPassForeground);
    background-color: var(--vscode-robotcode-logLabelPassBackground);
}

.label.fail,
.label.error {
    color: var(--vscode-robotcode-logLabelErrorForeground);
    background-color: var(--vscode-robotcode-logLabelErrorBackground);
}

.label.skip,
.label.warn {
    background-color: #fed84f;
    color: var(--vscode-robotcode-logLabelWarnForeground);
    background-color: var(--vscode-robotcode-logLabelWarnBackground);
}

/* Top right header */
#top-right-header {
    position: fixed;
    top: 0;
    right: 0;
    z-index: 1000;
    width: 12em;
    text-align: center;
}

#log-level-selector {
    padding: 0.3em 0;
    font-size: 0.9em;
    border-bottom-left-radius: 4px;
}`;var we=`.suite,
.test,
#errors {
    border-width: 1px;
    border-style: solid;
    padding: 0.3em 0.2em;
    margin: 0.2em 0;
}


.test {
    border-style: dashed;
}

#errors,
.messages {
    width: 100%;
    border-spacing: 0;
}

.children {
    margin-left: 0em;
}

.children.collapsible {
    margin-left: 1.4em;
}


.children[data-collapsed=true] {
    display: none;
}

.children[data-collapsed=false] {
    display: block;
}


.suite,
.test,
.keyword {
    border-left-width: 1px;
    border-left-style: solid;
    border-color: transparent;
}

.keyword:hover {
    border-left-style: dashed;
    border-color: inherit;
}

#s1,
.suite>.children>.keyword {
    margin-left: 0;
}

/* Suite, test and kw headers */
.expander-header {
    border-width: 0px;
    border-radius: 5px;
    position: relative;
    margin-left: 2px;
}

.expander-root-header {
    border-width: 0px;
    border-radius: 5px;
    position: relative;
    margin-left: 2px;
}

.expander-header:hover {
    background-color: var(--vscode-robotcode-expanderHeaderHoverBackground);
    outline: 1px dashed var(--vscode-robotcode-expanderHeaderHoverOutline);
    outline-offset: -1px;
}

.expander-header:focus {
    color: var(--vscode-robotcode-expanderHeaderFocusForeground);
    background-color: var(--vscode-robotcode-expanderHeaderFocusBackground);
    outline: 1px solid var(--vscode-robotcode-expanderHeaderFocusOutline);
    outline-offset: -1px;
}

.expander-header:focus:hover {
    color: var(--vscode-robotcode-expanderHeaderFocusForeground);
    background-color: var(--vscode-robotcode-expanderHeaderHoverBackground);
    outline: 1px solid var(--vscode-robotcode-expanderHeaderFocusOutline);
    outline-offset: -1px;
}

.expander-header-left {
    cursor: pointer;
    padding: 3px 80px 3px 20px;
}

.expander-root-header-left {
    padding: 3px 80px 3px 20px;
    height: 1em;
}

.expander-header-right {
    position: absolute;
    right: 0px;
    top: 2px;
    cursor: default;
}

.expander-header .label {
    margin-right: 0.5em;
}

.name {
    font-weight: bold;
    white-space: pre-wrap;
}

.arg,
.assign {
    white-space: pre-wrap;
}

.elapsed {
    float: right;
    padding-left: 1em;
}

.expander-icon {
    color: var(--vscode-robotcode-expanderIconForeground);
    text-align: center;
    vertical-align: middle;
    font-family: monospace;
    fill: var(--vscode-icon-foreground);
    cursor: pointer;
    display: inline-block;
    width: 1em;
    height: 1em;
    padding: 1px;
    border-radius: 5px;
}

.expander-icon:hover {
    cursor: pointer;
    background-color: var(--vscode-robotcode-expanderIconHoverBackground);
    outline: 1px dashed var(--vscode-robotcode-expanderIconHoverOutline);
    outline-offset: -1px;
}

.expander-icon.toggle[data-collapsed=false]::after {
    content: '-';
}

.expander-icon.toggle[data-collapsed=true]::after {
    content: '+';
}

.expander-icon.toggle {
    margin: 0 auto;
    position: absolute;
    left: 0px;
    top: 3px;
}

.expander-header .expand-all,
.expander-header .collapse-all,
.expander-header .link,
.expander-root-header .expand-all,
.expander-root-header .collapse-all,
.expander-root-header .link {
    visibility: hidden;
}

.collapse-all::after {
    content: '\u25B2';
}

.expand-all::after {
    content: '\u25BC';
}

.link::after {
    content: '\u21D7';
}

.expander-header:hover .collapse-all,
.expander-header:hover .expand-all,
.expander-header:hover .link,
.expander-root-header:hover .collapse-all,
.expander-root-header:hover .expand-all,
.expander-root-header:hover .link {
    visibility: visible;
}

/* Messages and errors */
.messages .time,
.messages .message {
    font-family: monospace;
}

#errors .message {
    font-family: monospace;
}

.message-row {
    height: 20px;
}

.time {
    width: 5.5em;
}

.error-time {
    width: 11em;
    white-space: nowrap;
}

.level {
    width: 5em;
    text-align: center;
}

/* Message tables - these MUST NOT be combined together because otherwise
   dynamically altering them based on visible log level is not possible. */
.trace-message {
    display: none;
}

.debug-message {
    display: none;
}

/* Metadata */
.metadata {
    width: 100%;
    border-spacing: 0.2em;
}

.metadata th {
    width: 12em;
    vertical-align: top;
    text-align: left;
}

.metadata td {
    vertical-align: top;
}

.keyword-metadata {
    font-size: 1em;
}`;var ke=`.doc>* {
    margin: 0.7em 1em 0.1em 1em;
    padding: 0;
}

.doc>p,
.doc>h1,
.doc>h2,
.doc>h3,
.doc>h4 {
    margin: 0.7em 0 0.1em 0;
}

.doc>*:first-child {
    margin-top: 0.1em;
}

.doc table {
    background: transparent;
    border-collapse: collapse;
    empty-cells: show;
    font-size: 0.9em;
}

.doc table th,
.doc table td {
    background: transparent;
    padding: 0.1em 0.3em;
    height: 1.2em;
}

.doc table th {
    text-align: center;
    letter-spacing: 0.1em;
}

.doc pre {
    border-radius: 2px;
    font-size: 1.1em;
    letter-spacing: 0.05em;
}

.doc code {
    border-radius: 2px;
    padding: 0 0.2em;
    letter-spacing: 0.05em;
}

.doc li {
    list-style-position: inside;
    list-style-type: square;
}

.doc img,
.doc table,
.doc table th,
.doc table td {
    border-width: 1px;
    border-style: solid;
}

.doc hr {
    background: #ccc;
    /* Fallback value */
    height: 1px;
    border: 0;
}`;var Qe=t=>{let e=new CSSStyleSheet({media:"all"});e.replaceSync(ye);let r=new CSSStyleSheet({media:"all"});r.replaceSync(we);let a=new CSSStyleSheet({media:"all"});return a.replaceSync(ke),{renderOutputItem(s,o,l){let d=o.shadowRoot;if(!d){d=o.attachShadow({mode:"open"}),d.adoptedStyleSheets=[...document.adoptedStyleSheets,e,r,a];let i=document.createElement("div");i.id="root",d?.append(i)}let h=d.querySelector("#root");h&&be(p(B,{data:s.json()}),h)}}};export{Qe as activate};
