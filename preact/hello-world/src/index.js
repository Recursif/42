// import 'promise-polyfill';
// import 'isomorphic-fetch';
import { h, render } from 'preact';
import './style';

let root;
function init() {
root = render ((
	  <div id="foo">
	    <span>Hello, world!</span>
	    <button onClick={ e => alert("hi!") }>Click me</button>
	  </div>
	), document.body, root);
}

// register ServiceWorker via OfflinePlugin, for prod only:
if (process.env.NODE_ENV==='production') {
	require('./pwa');
}

init();
