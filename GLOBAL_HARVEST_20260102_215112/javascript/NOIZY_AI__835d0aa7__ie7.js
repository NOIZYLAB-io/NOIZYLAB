/* To avoid CSS expressions while still supporting IE 7 and IE 6, use this script */
/* The script tag referencing this file must be placed before the ending body tag. */

/* Use conditional comments in order to target IE 7 and older:
	<!--[if lt IE 8]><!-->
	<script src="ie7/ie7.js"></script>
	<!--<![endif]-->
*/

(function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'icon\'">' + entity + '</span>' + html;
	}
	var icons = {
		'icon-search': '&#xe600;',
		'icon-arrow-back': '&#xe601;',
		'icon-chevron-right': '&#xe602;',
		'icon-close': '&#xe603;',
		'icon-menu': '&#xe604;',
		'icon-arrow-forward': '&#xe605;',
		'icon-twitter': '&#xe606;',
		'icon-github': '&#xe607;',
		'icon-download': '&#xe608;',
		'icon-star': '&#xe609;',
		'icon-warning': '&#xe610;',
		'icon-hint': '&#xe611;',
		'icon-home': '&#xe906;',
		'icon-bullhorn': '&#xe91a;',
		'icon-book': '&#xe91f;',
		'icon-file-empty': '&#xe924;',
		'icon-file-text2': '&#xe926;',
		'icon-file-zip': '&#xe92b;',
		'icon-folder-download': '&#xe933;',
		'icon-envelope': '&#xe945;',
		'icon-printer': '&#xe954;',
		'icon-box-add': '&#xe95e;',
		'icon-download2': '&#xe960;',
		'icon-floppy-disk': '&#xe962;',
		'icon-download3': '&#xe9c7;',
		'icon-sphere': '&#xe9c9;',
		'icon-earth': '&#xe9ca;',
		'icon-link': '&#xe9cb;',
		'icon-attachment': '&#xe9cd;',
		'icon-eye': '&#xe9ce;',
		'icon-bookmark': '&#xe9d2;',
		'icon-star-empty': '&#xe9d7;',
		'icon-star-full': '&#xe9d9;',
		'icon-point-right': '&#xea04;',
		'icon-warning2': '&#xea07;',
		'icon-notification': '&#xea08;',
		'icon-circle-up': '&#xea41;',
		'icon-circle-right': '&#xea42;',
		'icon-circle-down': '&#xea43;',
		'icon-circle-left': '&#xea44;',
		'icon-command': '&#xea4e;',
		'icon-shift': '&#xea4f;',
		'icon-ctrl': '&#xea50;',
		'icon-opt': '&#xea51;',
		'icon-share': '&#xea7d;',
		'icon-new-tab': '&#xea7e;',
		'icon-mail4': '&#xea86;',
		'icon-facebook': '&#xea91;',
		'icon-instagram': '&#xea92;',
		'icon-youtube': '&#xea9d;',
		'icon-file-pdf': '&#xeadf;',
		'0': 0
		},
		els = document.getElementsByTagName('*'),
		i, c, el;
	for (i = 0; ; i += 1) {
		el = els[i];
		if(!el) {
			break;
		}
		c = el.className;
		c = c.match(/icon-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
}());
